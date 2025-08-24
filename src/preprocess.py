import pandas as pd

def load_logs(filepath):
    """
    Load and preprocess log data from CSV file.
    """
    try:
        df = pd.read_csv(filepath)
        if 'event_code' not in df.columns:
            raise ValueError("Log file must contain an 'event_code' column.")
        return df
    except Exception as e:
        print(f"Error loading logs: {e}")
        return None
