import streamlit as st
import requests  # importing requests
from streamlit_lottie import st_lottie  # importing package for animation

st.set_page_config(page_title="PredictO", layout="wide")


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# -------------ASSETS-------------
lottie_files = load_lottieurl('https://assets8.lottiefiles.com/packages/lf20_duLkH4dmdC.json')

# -------------Header Section-----------------
st.subheader("WELCOME TO PREDICTO :wave:")
st.title("Your Real Time Healthcare App")
st.write("Revolutionize your healthcare experience with our smart app! Accessible, intuitive, and personalized, "
         "it empowers you to take control of your well-being. From tracking vital signs to scheduling appointments, "
         "our app seamlessly connects you with healthcare professionals and provides tailored recommendations for a "
         "healthier life. Experience the future of healthcare at your fingertips!")

# -------------What do i DO Section-----------------
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Just Another Title")
        st.write("##")  # adds space between title and body
        st.write(
            """
            - (TEXT_1)
                        
            - (TEXT_2)
            
            - (TEXT_3)
            
            - (TEXT_4)
            
            - (TEXT_5)
            
            """)

    with right_column:
        st_lottie(lottie_files, height=400, key="health")


# -------------Taking Inputs Section-----------------

with st.container():
    st.write("---")
    st.header("Let's get you Checked!")
    st.write("##")
    col1, col2, col3 = st.columns((1, 2, 1))
    with col2:
        st.number_input('Age')
        st.number_input('Weight')
        st.number_input('Height')
        st.number_input('Glucose Levels')
        st.radio("Gender", ('Male', 'Female'))
    st.write("---")
