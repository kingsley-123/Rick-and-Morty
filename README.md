# Overview
This project implements an automated ETL (Extract, Transform, Load) pipeline for the Rick and Morty API data using Apache Airflow. The pipeline extracts character, location, and episode data from the Rick and Morty API, transforms it, stores it in PostgreSQL, and visualizes it using Power BI. The entire solution is containerized using Docker for easy deployment and scalability.

# Objectives
1. Extract character, location, and episode data from Rick and Morty AP
2. Data transformation and cleaning
3. Persistent storage in PostgreSQL database
4. Interactive dashboards in Power BI
5. Scheduled data updates
6. Automate the entire process using Apache Airflow
7. Containerized solution with Docker

# Technologies Used
1. Container Platform: Docker
2. Orchestration: Apache Airflow
3. Programming Language: Python 3.x
4. Database: PostgreSQL
5. Visualization: Power BI
6. Version Control: Git
7. API: Rick and Morty REST API

# Project Architechure
![Project Architecture](https://github.com/user-attachments/assets/8debafca-c7d1-45c7-acd1-1b59b7bcfd86)
1. Data Extraction:
   - Use Python scripts to call the Rick and Morty API endpoints for characters, locations, and episodes.
   - Store the raw JSON responses temporarily.

2. Data Transformation:
   - Process the JSON data using Python libraries like pandas.
   - Standardize column names, handle missing data, and remove duplicates.
   - Enrich the data with derived columns, such as episode-to-location mappings.

3. Data Loading:     
   - Design PostgreSQL schemas for characters, locations, and episodes.
   - Load the transformed data into PostgreSQL tables using psycopg2.
     
4. Visualization:
   - Connect Power BI to the PostgreSQL database.
   - Create dashboards with KPIs such as character counts by location, episode timelines, and relationships between characters and locations.

5. Automation:
   - Define an Airflow DAG with tasks for extraction, transformation, and loading.
   - Schedule the pipeline to run daily, ensuring up-to-date data in the database and dashboards.

6. Containerization:
   - Use Docker to containerize all components (Airflow, PostgreSQL, Python scripts).
   - Deploy the solution on any Docker-compatible environment.


# Airflow UI
![Image](https://github.com/user-attachments/assets/aea96383-42cb-4c71-9178-a0eb391e08fa)
The Airflow pipeline consists of the following DAG tasks:
1. Extract Data:
   - Call API endpoints to fetch character, location, and episode data.
   - Save raw data as JSON files in a temporary folder.

2. Transform Data:
   - Read raw JSON files.
   - Clean and process the data using Python (e.g., handle missing fields, standardize formats).

3. Load Data:
   - Insert the processed data into PostgreSQL tables using batch inserts for efficiency.
     
# Database Schema Diagram
![Image](https://github.com/user-attachments/assets/00da0409-65a4-41d1-be31-33687386e23d)

# PowerBI
![Image](https://github.com/user-attachments/assets/7ae33614-311f-46ce-a052-a320333d5457)

# Scheduled Updates
1. Data updates are scheduled daily at 12:00 AM UTC using Airflow.
2. Airflow ensures retries in case of failure, with logs to monitor task execution.

# Deployment
1. Docker Containers:
   - Create separate containers for Airflow, PostgreSQL, and Python scripts.
   - Use docker-compose to orchestrate multi-container deployment.

2. Environment Setup:
   - Define environment variables for database credentials, API endpoints, and Airflow configurations.

3. Git Repository:
   - Store all code, including Airflow DAGs, Python scripts, and Docker configurations, in a version-controlled Git repository.
