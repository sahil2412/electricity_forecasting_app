# ⚡ Electricity Consumption Forecasting App

This Streamlit application predicts **future electricity usage and costs** using [Facebook Prophet](https://facebook.github.io/prophet/).  
It supports multiple tariff structures and provides interactive visualizations of energy consumption.

---

## 🚀 Features
- Upload your **own electricity dataset** (CSV format).
- Forecast electricity usage for:
  - 1 week  
  - 2 weeks  
  - 1 month  
- Interactive plots (Plotly + Prophet).
- Cost estimation based on tariff type:
  - Domestic (Tariff A)  
  - Commercial (Tariff B)  
  - Industrial (Tariff E1, includes Maximum Demand charges)  
- Download forecast results as CSV.

---

## 📂 Project Structure
electricity_forecasting_app/
│
├── streamlit_app.py # Main Streamlit app
├── requirements.txt # Python dependencies
│
├── forecasting/ # Core forecasting logic
│ ├── init.py
│ ├── preprocessing.py # Load & clean dataset
│ ├── modeling.py # Prophet model training & forecasting
│ ├── billing.py # Tariff and cost calculation
│ └── plotting.py # Plotly visualizations
│
├── data/ # Sample datasets
│ ├── AEP_hourly.csv
│ └── PJME.csv
│
├── assets/ # Images for UI
│ ├── Untitled.png
│ ├── MicrosoftTeams-image.png
│ └── time.png
│
└── README.md


