from airflow import DAG
from airflow.providers.databricks.operators.databricks import DatabricksRunNowOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "airflow",
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="stock_trading_etl_pipeline",
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    tags=["databricks", "etl", "stock"],
) as dag:

    run_stock_etl = DatabricksRunNowOperator(
        task_id="run_stock_trading_etl_job",
        databricks_conn_id="databricks_default",
        job_id=307842103734326
    )