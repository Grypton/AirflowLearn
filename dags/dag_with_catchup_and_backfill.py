from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "grypton",
    "retries": 5,
    "retry_delay": timedelta(minutes=2)
}

with DAG(
    dag_id="dag_with_catchup_and_backfill",
    default_args=default_args,
    description="This is the first DAG that I created",
    start_date=datetime(2025, 3, 28),
    schedule_interval="@daily",
    catchup=True,
) as dag:

    task1 = BashOperator(
        task_id="task1",
        bash_command="echo 'I am first task'",
    )

    task1