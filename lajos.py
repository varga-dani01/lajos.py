# lajos.py
# import module
import streamlit as st
 
# Title
st.title("Hello GeeksForGeeks !!!")

from tkinter import *

def evaluate_expression(expression):
    try:
        result = str(eval(expression))
        entry_var.set(result)
    except Exception as e:
        entry_var.set("Hiba")

def button_click(symbol):
    current_text = entry_var.get()
    entry_var.set(current_text + str(symbol))

def clear_entry():
    entry_var.set("")
