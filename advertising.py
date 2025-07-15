# streamlit_app.py
import streamlit

b0 = 0.12064022011716315
b1 = 0.63313218
b2 = 0.20728455
b3 = 0.00572282

streamlit.title("Sales Predictor Based on Advertisement Spend")

tv = streamlit.number_input("TV Ad Spend")
radio = streamlit.number_input("Radio Ad Spend")
newspaper = streamlit.number_input("Newspaper Ad Spend")

if streamlit.button("Predict"):
    sales = b0 + b1 * tv + b2 * radio + b3 * newspaper
    streamlit.success(f"Predicted Sales: {sales:.2f}")
