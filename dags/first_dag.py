from airflow import DAG
from datetime import datetime, timedelta

from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
 
default_args = {
    "owner": "grypton",
    "retries": 5,
    "retry_delay": timedelta(minutes=2)
}


with DAG(
    dag_id="first_dag",
    default_args=default_args,
    description="This is the first DAG that I created",
    start_date=datetime(2025, 4, 1, 18, 0, 0),
    schedule_interval="@daily",
) as dag:
    

### using Bash operator 

    # task1 = BashOperator(
    #     task_id="task1",
    #     bash_command="echo 'Hello World!!!, this is the very first dag'",
    # )

    # task2 = BashOperator(
    #     task_id="task2",
    #     bash_command="echo 'I am second task'",
    # )

    # task3 = BashOperator(
    #     task_id="task3",
    #     bash_command="echo 'I am third task'",
    # )

    # task1.set_downstream(task2)
    # task1.set_downstream(task3) # task1 >> [task2, task3]

    # task1.set_downstream(task2)
    # task2.set_downstream(task3) # task1 >> task2 >> task3


### using Python Operator

    # def greet1():
    #     print("Hello from task1 PythonOperator")

    # def greet2():
    #     print("Hello from task2 PythonOperator")

    # def greet3():
    #     print("Hello from task3 PythonOperator")

    # task1 = PythonOperator(
    #     task_id="task1",
    #     python_callable=greet1,
    # )
    
    # task2 = PythonOperator(
    #     task_id="task2",
    #     python_callable=greet2,
    # )

    # task3 = PythonOperator(
    #     task_id="task3",
    #     python_callable=greet3,
    # )

    # task1.set_downstream(task2) # task1 >> task2

    # task1.set_downstream(task2)
    # task1.set_downstream(task3) # task1 >> [task2, task3]

    # task1.set_downstream(task2)
    # task2.set_downstream(task3) # task1 >> task2 >> task3


### using op_kwargs in python operator
    # def get_greeting(name):
    #     return f"Hello {name} from PythonOperator"

    # task1 = PythonOperator(
    #     task_id="task1",
    #     python_callable=get_greeting,
    #     op_kwargs={"name": "Grypton"},
    # )

    # task1


### using xcoms in python operator
    # def get_name():
    #     return "Grypton"
    
    # def greet(age, ti):
    #     name = ti.xcom_pull(task_id="get_name")
    #     print(f"Hello {name}, you are {age} years old")

    # task1 = PythonOperator(
    #     task_id="get_name",
    #     python_callable=get_name,
    # )

    # task2 = PythonOperator(
    #     task_id="greet",
    #     python_callable=greet,
    #     op_kwargs={"age": 25},
    # )

    # task1 >> task2 # task1.set_downstream(task2)

# ## using xcoms in python operator with key using direct return feature
#     def get_name():
#         return {"first_name": "Grypton", "last_name": "Noname", "age": 25}
    
#     def greet(ti):
#         first_name = ti.xcom_pull(task_ids="get_name", key="first_name")
#         last_name = ti.xcom_pull(task_ids="get_name", key="last_name")
#         age = ti.xcom_pull(task_ids="get_name", key="age")
#         print(f"Hello {first_name} {last_name}, you are {age} years old")

#     task1 = PythonOperator(
#         task_id="get_name",
#         python_callable=get_name,
#     )

#     task2 = PythonOperator(
#         task_id="greet",
#         python_callable=greet,
#     )

#     task1 >> task2 # task1.set_downstream(task2)
    
 ## using xcoms in python operator with key using xcom_push feature
    def get_name(ti):
        ti.xcom_push(key="first_name", value="Grypton")
        ti.xcom_push(key="last_name", value="Noname")
        ti.xcom_push(key="age", value=25)
    
    def greet(ti):
        first_name = ti.xcom_pull(task_ids="get_name", key="first_name")
        last_name = ti.xcom_pull(task_ids="get_name", key="last_name")
        age = ti.xcom_pull(task_ids="get_name", key="age")
        print(f"Hello {first_name} {last_name}, you are {age} years old")

    task1 = PythonOperator(
        task_id="get_name",
        python_callable=get_name,
    )

    task2 = PythonOperator(
        task_id="greet",
        python_callable=greet,
    )

    task1 >> task2 # task1.set_downstream(task2)


