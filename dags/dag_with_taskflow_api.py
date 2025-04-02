from airflow.decorators import dag, task

from datetime import datetime, timedelta

default_args = {
    "owner": "grypton",
    "retries": 5,
    "retry_delay": timedelta(minutes=2)
}

@dag(
    dag_id="dag_with_taskflow_api",
    default_args=default_args,
    description="This is the first task DAG that I created",
    start_date=datetime(2025, 4, 1, 18, 0, 0),
    schedule_interval="@daily",
)
def taskflow_api_dag():
    @task(multiple_outputs=True)
    def getname():
        return {
            "first_name": "Grypton",
            "last_name": "Noname"
        }

    @task
    def getage():
        return 25
    
    @task
    def greet(name, age):
        print(f"Hello {name['first_name']} {name['last_name']}, you are {age} years old")

    name = getname()
    age = getage()
    greet(name, age)

greet_dag = taskflow_api_dag()