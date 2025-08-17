from prophet import Prophet
import pandas as pd


def train_and_forecast(df, periods=31, freq="D"):
    """
    Train a Prophet model and return forecast.
    df: DataFrame with columns ['Datetime', 'Energy_kWh']
    """
    data = df.rename(columns={"Datetime": "ds", "Energy_kWh": "y"})
    model = Prophet()
    model.fit(data)

    future = model.make_future_dataframe(periods=periods, freq=freq)
    forecast = model.predict(future)

    return model, forecast
