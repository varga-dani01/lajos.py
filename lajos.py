# lajos.py
# import module
import streamlit as st
 
# Title
st.title("Hello GeeksForGeeks !!!")

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

while True:
    # Felhasználótól input bekérése
    num1 = float(input("Adj meg egy számot: "))
    operator = input("Válassz műveletet (+, -, *, /): ")
    num2 = float(input("Adj meg még egy számot: "))

    # Művelet végrehajtása és eredmény kiírása
    if operator in ('+', '-', '*', '/'):
        result = None
        if operator == '+':
            result = add(num1, num2)
        elif operator == '-':
            result = subtract(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)
        print(f"Eredmény: {result}")
    else:
        print("Érvénytelen művelet!")

    # Új számológép használata vagy kilépés
    another_calculation = input("Szeretnél új számolást végezni? (igen/nem): ")
    if another_calculation.lower() != 'igen':
        break

    print(f"Eredmény: {result}")

    another_calculation = input("Szeretnél új számolást végezni? (igen/nem): ")
    if another_calculation.lower() != 'igen':
        break

