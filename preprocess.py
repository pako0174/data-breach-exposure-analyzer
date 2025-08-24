import pandas as pd

def load_logs(filepath):
    """
    Load and preprocess log data from CSV file.
    Adds time-based features for anomaly detection.
    """
    try:
        df = pd.read_csv(filepath)
        if 'event_code' not in df.columns or 'timestamp' not in df.columns:
            raise ValueError("Log file must contain 'event_code' and 'timestamp' columns.")

        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df['hour'] = df['timestamp'].dt.hour
        df['day_of_week'] = df['timestamp'].dt.dayofweek
        df['is_weekend'] = df['day_of_week'].isin([5, 6]).astype(int)

        return df
    except Exception as e:
        print(f"Error loading logs: {e}")
        return None
