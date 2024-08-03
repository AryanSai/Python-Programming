import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title("Simple Streamlit App")

# Display text
st.write("Welcome to the Simple Streamlit App!")

# Text input
name = st.text_input("Enter your name:")

# Button
if st.button("Submit"):
    st.write(f"Hello, {name}!")

# Slider input
number = st.slider("Pick a number", 0, 100, 50)

# Display a chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(chart_data)
