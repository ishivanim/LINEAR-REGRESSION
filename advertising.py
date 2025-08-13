# streamlit_app.py
import streamlit
import joblib
import pandas as pd

b0 = 4.66156328475459
b1 = 16.08295946
b2 = 5.26266769
b3 = 0.15666404

min_values = joblib.load("min_values.pkl")
max_values = joblib.load("max_values.pkl")

streamlit.title("Sales Predictor Based on Advertisement Spend")

tv = streamlit.number_input("TV Ad Spend($)")
radio = streamlit.number_input("Radio Ad Spend($)")
newspaper = streamlit.number_input("Newspaper Ad Spend($)")

user_data = {
    "tv" : tv,
    "radio" : radio,
    "newspaper" :newspaper
}
normalized_user_data = pd.DataFrame([{
    "tv" : (user_data["tv"] - min_values["TV"])/(max_values["TV"] - min_values["TV"]),
    "radio" : (user_data["radio"] - min_values["Radio"])/(max_values["Radio"] - min_values["Radio"]),
    "newspaper" : (user_data["newspaper"] - min_values["Newspaper"])/(max_values["Newspaper"] - min_values["Newspaper"])
}])


if streamlit.button("Predict"):
    sales = b0 + b1 * normalized_user_data["tv"] + b2 * normalized_user_data["radio"] + b3 * normalized_user_data["newspaper"]
    sales = float(sales.iloc[0])
    streamlit.success(f"Sales Revenue in M$: {sales:.2f}")
