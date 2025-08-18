import streamlit as st
import pandas as pd
import base64

from forecasting.preprocessing import load_data
from forecasting.modeling import train_and_forecast
from forecasting.plotting import plot_raw_data, plot_forecast
from forecasting.billing import calculate_cost

st.set_page_config(page_title="Electricity Consumption Forecasting ⚡", layout="wide")

st.title("⚡ Electricity Usage Prediction App")
st.write("Upload your dataset and forecast future electricity consumption with cost estimates.")

# Sidebar
with st.sidebar:
    st.header("About")
    st.write("This app predicts electricity usage and costs using Prophet.")
    st.markdown("**Steps:**\n1. Upload dataset\n2. Select tariff\n3. Run forecast")

# Upload data
uploaded_file = st.file_uploader("Upload CSV dataset", type=["csv"])

if uploaded_file:
    try:
        df = load_data(uploaded_file)
        # Standardize column names so downstream code works
        if "PJME_MW" in df.columns:
            df = df.rename(columns={"PJME_MW": "Energy_kWh"})
        elif "AEP_MW" in df.columns:
            df = df.rename(columns={"AEP_MW": "Energy_kWh"})
        elif df.shape[1] >= 2:
            df = df.rename(columns={df.columns[1]: "Energy_kWh"})
         # fallback: rename 2nd column
        st.subheader("Data Preview")
        st.write(df.head())

        st.plotly_chart(plot_raw_data(df))

        # Tariff selection
        tariff = st.selectbox(
            "Select Tariff",
            ["Tariff A – Domestic", "Tariff B – Commercial", "Tariff E1 – Industrial"],
        )
        option = ["Tariff A – Domestic", "Tariff B – Commercial", "Tariff E1 – Industrial"].index(tariff)

        # Forecasting period
        period = st.selectbox("Forecast period", ["1 week", "2 weeks", "1 month"])
        if period == "1 week":
            periods, freq = 7 * 24, "H"
        elif period == "2 weeks":
            periods, freq = 14 * 24, "H"
        else:
            periods, freq = 31, "D"

        if st.button("Run Forecast"):
            with st.spinner("Training Prophet model..."):
                model, forecast = train_and_forecast(df, periods, freq)

            st.success("Forecast complete ✅")
            st.subheader("Forecast Results")
            st.plotly_chart(plot_forecast(model, forecast))

            # Cost estimation
            future = forecast[["ds", "yhat"]].tail(periods)
            future = future.rename(columns={"ds": "Datetime", "yhat": "Energy_kWh"})
            cost, tcost, tsum, details = calculate_cost(future, option)

            st.subheader("💰 Cost Estimation")
            if option in [0, 1]:
                st.write(f"Estimated cost: $ {cost:.2f}")
            else:
                st.write(f"Estimated cost (including max demand): $ {tcost:.2f}")

            st.write("**Bill Breakdown:**")
            st.table(details["blocks"])

            # Download forecast data
            csv = future.to_csv(index=False)
            b64 = base64.b64encode(csv.encode()).decode()
            st.markdown(f'<a href="data:file/csv;base64,{b64}" download="forecast.csv">Download Forecast CSV</a>', unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Error loading data: {e}")
