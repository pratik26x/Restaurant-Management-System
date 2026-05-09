from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
#from Ticket_zoo import ZoomanagementSystem
#from Ticket_zoo3 import Ticket_page
import mysql.connector
from tkinter import Toplevel, Label, Entry, Button, messagebox


class Login_Page:
    def _init__(self, root1):
        self.username_var = StringVar()
        self.password_var = StringVar()

        self.root1 = root1
        self.root1.title("Ticket Booking")
        self.root1.geometry("1550x800+0+0")
        self.root1.configure(bg="#F3DEBA", relief=FLAT)

        self.label_username = Label(self.root1, text="Username:")
        self.label_username.pack(pady=10)
        self.entry_username = Entry(self.root1, textvariable=self.username_var)
        self.entry_username.pack()

        self.label_password = Label(self.root1, text="Password:")
        self.label_password.pack(pady=10)
        self.entry_password = Entry(self.root1, show="*", textvariable=self.password_var)
        self.entry_password.pack()

        
        self.label_error = Label(self.root1, fg="red")
        self.label_error.pack()

        # self.label_user_role = Label(self.root1, text="User Role:")
        # self.label_user_role.pack(pady=10)
        # self.combobox_user_role = ttk.Combobox(self.root1, values=["user", "admin"])
        # self.combobox_user_role.pack()

        self.btn_signup = Button(self.root1, text="Signup", command=self.signup)
        self.btn_signup.pack(pady=20)

        self.admin_log = Button(self.root1, text="Admin Login", command=self.admin_login)
        self.admin_log.pack(pady=20)

        self.user_login = Button(self.root1, text="User Login", command=self.User_login)
        self.user_login.pack(pady=20)

    
    
    

    def signup(self):
        # Create a new top-level window for the sign-up dialog
        signup_window = Toplevel(self.root1)
        signup_window.title("Sign up")

        # Add a label and entry widget for the username
        username_label = Label(signup_window, text="Username:")
        username_label.grid(row=0, column=0, padx=5, pady=5)
        username_entry = Entry(signup_window)
        username_entry.grid(row=0, column=1, padx=5, pady=5)

        # Add a label and entry widget for the password
        password_label = Label(signup_window, text="Password:")
        password_label.grid(row=1, column=0, padx=5, pady=5)
        password_entry = Entry(signup_window, show="*")
        password_entry.grid(row=1, column=1, padx=5, pady=5)

        # Add a label and entry widget for the confirm password
        confirm_label = Label(signup_window, text="Confirm Password:")
        confirm_label.grid(row=2, column=0, padx=5, pady=5)
        confirm_entry = Entry(signup_window, show="*")
        confirm_entry.grid(row=2, column=1, padx=5, pady=5)

        # Add a button to submit the sign-up form
        signup_button = Button(signup_window, text="Sign up", command=lambda: self.process_signup(username_entry.get(), password_entry.get(), confirm_entry.get(), signup_window))
        signup_button.grid(row=3, column=1, padx=5, pady=5)

    def process_signup(self, username, password, confirm_password, signup_window):
        if not username or not password:
            messagebox.showerror("Error", "Username and password are required.")
        elif password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match.")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="9206", database="zoo")
            my_cursor = conn.cursor()
            my_cursor.execute("INSERT INTO user_data (username, password) VALUES (%s, %s)", (
                username,
                password
            ))
            conn.commit()
            messagebox.showinfo("Signup", "Signup Successful. Please login with your credentials.")
            signup_window.destroy()
            conn.close()


    def admin_login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        # user_role = self.combobox_user_role.get()
        if username == "admin" and password == "password":
            self.new_window = Toplevel(self.root1)
            self.app = ZoomanagementSystem(self.new_window)
            self.root1.withdraw()
        else:
            messagebox.showerror("Error ","Wrong Admin Credentials")


    def User_login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        # user_role = self.combobox_user_role.get()

        if self.username_var.get() == "" or self.password_var.get() == "":
                messagebox.showerror("Error", "All fields required")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="9206", database="zoo")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM user_data WHERE username = %s AND password = %s", (
                self.username_var.get(),
                self.password_var.get()
            ))
            row = my_cursor.fetchone()
            if row is not None:
                messagebox.showinfo("Login", "Login Succcesfull")
                self.new_window = Toplevel(self.root1)
                self.app = Ticket_page(self.new_window)
                self.root1.withdraw()

            else:
                messagebox.showerror("Error", "Username and Password not found")
            conn.close()

        # else:
        #     self.label_error.config(text="Invalid username or password")


if __name__ == "_main_":
    root1 = Tk()
    obj = Login_Page(root1)
    root1.mainloop()