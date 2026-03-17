# Pipeline Design

## Layers
| Layer | Location | Description |
|-------|----------|-------------|
| Raw | data/raw/ | Unmodified source data |
| Clean | data/clean/ | Validated + type-cast |
| Curated | data/curated/ | Business-ready + derived columns |

## Modules
- **extract/** - Load CSVs, detect nulls and duplicates
- **transform/** - Standardize, cast types, add derived columns
- **quality/** - Run assertions, fail on critical violations
- **load/** - Write outputs partitioned by date
