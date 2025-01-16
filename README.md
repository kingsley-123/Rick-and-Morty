# Overview
This project implements an automated ETL (Extract, Transform, Load) pipeline for the Rick and Morty API data using Apache Airflow. The pipeline extracts character, location, and episode data from the Rick and Morty API, transforms it, stores it in PostgreSQL, and visualizes it using Power BI. The entire solution is containerized using Docker for easy deployment and scalability.

# Features
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

# Pipeline Components
1. Data Extraction (fetchdata.py)
   a) Connects to the Rick and Morty API
   b) Extracts data about characters, locations, and episodes
   c) Handles API pagination and rate limiting
   d) Performs initial data transformation and cleaning

2. Data Loading (loaddata.py)
   a) Manages database connections
   b) Creates necessary database schema
   c) Loads transformed data into PostgreSQL
   d) Handles data updates and integrity

3. Airflow DAG (rickmorty.py)
   a) Orchestrates the ETL workflow
   b) Schedules regular data updates
   c) Monitors pipeline execution
   d) Handles error reporting and retries
