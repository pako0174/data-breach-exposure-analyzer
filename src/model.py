from sklearn.ensemble import IsolationForest

def detect_anomalies(df, column, contamination=0.1):
    """
    Detect anomalies using IsolationForest.
    """
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame.")

    model = IsolationForest(contamination=contamination, random_state=42)
    df['anomaly'] = model.fit_predict(df[[column]])
    return df
