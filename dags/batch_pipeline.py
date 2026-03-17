from datetime import datetime, timedelta
try:
    from airflow import DAG
    from airflow.operators.python import PythonOperator
    from airflow.operators.empty import EmptyOperator
    AIRFLOW = True
except ImportError:
    AIRFLOW = False

def run(**ctx): return "ok"

if AIRFLOW:
    with DAG("batch_etl_pipeline", schedule_interval="0 6 * * *",
             start_date=datetime(2024,1,1), catchup=False, tags=["etl"]) as dag:
        s = EmptyOperator(task_id="start")
        e = PythonOperator(task_id="extract", python_callable=run)
        t = PythonOperator(task_id="transform", python_callable=run)
        v = PythonOperator(task_id="validate", python_callable=run)
        l = PythonOperator(task_id="load", python_callable=run)
        end = EmptyOperator(task_id="end")
        s >> e >> t >> v >> l >> end
