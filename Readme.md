# Sample Paylaod

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