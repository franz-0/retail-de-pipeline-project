\# DummyJSON Retail Data Engineering Pipeline

A production-style Data Engineering project that extracts retail product data from the DummyJSON REST API, transforms it using Pandas, and loads it into MySQL.

The project is designed to demonstrate the complete lifecycle of building a modern ETL pipeline while gradually incorporating software engineering and Data Engineering best practices.

\---

\## Features

\- REST API Extraction

\- Data Cleaning \& Transformation

\- MySQL Loading

\- Modular ETL Architecture

\- Environment Variable Configuration

\- Structured Logging

\- Incremental Loading

\- Snapshot Comparison

\- Error Handling

\- Retry Logic

Upcoming Features

\- Data Warehouse

\- Docker

\- Apache Airflow

\- Data Validation

\- Automated Testing

\- GitHub Actions CI/CD

\- Power BI Dashboard

\- Cloud Deployment

\---

\## Tech Stack

\- Python

\- Pandas

\- Requests

\- SQLAlchemy

\- PyMySQL

\- MySQL

\- dotenv

\- Logging

\- Git

\- GitHub

Future

\- Docker

\- Apache Airflow

\- Power BI

\- AWS / Azure / GCP

\---

\## Project Structure

```text

dummyjson-pipeline/



extract/

transform/

load/

incremental/

utils/

config/

tests/

logs/

snapshots/



pipeline.py

```

\---

\## ETL Workflow

```text

DummyJSON API

│

▼

Extract

│

▼

Transform

│

▼

Incremental Detection

│

▼

Load into MySQL

│

▼

Logging

```

\---

\## Installation

Clone the repository.

```bash

git clone https://github.com/yourusername/dummyjson-pipeline.git

```

Create a virtual environment.

```bash

python -m venv .venv

```

Activate it.

Windows

```bash

.venv\\Scripts\\activate

```

Linux / macOS

```bash

source .venv/bin/activate

```

Install dependencies.

```bash

pip install -r requirements.txt

```

\---

\## Environment Variables

Create a `.env` file.

```env

DB\_HOST=localhost

DB\_PORT=3306

DB\_NAME=dummyjson

DB\_USER=root

DB\_PASSWORD=yourpassword



API\_URL=https://dummyjson.com/products

```

\---

\## Run

```bash

python pipeline.py

```

\---

\## Learning Objectives

This repository demonstrates practical experience with:

\- REST APIs

\- JSON Processing

\- Pandas Data Transformation

\- SQL

\- MySQL

\- ETL Pipelines

\- Logging

\- Incremental Loading

\- Software Engineering Best Practices

\- Version Control with Git

\- Data Warehouse Design

\- Docker

\- Apache Airflow

\- CI/CD

\- Cloud Data Engineering

\---

\## Roadmap

\- ✅ Python ETL

\- ✅ Modular Project Structure

\- ✅ Logging

\- ✅ Environment Variables

\- 🚧 Incremental Loading

\- ⏳ Data Warehouse

\- ⏳ Docker

\- ⏳ Apache Airflow

\- ⏳ Data Validation

\- ⏳ Automated Testing

\- ⏳ GitHub Actions

\- ⏳ Dashboard

\- ⏳ Cloud Deployment

\---

\## Author

Built as part of my journey from IT Operations into Data Engineering, focusing on production-ready ETL pipelines and modern data engineering practices.
