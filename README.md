# Batch ETL Data Pipeline

![Tests](https://github.com/saiprudhvi-d/batch-etl-data-pipeline/actions/workflows/test.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.11-blue)

Modular batch ETL pipeline: raw → clean → curated with data quality checks and Airflow orchestration.

## Stack
Python · PySpark · Airflow · pandas · SQL

## Structure
```
batch-etl-data-pipeline/
├── .github/workflows/test.yml
├── configs/pipeline_config.yaml
├── dags/batch_pipeline.py
├── src/extract/ transform/ quality/ load/ utils/
├── tests/test_quality_checks.py
└── requirements.txt
```

## Setup
```bash
git clone https://github.com/saiprudhvi-d/batch-etl-data-pipeline
pip install -r requirements.txt
```

## CI/CD
Tests run automatically on every push via GitHub Actions.