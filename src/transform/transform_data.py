import pandas as pd, re
from src.utils.logger import get_logger
logger = get_logger(__name__)

def standardize_column_names(df):
    def snake(n): return re.sub(r'([a-z])([A-Z])',r'\1_\2',re.sub(r'[\s\-]+','_',n.strip())).lower()
    df.columns = [snake(c) for c in df.columns]
    return df

def add_derived_columns(df):
    if 'order_date' in df.columns:
        df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
        df['order_year'] = df['order_date'].dt.year
        df['order_month'] = df['order_date'].dt.month
        df['order_quarter'] = df['order_date'].dt.quarter
    if 'revenue' in df.columns and 'cost' in df.columns:
        df['gross_profit'] = df['revenue'] - df['cost']
        df['gross_margin_pct'] = (df['gross_profit'] / df['revenue'].replace(0,pd.NA)*100).round(2)
    return df

def filter_invalid_records(df):
    if 'revenue' in df.columns: df = df[df['revenue'] >= 0]
    if 'quantity' in df.columns: df = df[df['quantity'] > 0]
    return df.reset_index(drop=True)

def transform(df, type_map=None):
    df = standardize_column_names(df)
    df = add_derived_columns(df)
    return filter_invalid_records(df)
