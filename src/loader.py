# src/loader.py
import os
import pandas as pd

def load_data(file_path=None):
    """
    Load CSV file into a pandas DataFrame.
    If file_path is None, it uses the default clean_dataset.csv in data folder.
    """
    if file_path is None:
        # Path relative to this script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, "../data/clean_dataset.csv")

    try:
        df = pd.read_csv(file_path)
        print(f"Loaded data with {df.shape[0]} rows and {df.shape[1]} columns.")
        return df
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

if __name__ == "__main__":
    df = load_data()
