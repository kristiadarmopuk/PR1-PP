import tkinter as tk
from tkinter import simpledialog

def show_dialog():
    root = tk.Tk()
    root.withdraw()
    user_input = simpledialog.askstring("Введення", "Введіть текст:")
    if user_input is not None:
        print("Ви ввели:", user_input)

show_dialog()