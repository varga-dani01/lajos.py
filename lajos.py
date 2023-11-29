# lajos.py
# import module
import streamlit as st
 
# Title
st.title("Hello GeeksForGeeks !!!")

import streamlit as st

st.title("Streamlit Számológép")

num1 = st.number_input("Adj meg egy számot", step=1.0)
operator = st.selectbox("Válassz műveletet", ('+', '-', '*', '/'))
num2 = st.number_input("Adj meg még egy számot", step=1.0)

if st.button("Számol"):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Hiba: osztás 0-val"
    else:
        result = "Érvénytelen művelet!"

    st.success(f"Eredmény: {result}")

