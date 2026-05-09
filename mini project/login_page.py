from tkinter import *
from PIL import Image,ImageTk
from tkinter import Toplevel, Label, Entry, Button,messagebox
from home_page import RestaurantManagementSystem
import mysql.connector

class Login:
    def __init__(self, home_root1):
        self.home_root1 = home_root1
        self.home_root1.title("Login PAGE")
        self.home_root1.geometry("1440x1080+0+0")
        self.home_root1.maxsize(1440, 1080)
        self.home_root1.minsize(1440, 1080)
        self.email_var=StringVar()
        self.mobno_var=StringVar()
        

        # self.btn_login = Button(self.home_root1, text="LOGIN", command=self.login)
        # self.btn_login.pack(pady=20)

        main_home=Frame(self.home_root1,relief=RIDGE,bd=0,bg="#FFE5CA")
        main_home.place(x=0,y=0,width=1440,height=1080)

        img1=Image.open("Group 29.png")
        img1=img1.resize((1440,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg=Label(self.home_root1, image=self.photoimg1)
        lblimg.place(x=0, y=0,width=1440,height=140)

        img2=Image.open("journey.png")
        img2=img2.resize((1440,120),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg=Label(self.home_root1, image=self.photoimg2)
        lblimg.place(x=0, y=140,width=1440,height=120)
        
        img3=Image.open("u_name.png")
        img3=img3.resize((299,60),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        lblimg=Label(self.home_root1, image=self.photoimg3)
        lblimg.place(x=478, y=447,width=299,height=60)
        
        img4=Image.open("pass.png")
        img4=img4.resize((299,60),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        lblimg=Label(self.home_root1, image=self.photoimg4)
        lblimg.place(x=470, y=610,width=299,height=60)
        
        self.username_var = StringVar()
        self.password_var = StringVar()

    
        self.label_username = Label(self.home_root1, text="Username:")
        self.label_username.pack(pady=10)
        self.label_username.place(x=1,y=50)
        self.entry_username = Entry(self.home_root1, font=('Georgia 20'),textvariable=self.username_var)
        self.entry_username.pack()
        self.entry_username.place(x=809,y=436,width=359,height=74)

        self.label_password = Label(self.home_root1, text="Password:")
        self.label_password.pack(pady=10)
        self.entry_password = Entry(self.home_root1, show="*", font=('Georgia 20'),textvariable=self.password_var)
        self.entry_password.pack()
        self.entry_password.place(x=809,y=603,width=359,height=74)

        
        self.label_error = Label(self.home_root1, fg="red")
        self.label_error.pack()

        # self.label_user_role = Label(self.root1, text="User Role:")
        # self.label_user_role.pack(pady=10)
        # self.combobox_user_role = ttk.Combobox(self.root1, values=["user", "admin"])
        # self.combobox_user_role.pack()

        self.btn_signup = Button(self.home_root1, text="Signup", command=self.signup)
        self.btn_signup.pack(pady=20)
        self.btn_signup.place(x=75,y=802,width=398,height=106)

        self.admin_log = Button(self.home_root1, text="Admin Login", command=self.admin_login)
        self.admin_log.pack(pady=20)
        self.admin_log.place(x=546,y=802,width=398,height=106)

        self.user_login = Button(self.home_root1, text="User Login", command=self.User_login)
        self.user_login.pack(pady=20)
        self.user_login.place(x=1017,y=802,width=398,height=106)

    
    
    

    def signup(self):
        # Create a new top-level window for the sign-up dialog
        signup_window = Toplevel(self.home_root1)
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

        # Add a label and entry widget for the confirm password
        email_label = Label(signup_window, text="Email:")
        email_label.grid(row=3, column=0, padx=5, pady=5)
        email_entry = Entry(signup_window, show="*",textvariable=self.email_var)
        email_entry.grid(row=3, column=1, padx=5, pady=5)

        # Add a label and entry widget for the confirm password
        mob_label = Label(signup_window, text="Mobile No.:")
        mob_label.grid(row=4, column=0, padx=5, pady=5)
        mob_entry = Entry(signup_window, show="*",textvariable=self.mobno_var)
        mob_entry.grid(row=4, column=1, padx=5, pady=5)

        # Add a button to submit the sign-up form
        signup_button = Button(signup_window, text="Sign up", command=lambda: self.process_signup(username_entry.get(), password_entry.get(), confirm_entry.get(), signup_window))
        signup_button.grid(row=5, column=1, padx=5, pady=5)

    def process_signup(self, username, password, confirm_password, signup_window):
        if not username or not password:
            messagebox.showerror("Error", "Username and password are required.")
        elif password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match.")
        else:
            conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ak@sh",
    database="mini_project"
)

            my_cursor = conn.cursor()
            my_cursor.execute("INSERT INTO user_data (username, password, email,mobno) VALUES (%s, %s ,%s,%s)", (
                username,
                password,
                self.email_var.get(),
                self.mobno_var.get()
            ))
            conn.commit()
            messagebox.showinfo("Signup", "Signup Successful. Please login with your credentials.")
            signup_window.destroy()
            conn.close()


    def admin_login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        # user_role = self.combobox_user_role.get()
        if username == "admin" and password == "admin":
            self.new_window = Toplevel(self.home_root1)
            self.app = RestaurantManagementSystem(self.new_window)
            self.home_root1.withdraw()
        else:
            messagebox.showerror("Error ","Wrong Admin Credentials")


    def User_login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        # user_role = self.combobox_user_role.get()

        if self.username_var.get() == "" or self.password_var.get() == "":
                messagebox.showerror("Error", "All fields required")
        else:
            conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ak@sh",
    database="mini_project"
)


            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM user_data WHERE username = %s AND password = %s", (
                self.username_var.get(),
                self.password_var.get()
            ))
            row = my_cursor.fetchone()
            if row is not None:
                messagebox.showinfo("Login", "Login Succcesfull")
                self.new_window = Toplevel(self.home_root1)
                self.app = RestaurantManagementSystem(self.new_window)
                self.home_root1.withdraw()

            else:
                messagebox.showerror("Error", "Username and Password not found")
            conn.close()

        # else:
        #     self.label_error.config(text="Invalid username or password")


if __name__=="__main__":
    home_root1=Tk()
    obj=Login(home_root1)
    home_root1.mainloop()




