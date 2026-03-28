BG_SQL_EXECUTOR = "BG_SQL_EXECUTOR"
BT_TO_BQ_STREAMING = "BT_TO_BQ_STREAMING"
INLINE_SQL = "INLINE_SQL"
EXTERNAL_SQL = "EXTERNAL_SQL"


MANAGER_DEFAULTS = {
    "test": {
        "tenant": "email",
        "lob": "platform",
        "app": "data-pipeline",
        "cost_center": "ENG-PLATFORM",

        "schedule_interval": "0 * * * *",
        "schedule_description": "schedule_description input",
        "brief_description": "brief_description input",
        "sql_source_type": "test type",
        "inline_sql_query": "inline_sql_query type",
        "dag_repo": "dag_repo input",
        "dag_name": "dag_name input",

        "notify_success": True,
        "notify_failure": True,
        "email": "test@email.com",
        "test_success_emails": [
            "test@email.com"
        ],
        "test_failure_emails": [
            "test@email.com"
        ],
        "dev_failure_emails": [
            "test@email.com"
        ],
        "dev_success_emails": [
            "test@email.com"
        ],

        "prod_failure_emails": [
            "alerts@email.com"
        ],
        "prod_success_emails": [
            "alerts@email.com"
        ],
        "temp_bucket": "dataflow-temp-bucket",
        "bt_instance_id": "prod-instance",
        "bt_column_id": "cf",
        "dataflow_job_name": "bt-bq-streaming",
        "username": "test username",
        "bq_tenant": "bq_tenant input",
        "bq_table_id": "bq_table_id input",
        "bq_streaming_table_id": "bq_streaming_table_id input",
        "bt_table_id": "bt_table_id input",
        "table_name": "table_name input",
        "gcs_source_path": "gcs_source_path input",
        "source_format": "CSV",
        "skip_leading_rows": 56,
        "field_delimiter": ",",
        "autodetect": True,
        "allow_jagged_rows": True,
        "ignore_unknown_values": False,
        "allow_quoted_newlines": True,
        "table_schema": "table_schema input",
        "create_table": True,
        "create_table_sql": "create_table_sql input",
        "load_data_sql": "load_data_sql input",
        "custom_capabilities": "dataproc_processing",
        "custom_description": "custom_description input",
        "operation_type": "bt_migration",
        "dev_resource_sa": "dev-resource-sa@project-id.iam.gserviceaccount.com",
        "dev_connect_sa": "dev-connect-resource-sa@project-id.iam.gserviceaccount.com",
        "test_resource_sa": "test-resource-sa@project-id.iam.gserviceaccount.com",
        "test_connect_sa": "test-connect-resource-sa@project-id.iam.gserviceaccount.com",
        "prod_resource_sa": "prod-resource-sa@project-id.iam.gserviceaccount.com",
        "prod_connect_sa": "prod-connect-resource-sa@project-id.iam.gserviceaccount.com"
    },

    "rahul": {
        "tenant": "email",
        "lob": "analytics",
        "app": "reporting",
        "cost_center": "ENG-ANALYTICS",
        "schedule_interval": "0 */2 * * *",
        "notify_success": False,
        "notify_failure": True,
        "dev_failure_emails": [
            "rahul@email.com"
        ]
    }
}