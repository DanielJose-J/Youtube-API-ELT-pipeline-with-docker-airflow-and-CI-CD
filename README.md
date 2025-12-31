🎥 YouTube ELT Data Pipeline (End-to-End)

🚀 End-to-End Data Engineering Project built to demonstrate real-world ELT architecture, orchestration, data quality, and CI/CD best practices.

📌 Project Overview

This project implements a production-style ELT data pipeline that extracts data from the YouTube Data API, processes it using Python, orchestrates workflows with Apache Airflow, stores data in PostgreSQL, validates data quality with Soda, and automates deployment and testing via GitHub Actions CI/CD.

The pipeline is fully containerized with Docker and includes unit, integration, and end-to-end tests.

🧱 Architecture Overview

Data Flow:

YouTube API → Python → Airflow DAGs → PostgreSQL (Staging → Core) → Soda Checks
                           ↑
                    Docker & CI/CD

🔄 Pipeline Workflow (Airflow DAGs)
1️⃣ produce_json

Extracts video metadata from YouTube API

Handles pagination & API limits

Stores raw data as JSON

2️⃣ update_db

Loads data into staging schema

Transforms data and loads into core schema

Handles inserts, updates, and deletes

3️⃣ data_quality

Runs automated Soda data quality checks

Validates:

Null values

Duplicates

Business rules (likes/comments ≤ views)

🗄 Data Warehouse Design (PostgreSQL)

Schemas:

staging → raw, lightly processed data

core → transformed, analytics-ready data

Key Transformations:

ISO 8601 duration parsing

Video classification (Shorts vs Normal)

🧪 Testing Strategy

✔ Unit Tests – core Python logic
✔ Integration Tests – database & Airflow interactions
✔ End-to-End Tests – full DAG execution via Airflow CLI

All tests run automatically in CI.

⚙️ CI/CD Pipeline (GitHub Actions)

Automated on push / PR / manual trigger:

Build Docker image

Push image to Docker Hub

Spin up full Airflow stack

Run unit, integration & E2E tests

Tear down environment

🐳 Containerization

Docker & Docker Compose

CeleryExecutor for distributed task execution

Redis as message broker

PostgreSQL as metadata & ELT database

Ensures environment consistency across local, CI, and production-like setups.

🔍 Tools & Technologies

Python

Apache Airflow

PostgreSQL

Docker & Docker Compose

GitHub Actions

Soda (Data Quality)

Pytest

Postman (API validation)

DBeaver (Database inspection)

🎯 Key Learnings

Designing modular Airflow DAGs

Handling stateful ELT pipelines

Implementing data quality gates

Debugging containerized Airflow systems

Building production-ready CI/CD pipelines

Managing database schemas and migrations

📸 Screenshots Included

Airflow DAG graph & execution

PostgreSQL schemas and tables

GitHub Actions CI/CD runs

🚀 Final Outcome

A fully automated, production-aligned ELT pipeline demonstrating how modern data platforms are built, tested, and deployed in real-world environments.
