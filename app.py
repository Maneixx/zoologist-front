import streamlit as st

"""
# Zoologist front
"""

st.image("https://wagon-public-datasets.s3.amazonaws.com/05-Machine-Learning/01-Fundamentals-of-Machine-Learning/palmer-penguins.png")

island = st.selectbox('Island', ['Biscoe', 'Dream','Torgersen'])


bill_length_mm= st.slider('Bill length (in mm)', 1, 100, 3)
bill_depth_mm = st.slider('Bill depth (in mm)',  1, 100, 3)
flipper_length_mm = st.slider('Flipper length (in mm)', 1, 300, 3)
body_mass_g = st.slider('Body mass (in g)', 1, 3000, 3)
sex = st.selectbox('Sex', ['Male','Female'])

url = "http://localhost:8899/predict"

if st.button("Predict") :
    API_params = dict(
                island=island,
                bill_length_mm=bill_length_mm,
                bill_depth_mm=bill_depth_mm,
                flipper_length_mm=flipper_length_mm,
                body_mass_g=body_mass_g,
                sex=sex
        )

    import requests
    response = requests.get(url, params=API_params, timeout=10)
    result = response.json()

    st.write(f"The puiguin specie is {result["prediction"]}")
