# src/checks.py
import pandas as pd

def check_missing(df):
    """Return count of missing values per column"""
    if df is None:
        return {}
    return df.isnull().sum().to_dict()

def check_duplicates(df):
    """Return number of duplicate rows"""
    if df is None:
        return 0
    return int(df.duplicated().sum())

def check_outliers(df):
    """Detect numeric column outliers using mean ± 3*std"""
    outliers = {}
    if df is None:
        return outliers

    numeric_cols = df.select_dtypes(include='number').columns
    for col in numeric_cols:
        mean = df[col].mean()
        std = df[col].std()
        count = ((df[col] < mean - 3*std) | (df[col] > mean + 3*std)).sum()
        # Main branch modification: multiply count by 2 for demo
        outliers[col] = int(count * 2)
    return outliers


def check_schema(df, expected_columns):
    """Return missing columns compared to expected schema"""
    if df is None:
        return expected_columns
    missing_cols = list(set(expected_columns) - set(df.columns))
    return missing_cols
