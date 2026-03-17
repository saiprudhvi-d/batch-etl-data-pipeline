# Batch ETL Data Pipeline

![Tests](https://github.com/saiprudhvi-d/batch-etl-data-pipeline/actions/workflows/test.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Apache Spark](https://img.shields.io/badge/Apache%20Spark-3.5-E25A1C)

## Overview
A modular, production-style batch ETL pipeline that ingests raw retail sales data, applies validation and transformation rules, and produces clean curated datasets for analytics — structured with separate extract, transform, load, and quality modules.

## Business Problem
A retail analytics team receives daily raw data from 5+ source systems. Without a standardized pipeline, analysts spend hours on manual cleaning. This pipeline automates the full raw → clean → curated flow, reducing data preparation time by ~40%.

## Architecture
```
Raw Data (CSV/Parquet)
    → [Extract] → load sources, detect nulls/duplicates
    → [Transform] → standardize, cast types, add derived columns
    → [Quality] → run assertions, fail on violations
    → [Load] → write partitioned Parquet to curated layer
    → [Airflow DAG] → orchestrate and schedule daily
```

## Tech Stack
Python · PySpark · Airflow · pandas · SQL · pytest · GitHub Actions

## Setup
```bash
git clone https://github.com/saiprudhvi-d/batch-etl-data-pipeline
pip install -r requirements.txt
python src/extract/extract_data.py --config configs/pipeline_config.yaml
```

## Future Improvements
- Great Expectations for richer data quality contracts
- Delta Lake for ACID transactions
- dbt models for curated layer
- Slack alerting on quality failures