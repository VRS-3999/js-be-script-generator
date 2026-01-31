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

        # UUID-based DAG filename
        dag_uuid = uuid.uuid4().hex
        dag_path = os.path.join(
            os.environ["DAGS_FOLDER"],
            f"{dag_uuid}.py",
        )

        with open(dag_path, "w") as f:
            f.write(dag_code)

        return {
            "dag_id": payload["dag_id"],
            "dag_uuid": dag_uuid,
            "dag_path": dag_path,
        }
