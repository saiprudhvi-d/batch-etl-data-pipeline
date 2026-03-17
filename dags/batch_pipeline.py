"""
Airflow DAG: raw -> clean -> curated
"""
from datetime import datetime, timedelta
try:
    from airflow import DAG
    from airflow.operators.python import PythonOperator
    from airflow.operators.empty import EmptyOperator
    AIRFLOW = True
except ImportError:
    AIRFLOW = False

def extract_task(**ctx): return "Extracted"
def transform_task(**ctx): return "Transformed"
def validate_task(**ctx): return "Validated"
def load_task(**ctx): return "Loaded"

if AIRFLOW:
    with DAG("batch_etl_pipeline",
             default_args={"owner":"data-eng","retries":2,"retry_delay":timedelta(minutes=5)},
             schedule_interval="0 6 * * *", start_date=datetime(2024,1,1), catchup=False,
             tags=["etl","batch"]) as dag:
        s = EmptyOperator(task_id="start")
        e = PythonOperator(task_id="extract", python_callable=extract_task)
        t = PythonOperator(task_id="transform", python_callable=transform_task)
        v = PythonOperator(task_id="validate", python_callable=validate_task)
        l = PythonOperator(task_id="load", python_callable=load_task)
        end = EmptyOperator(task_id="end")
        s >> e >> t >> v >> l >> end
