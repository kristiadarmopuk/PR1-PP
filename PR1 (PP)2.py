import tkinter as tk
from tkinter import messagebox

def register():
    username = entry_username.get()
    password = entry_password.get()
    messagebox.showinfo("Реєстрація", f"Користувач {username} зареєстрований!")

root = tk.Tk()
root.title("Форма реєстрації")

tk.Label(root, text="Ім'я користувача:").pack()
entry_username = tk.Entry(root)
entry_username.pack()

tk.Label(root, text="Пароль:").pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

tk.Button(root, text="Зареєструватися", command=register).pack()

root.mainloop()