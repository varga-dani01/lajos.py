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


calculator = Tk()
calculator.title("Számológép")


entry_var = StringVar()
entry = Entry(calculator, textvariable=entry_var, font=("Arial", 18), bd=10, insertwidth=4, width=14, justify="right")
entry.grid(row=0, column=0, columnspan=4)


buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, col) in buttons:
    button = Button(calculator, text=text, font=("Arial", 14), padx=20, pady=20, command=lambda t=text: button_click(t))
    button.grid(row=row, column=col)

clear_button = Button(calculator, text="C", font=("Arial", 14), padx=20, pady=20, command=clear_entry)
clear_button.grid(row=5, column=0, columnspan=3)

# Fő ciklus indítása
calculator.mainloop()
