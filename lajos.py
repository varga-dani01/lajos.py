# lajos.py
# import module
import streamlit as st
 
# Title
st.title("Hello GeeksForGeeks !!!")


import streamlit as st

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Hiba: osztás 0-val"

def calculate(selected_operation, num1, num2):
    if selected_operation == "Összeadás":
        result = add(num1, num2)
    elif selected_operation == "Kivonás":
        result = subtract(num1, num2)
    elif selected_operation == "Szorzás":
        result = multiply(num1, num2)
    elif selected_operation == "Osztás":
        result = divide(num1, num2)
    else:
        result = "Érvénytelen művelet!"
    return result

st.title("Extreme Streamlit Számológép")

selected_operation = st.selectbox("Válassz műveletet", ("Összeadás", "Kivonás", "Szorzás", "Osztás"))

num1 = st.number_input("Adj meg egy számot", step=1.0)
num2 = st.number_input("Adj meg még egy számot", step=1.0)

result = calculate(selected_operation, num1, num2)
st.success(f"Eredmény: {result}")

st.info("Ez egy interaktív Streamlit számológép példa.")

