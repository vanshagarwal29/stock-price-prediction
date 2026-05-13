import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Page Configuration
st.set_page_config(
    page_title="Stock Price Prediction",
    page_icon="📈",
    layout="centered"
)

# Load Trained Model
model = joblib.load('stock_model.pkl')

# Sidebar
st.sidebar.title("📊 Stock Prediction App")

st.sidebar.info("""
This application predicts stock closing prices 
using Machine Learning.

Developed using:
- Python
- Scikit-Learn
- Streamlit
""")

# Main Title
st.title("📈 Stock Price Prediction System")

st.markdown("""
Predict stock closing prices using a Machine Learning model trained on historical stock market data.
""")

st.markdown("---")

# User Input Section
st.subheader("📥 Enter Stock Details")

open_price = st.number_input(
    "Open Price",
    min_value=0.0,
    format="%.2f"
)

high_price = st.number_input(
    "High Price",
    min_value=0.0,
    format="%.2f"
)

low_price = st.number_input(
    "Low Price",
    min_value=0.0,
    format="%.2f"
)

volume = st.number_input(
    "Volume",
    min_value=0.0,
    format="%.2f"
)

st.markdown("---")

# Prediction Button
if st.button("🔍 Predict Stock Price"):

    input_data = np.array([
        [open_price, high_price, low_price, volume]
    ])

    prediction = model.predict(input_data)

    st.success("Prediction Generated Successfully!")

    st.markdown(f"""
    ## 📊 Predicted Closing Price

    # 💰 ${prediction[0]:.2f}
    """)

# Optional Dataset Preview
try:
    df = pd.read_csv("stock_data.csv")

    st.markdown("---")

    st.subheader("📁 Dataset Preview")

    st.dataframe(df.head())

    st.subheader("📉 Closing Price Trend")

    st.line_chart(df['Close'])

except:
    st.warning("Dataset file not found. Add stock_data.csv to display charts.")

# Footer
st.markdown("---")

st.markdown(
    "<center>Developed by <b>Vansh Agarwal</b></center>",
    unsafe_allow_html=True
)