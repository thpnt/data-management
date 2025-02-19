# airflow/dags/simple_dag.py
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Import your function (adjust the import as needed)
from etl.script import main

def run_my_script():
    # You can also simply import and run the logic here instead of calling a subprocess.
    main()

with DAG(
    dag_id='simple_dag',
    start_date=datetime(2025, 19, 1),
    schedule_interval='0 6 * * *',
    catchup=False,
) as dag:
    task = PythonOperator(
        task_id='run_my_script',
        python_callable=run_my_script
    )
