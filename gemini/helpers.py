import re, os
from dataclasses import dataclass


@dataclass
class GeminiConfig:
    project_id: str
    region: str
    model_name: str
    temperature: float


CFG = GeminiConfig(
    project_id=os.environ.get("GCP_PROJECT", "DEFAULT"),
    region=os.environ.get("GCP_REGION", "us-central1"),
    model_name="gemini-1.5-pro",
    temperature=0.1,
)


def clean_generated_code(text: str) -> str:
    """
    Cleans Gemini-generated code by removing markdown fences and
    preserving the original Python code exactly.
    """

    if not text:
        return ""

    # Remove ```python or ``` blocks
    text = re.sub(r"^```(?:python)?\s*", "", text, flags=re.IGNORECASE | re.MULTILINE)
    text = re.sub(r"\s*```$", "", text, flags=re.MULTILINE)

    # Strip leading/trailing whitespace only
    return text.strip()


def load_system_instruction(path: str) -> str:
    if not os.path.exists(path):
        raise FileNotFoundError(f"System instruction file not found: {path}")

    with open(path, "r") as f:
        return f.read().strip()


def build_user_prompt(dag_template: str, payload: dict) -> str:
    return f"""
            DAG TEMPLATE:
            {dag_template}

            JSON PAYLOAD:
            {payload}

            Replace placeholders and return the final DAG Python code.
            """.strip()