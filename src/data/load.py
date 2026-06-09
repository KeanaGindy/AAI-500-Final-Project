import pandas as pd

from src.config import RAW_DIR, RAW_FILE


def load_raw(filename=RAW_FILE):
    return pd.read_csv(RAW_DIR / filename)
