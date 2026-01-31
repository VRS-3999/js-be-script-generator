from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, Any
from settings.config import BG_SQL_EXECUTOR
from gemini.core import DagGenerator, CFG
from utils.common import _normalize_list

app = FastAPI()

# ✅ Allow frontend (React) to call API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/generate_script")
async def generate_script(payload: Dict[str, Any]):
    if payload.get('dag_type') == BG_SQL_EXECUTOR:
        generator = DagGenerator(
            cfg=CFG,
            system_instruction_md_path="prompts/system_instruction.md",
        )
        with open("templates/bg_sql_executor_file_input.py.template", "r") as f:
            dag_template = f.read()
        external_sql_filename = (
            payload.get("external_sql_file", {})
            .get("fileList", [{}])[0]
            .get("name")
        )
        if not external_sql_filename:
            raise ValueError("external_sql_file.fileList[0].name is required")
        dag_config = {
            "project_id": CFG.project_id,
            "tenant": payload.get("tenant", ""),
            "app": payload.get("app", ""),
            "lob": payload.get("lob", ""),
            "region": CFG.region,
            "username": payload.get("username", ""),
            "cost_center": payload.get("cost_center", ""),

            "dag_repo": "auto-pa-features-update-bq",
            "dag_id": payload.get("dag_id", ""),
            "dag_tags": [
                f"tenant:{payload.get('tenant', '')}",
                f"app:{payload.get('app', '')}",
                f"owner:{payload.get('email', '')}",
                f"cost-center:{payload.get('cost_center', '')}",
            ],

            "bq_tenant": payload.get("bq_tenant", ''),
            "bq_table_id": payload.get("bq_table_id", ''),
            "bq_streaming_table_id": payload.get("bq_streaming_table_id", ''),

            "owner_email": payload.get("email", ''),
            "to_emails": _normalize_list(payload.get("dev_failure_emails", '')),
            "cc_emails": [],

            "notify_success": payload.get("notify_success", ''),
            "notify_failure": payload.get("notify_failure", ''),
            "schedule_interval": payload.get("schedule_interval", "0 * * * *"),
            "sql_file_name": external_sql_filename,
        }

        result = generator.generate_and_write_dag(
            dag_template=dag_template,
            payload=dag_config,
        )
        return result
    return {
        "status": "success"
    }
