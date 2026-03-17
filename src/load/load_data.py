import pandas as pd
from pathlib import Path
from datetime import datetime

def write_curated(df, output_dir):
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    out = Path(output_dir) / f"sales_{datetime.now().strftime('%Y%m%d')}.parquet"
    df.to_parquet(out, index=False)
    return str(out)
