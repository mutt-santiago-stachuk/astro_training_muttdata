from airflow.decorators import dag, task
from datetime import datetime

@dag(
    schedule=None,
    catchup=False,
    default_args={'retries': 1},
    tags=["example"]
)
def github():
    @task
    def my_task():
        return "include/sql/SELECT_from_my_table.sql"
    my_task()

github()