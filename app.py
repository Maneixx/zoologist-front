import streamlit as st

"""
# Zoologist front
"""

# st.markdown(
#     """
# Remember that there are several ways to output content into your web page...

# Either like the title above by just creating a string (or an f-string) starting. Or like this paragraph using the `st.` function.
# """
# )

island = st.text_input('Island (the location where the penguin lives: Biscoe, Dream or Torgersen)', key=20)

# st.write('The current movie title is', title)

# bill_length_mm = st.number_input('Bill length (in mm)', key=1)
bill_length_mm= st.slider('Bill length (in mm)', 1, 100, 3)
bill_depth_mm = st.number_input('Bill depth (in mm)', key=2)
flipper_length_mm = st.number_input('Flipper length (in mm)', key=4)
body_mass_g = st.number_input('Body mass (in g)', key=5)
# sex = st.text_input('sex ("Male" or "Female")', key=30)
sex = st.selectbox('sex', ['Male','Female'])


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

    st.write(result["prediction"])
