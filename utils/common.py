import os 
from gemini.core import DagGenerator, CFG

def _normalize_list(value):
    if not value:
        return []
    if isinstance(value, list):
        return value
    return [value]

def is_debug() -> bool:
    return os.environ.get("DEBUG", "false").lower() == "true"


def load_template(path: str) -> str:
    with open(path, "r") as f:
        return f.read()

def get_generator(system_prompt: str) -> DagGenerator:
    return DagGenerator(
        cfg=CFG,
        system_instruction_md_path=system_prompt,
    )

def generate_and_write_dag(dag_template, dag_config):
    generator = DagGenerator(
        cfg=CFG,
        system_instruction_md_path="prompts/system_instruction.md",
    )
    return generator.generate_and_write_dag(
                dag_template=dag_template,
                payload=dag_config,
            )