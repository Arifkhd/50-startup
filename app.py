# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 16:32:02 2024

@author: Dell
"""

import pickle
import streamlit as st
import joblib
from sklearn.linear_model import LinearRegression

st.title('Profit Prediction of StartUp Companys:')

model = joblib.load('startup.pkl')

def predict(Spend,Administration,Marketing_Spend,State):
    prediction = model.predict([[Spend,Administration,Marketing_Spend,State]])
    return prediction[0]

def main():
    st.markdown('This is a simple web app for predicting spend of company :chart:')
    
    # Input fields with validation
    spend = st.number_input('Enter Spend Amount ($)', min_value=0, max_value=1_000_000_000, value=0)
    administration = st.number_input('Enter Administration Cost ($)', min_value=0, max_value=1_000_000, value=0)
    marketing_spend = st.number_input('Enter Marketing Spend ($)', min_value=0, max_value=1_000_000, value=0)
    state = st.selectbox('Select State', ('New York', 'California', 'Florida'))
    
    # Validation for required inputs
    if st.button('Predict'):
        if spend == 0 or administration == 0 or marketing_spend == 0:
            st.error("Please fill out all fields.")
        else:
            # Call the predict function and display the result
            result = predict(spend, administration, marketing_spend, state)
            st.success(f'The predicted profit of the company is: ${result:,.0f}')
                          
if __name__ == '__main__':
    main()