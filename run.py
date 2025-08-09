import streamlit as st
from streamlit_option_menu import option_menu
import joblib
import pandas as pd

# Load the model
model = joblib.load('weather_model.pkl')

st.title("Weather Prediction App")
st.markdown(
    """
    <style>
    .reportview-container {
        background: linear-gradient(to top right, #ffcccb, #d1e7dd);
        color: #333;
    }
    </style>
    """,
    unsafe_allow_html=True
)

with st.sidebar:
    selected = option_menu("Menu", ["Home", "Predict"],
        icons=["house", "cloud"], 
        menu_icon="cast", default_index=0)

if selected == "Predict":
    st.header("Predict Weather Conditions")

    precipitation = st.number_input("Precipitation (mm)", min_value=0.0)
    temp_max = st.number_input("Max Temperature (°C)", min_value=-50.0, max_value=50.0)
    temp_min = st.number_input("Min Temperature (°C)", min_value=-50.0, max_value=50.0)
    wind = st.number_input("Wind Speed (km/h)", min_value=0.0)

    if st.button("Predict"):
        
        input_data = pd.DataFrame({
            'precipitation': [precipitation],
            'temp_max': [temp_max],
            'temp_min': [temp_min],
            'wind': [wind]
        })

        
        prediction = model.predict(input_data)

 
        st.success(f"The predicted weather outcome is: {prediction[0]}")
