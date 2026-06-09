import numpy as np
import pandas as pd

from src.config import ID_COL

# clinically plausible ranges, anything outside is treated as a bad reading
RANGES = {
    "age": (18, 110),
    "bmi": (12, 70),
    "bnp": (0, 5000),
    "sodium": (110, 160),
    "creatinine": (0.1, 15),
    "systolic_bp": (60, 250),
    "heart_rate": (30, 200),
}


def drop_id(df):
    return df.drop(columns=[ID_COL], errors="ignore")


def flag_impossible(df, ranges=RANGES):
    df = df.copy()
    for col, (lo, hi) in ranges.items():
        if col in df.columns:
            df.loc[(df[col] < lo) | (df[col] > hi), col] = np.nan
    return df


def missing_summary(df):
    m = df.isna().sum()
    pct = (m / len(df) * 100).round(2)
    return pd.DataFrame({"missing": m, "pct": pct}).sort_values("pct", ascending=False)
