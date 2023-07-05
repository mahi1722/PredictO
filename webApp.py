import pandas as pd
import numpy as np
import streamlit as st
import requests
from streamlit_lottie import st_lottie  # importing package for animation
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

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
st.title("Your Real-Time Healthcare App")
with st.container():
    l_column, r_column = st.columns((7, 3))
    with l_column:
        st.write("Revolutionize your healthcare experience with our smart app! "
                 "Accessible, intuitive, and personalized, it empowers you to take control of your well-being. "
                 "From tracking vital signs to scheduling appointments, our app seamlessly connects you with healthcare"
                 " professionals and provides tailored recommendations for a healthier life. "
                 "Experience the future of healthcare at your fingertips!")

# -------------What do I DO Section-----------------
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("How to get yourself Checked?")
        st.write("##")  # adds space between title and body
        st.write(
            """
            - Fill in all the values in their respective blocks.

            - Click on the 'Predict' button.

            - Get to know your results in Real-time.

            """)

    with right_column:
        st_lottie(lottie_files, height=400, key="health")

# -------------Loading dataset-----------------
df = pd.read_csv("diabetesv2.0.csv")

# Assuming your dataset is stored in the 'df' variable
X = df[['BMI', 'Glucose', 'Pregnancies', 'Age']]
y = df['Outcome']

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creating and training the Support Vector Machine model
svm = SVC()
svm.fit(X_train, y_train)

# -------------Taking Inputs Section-----------------

with st.container():
    st.write("---")
    st.header("Let's get you Checked!")
    st.write("##")
    col1, col2, col3 = st.columns((3, 4, 3))
    with col2:
        # Input fields
        bmi = st.number_input("BMI", min_value=0.0, max_value=60.0, value=0.0)
        glucose = st.number_input("Glucose Level", min_value=0, max_value=200, value=0)
        pregnancies = st.number_input("Number of Pregnancies", min_value=0, max_value=10, value=0)
        age = st.number_input("Age", min_value=0, max_value=120, value=0)


        def user_report():
            user_report_data = {
                'BMI': bmi,
                'Glucose': glucose,
                'Pregnancies': pregnancies,
                'Age': age
            }
            report_data = pd.DataFrame(user_report_data, index=[0])
            return report_data


        # Button to predict
        if st.button("Predict"):
            # Get user input and make prediction
            user_data = user_report()
            user_result = svm.predict(user_data)

            # Display the prediction result
            st.write(f"Diabetes Prediction: {user_result}")
