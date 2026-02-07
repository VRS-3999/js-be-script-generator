# Sample Paylaod

#### BG_SQL_EXECUTOR
```JSON
{
  "dag_type": "BG_SQL_EXECUTOR",
  "dag_id": "paops-auto-pa-bq-sync",
  "tenant": "paops",
  "app": "auto_pa",
  "lob": "pss",
  "username": "rohit_patidar",
  "email": "patidarr@aetna.com",
  "cost_center": "0000230810",

  "notify_success": true,
  "notify_failure": true,
  "schedule_interval": "0 * * * *",

  "bq_tenant": "pmcydealclnt",
  "bq_table_id": "auto_pa_audit_data_final",
  "bq_streaming_table_id": "auto_pa_audit_data_streaming_temp",

  "dev_failure_emails": [
    "patidarr@aetna.com",
    "praneeth.nagamandla@cvshealth.com"
  ],

  "external_sql_file": {
    "fileList": [
      {
        "name": "bq_stream_table_to_view.sql"
      }
    ]
  }
}

```

#### BG_SQL_EXECUTOR
```JSON
{
  "dag_type": "BT_TO_BQ_STREAMING",

  "project_id": "anbc-pss-dev",
  "tenant": "paops",
  "lob": "pss",
  "app": "auto_pa",
  "region": "us-east4",

  "username": "parthiv.borghain",
  "email": "parthiv.borghain@company.com",
  "cost_center": "295630",

  "dag_id": "paops-pss-auto-pa-bt-to-bq-stream",
  "dag_tags": [
    "tenant:paops",
    "app:auto_pa",
    "owner:parthiv.borghain@company.com",
    "cost-center:295630"
  ],

  "bq_tenant": "pmcydealclnt",
  "bq_table_id": "auto_pa_audit_data",

  "bt_instance_id": "paops-app-pss-dev",
  "bt_table_id": "auto_pa_audit_data",
  "bt_column_id": "cf_auto_pa_audit_data",

  "temp_bucket": "gs://paops-data-pss-dev/users/patidar/temp/auto_pa",
  "dataflow_job_name": "auto-pa-bt-to-bq-streaming-dag"
}
```

### TODO
1. .env Approach using decouple
2. Remove DAG Folder approach
3. BG_SQL --> BQ_SQL