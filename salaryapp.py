# -*- coding: utf-8 -*-
"""salaryapp.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tJY1fyR0BO6I_dri_AnrD2TxJR8sLmRQ
"""

# Streamlit App Only (Clean Version)
import pandas as pd
import streamlit as st
import pickle

# Load model and label encoder
model = pickle.load(open('salary_predictor.pkl', 'rb'))
le = pickle.load(open('label_encoder.pkl', 'rb'))

# Title
st.title('Data Scientist Salary Predictor')

# Input fields
country = st.text_input('Enter your Country')
education = st.text_input('Enter your Education Level')
experience = st.text_input('Enter your Years of Experience')
role = st.text_input('Enter your Job Title')

# Predict salary if button clicked
if st.button('Predict Salary'):
    input_data = pd.DataFrame({
        'Q4': [country],
        'Q8': [education],
        'Q11': [experience],
        'Q23': [role]
    })
    for col in input_data.columns:
        input_data[col] = le.fit_transform(input_data[col].astype(str))
    prediction = model.predict(input_data)
    st.success(f'Estimated Salary: ${prediction[0]:,.0f}')