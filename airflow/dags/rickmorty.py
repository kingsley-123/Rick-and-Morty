from airflow.providers.http.sensors.http import HttpSensor #type: ignore
from airflow.operators.python import PythonOperator #type: ignore
from datetime import datetime, timedelta
from airflow import DAG
import sys
import os

# Ensure the scripts directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../scripts')))

def import_and_load_episode():
    from loaddata import load_episode_data #type: ignore
    return load_episode_data()

def import_and_load_location():
    from loaddata import load_location_data #type: ignore
    return load_location_data()

def import_and_load_character():
    from loaddata import load_character_data #type: ignore
    return load_character_data()

default_args = {
    "start_date": datetime(2025, 1, 13),
    "retries": 5,
    "retry_delay": timedelta(minutes=10),
}

with DAG(
    dag_id="rickmorty",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
) as dag:

    is_api_available = HttpSensor(
        task_id="is_api_available",
        http_conn_id="api",
        endpoint="api/",
        timeout=20,  # Add timeout to prevent hanging
        poke_interval=5,  # Check every 5 seconds
    )

    load_episode = PythonOperator(
        task_id='load_episode',
        python_callable=import_and_load_episode  # Changed from load_episode_data
    )
    
    load_location = PythonOperator(
        task_id='load_location',
        python_callable=import_and_load_location  # Changed from load_location_data
    )
    
    load_character = PythonOperator(
        task_id='load_character',
        python_callable=import_and_load_character  # Changed from load_character_data
    )

    is_api_available >> load_episode >> load_location >> load_character