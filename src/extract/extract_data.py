import pandas as pd
from pathlib import Path
from src.utils.logger import get_logger
logger = get_logger(__name__)

def extract_csv(file_path, expected_columns=None):
    path = Path(file_path)
    if not path.exists(): raise FileNotFoundError(f"Not found: {file_path}")
    df = pd.read_csv(file_path)
    logger.info(f"Loaded {len(df):,} rows from {path.name}")
    if expected_columns:
        missing = set(expected_columns) - set(df.columns)
        if missing: raise ValueError(f"Missing columns: {missing}")
    return df

def detect_nulls(df, required_columns):
    for col in required_columns:
        n = df[col].isna().sum()
        if n: logger.warning(f"{n:,} null {col}s — dropping")
        df = df.dropna(subset=[col])
    return df
