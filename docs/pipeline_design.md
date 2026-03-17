# Pipeline Design

## Layers
| Layer | Location | Description |
|-------|----------|-------------|
| Raw | data/raw/ | Unmodified source data |
| Clean | data/clean/ | Validated + type-cast |
| Curated | data/curated/ | Business-ready with derived columns |

## Modules
- **extract/** - Load CSVs, detect nulls and duplicates
- **transform/** - Standardize, add derived columns, filter invalids
- **quality/** - Run assertions, fail pipeline on critical violations
- **load/** - Write Parquet outputs partitioned by date
