import pandas as pd
from dataclasses import dataclass, field
from typing import List

@dataclass
class QualityCheck:
    name: str; passed: bool; message: str; rows_affected: int = 0

@dataclass
class QualityReport:
    checks: List[QualityCheck] = field(default_factory=list)
    @property
    def passed(self): return all(c.passed for c in self.checks)
    @property
    def summary(self): return f"{sum(1 for c in self.checks if c.passed)}/{len(self.checks)} passed"

def check_no_nulls(df, columns):
    return [QualityCheck(f"no_nulls_{c}", df[c].isna().sum()==0 if c in df.columns else False,
            f"{df[c].isna().sum()} nulls" if c in df.columns else "not found",
            int(df[c].isna().sum()) if c in df.columns else 0) for c in columns]

def check_unique(df, col):
    n = df.duplicated(subset=[col]).sum() if col in df.columns else -1
    return QualityCheck(f"unique_{col}", n==0, f"{n} dupes" if n>0 else "all unique", int(max(n,0)))

def check_non_negative(df, col):
    n = (df[col]<0).sum() if col in df.columns else -1
    return QualityCheck(f"non_neg_{col}", n==0, f"{n} negatives" if n>0 else "all non-negative", int(max(n,0)))

def check_row_count(df, min_rows):
    return QualityCheck("min_rows", len(df)>=min_rows, f"{len(df):,} rows (min {min_rows:,})")

def run_quality_checks(df, config):
    from src.quality.validate_data import QualityReport, check_row_count, check_unique, check_no_nulls, check_non_negative
    r = QualityReport()
    if mr := config.get("min_row_count"): r.checks.append(check_row_count(df, mr))
    for c in config.get("unique_columns",[]): r.checks.append(check_unique(df, c))
    r.checks.extend(check_no_nulls(df, config.get("required_columns",[])))
    for c in config.get("non_negative_columns",[]): r.checks.append(check_non_negative(df, c))
    return r
