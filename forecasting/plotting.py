import plotly.graph_objs as go
from fbprophet.plot import plot_plotly


def plot_raw_data(df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df["Datetime"], y=df["Energy_kWh"], name="Energy_kWh"))
    fig.layout.update(title_text="Energy Consumption History", xaxis_rangeslider_visible=True)
    return fig


def plot_forecast(model, forecast):
    fig = plot_plotly(model, forecast, xlabel="Datetime", ylabel="Electricity Consumption")
    return fig
