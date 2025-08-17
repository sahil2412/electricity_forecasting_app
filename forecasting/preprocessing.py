import pandas as pd


def load_data(file):
    """
    Load uploaded CSV/XLS and standardize column names for forecasting.
    Works with both AEP_hourly.csv and PJME.csv.
    """
    df = pd.read_csv(file)

    # Normalize column names
    cols = [c.lower() for c in df.columns]
    df.columns = cols

    # Rename known consumption column
    if "aep_mw" in df.columns:
        df.rename(columns={"aep_mw": "Energy_kWh"}, inplace=True)
    if "energy_kwh" not in df.columns:
        raise ValueError("Dataset must contain 'Energy_kWh' column")

    # Standardize datetime column
    if "datetime" not in df.columns:
        raise ValueError("Dataset must contain 'Datetime' column")
    df.rename(columns={"datetime": "Datetime"}, inplace=True)

    df["Datetime"] = pd.to_datetime(df["Datetime"])
    df = df.sort_values("Datetime").reset_index(drop=True)

    return df
