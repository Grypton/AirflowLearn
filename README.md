Commands:
1. Fetch the docker file : ```curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.10.5/docker-compose.yaml'```
2. Remove unnecessary items for local:
    1. Make CeleryExecutor to LocalExecutor
    2. Remove celery related items : 
        1. Comment ```AIRFLOW__CELERY__RESULT_BACKEND```, ```AIRFLOW__CELERY__BROKER_URL```
        2. Comment ```redis``` dependency from ```x-airflow-common``` 
        3. Comment ```redis``` related configuration
        4. Comment ```airflow-worker``` related configuration
        5. Comment ```flower``` related configuration

3. Run the command ```docker-compose up airflow-init```: This sets up database 
4. Run the command ```docker-compose up -d``` to run airflow in detached mode
5. Run ```docker ps``` to see container and related information
6. To remove airflow with volume: ```docker-compose down -v```
7. Remove airflow default examples by turning the values of ```AIRFLOW__CORE__LOAD_EXAMPLES``` to ```'false'```