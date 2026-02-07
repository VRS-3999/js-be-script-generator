import logging
import ast
import uuid
import os
from google import genai
from google.genai import types
from .helpers import clean_generated_code, load_system_instruction, build_user_prompt, CFG

logger = logging.getLogger(__name__)


class DagGenerator:
    def __init__(
        self,
        cfg,
        system_instruction_md_path: str,
    ):
        self.cfg = cfg
        self.system_instruction = load_system_instruction(
            system_instruction_md_path
        )

        self.client = genai.Client(
            vertexai=True,
            project=cfg.project_id,
            location=cfg.region,
        )

    def generate_dag_code(self, user_prompt: str) -> str:
        logger.debug(
            "Generating code: model=%s temperature=%.2f",
            self.cfg.model_name,
            self.cfg.temperature,
        )

        contents = [
            types.Content(
                role="user",
                parts=[types.Part.from_text(text=user_prompt)],
            )
        ]

        resp = self.client.models.generate_content(
            model=self.cfg.model_name,
            contents=contents,
            config=types.GenerateContentConfig(
                temperature=self.cfg.temperature,
                system_instruction=self.system_instruction,
                response_mime_type="text/plain",
            ),
        )

        text = resp.text or ""

        # Clean up markdown/code fences only
        text = clean_generated_code(text)

        logger.debug("Generation complete (chars=%d).", len(text))
        return text

    def generate_and_write_dag(
        self,
        dag_template: str,
        payload: dict,
    ) -> dict:
        user_prompt = build_user_prompt(dag_template, payload)
        dag_code = self.generate_dag_code(user_prompt)
        # Validate generated Python
        ast.parse(dag_code)
        return {
            "dag_code": dag_code
        }

    def cron_from_description_ai(self, description: str) -> str:
        """
        Uses Gemini to convert a human cron description into a UTC cron expression.

        Example:
            Input:  "Everything is in utc… daily at 7 AM EST"
            Output: "0 12 * * *"
        """

        prompt = f"""
            {self.system_instruction}

            Description:
            {description}
            """

        contents = [
            types.Content(
                role="user",
                parts=[types.Part.from_text(text=prompt)],
            )
        ]

        response = self.client.models.generate_content(
            model=self.cfg.model_name,
            contents=contents,
            config=types.GenerateContentConfig(
                temperature=0.0,  # deterministic output
                response_mime_type="text/plain",
            ),
        )

        cron = (response.text or "").strip()

        # Basic validation: must have 5 cron fields
        if len(cron.split()) != 5:
            raise ValueError(f"Invalid cron returned by AI: '{cron}'")

        return cron
