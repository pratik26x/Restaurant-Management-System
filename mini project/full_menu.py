from tkinter import *
from PIL import Image,ImageTk
import importlib


class full_Menu_win:
    def __init__(self, root_menu):
        self.root_menu = root_menu
        self.root_menu.title("Restaurant Management System")
        self.root_menu.geometry("1440x1080+0+0")
        self.root_menu.maxsize(1440,1080)
        self.root_menu.minsize(1440,1080)

        img1=Image.open(r"C:\Users\AKASH\.vscode\mini project\Images\full_menu\header .png")
        img1=img1.resize((1440,150),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root_menu, image=self.photoimg1, bd=4)
        lblimg.place(x=0, y=0, width=1440, height=150)

        main_frame=Frame(self.root_menu)
        main_frame.place(x=0,y=150,width=1440,height=98)

        cust_btn_home=Button (main_frame, text="HOME",command=self.home,width=25,height=4,font=("times new roman", 14,"bold"), bg="black", fg="gold",  cursor="hand1")
        cust_btn_home.grid(row=0,column=0)
        cust_btn_home=Button (main_frame, text="ABOUT US",command=self.about_us,width=25,height=4,font=("times new roman", 14,"bold"), bg="black", fg="gold",  cursor="hand1")
        cust_btn_home.grid(row=0,column=1)
        cust_btn_home=Button (main_frame, text="MENU",width=27,height=4,font=("times new roman",14,"bold"), bg="#FFE5CA", fg="black",  cursor="hand1")
        cust_btn_home.grid(row=0,column=2)
        cust_btn_home=Button (main_frame, text="CONTACT",command=self.contact2,width=25,height=4,font=("times new roman", 14,"bold"), bg="black", fg="gold",  cursor="hand1")
        cust_btn_home.grid(row=0,column=3)
        cust_btn_home=Button (main_frame, text="USER",width=25,height=4,font=("times new roman", 14,"bold"), bg="black", fg="gold",  cursor="hand1")
        cust_btn_home.grid(row=0,column=4)

        main_home=Frame(self.root_menu,bd=0,bg="#FFE5CA")
        main_home.place(x=0,y=238,width=1440,height=780)

        full_img_menu=Image.open(r"C:\Users\AKASH\.vscode\mini project\Images\full_menu\full menu.png")
        full_img_menu=full_img_menu.resize((1440,780),Image.ANTIALIAS)
        self.photoimg_full_menu=ImageTk.PhotoImage(full_img_menu)
        full_lblimg=Label(main_home, image=self.photoimg_full_menu, bd=4, relief=RIDGE)
        full_lblimg.place(x=0, y=0, width=1440, height=780)
    
    def home(self):
        from home_page import RestaurantManagementSystem
        self.new_window = Toplevel(self.root_menu)
        self.app = RestaurantManagementSystem(self.new_window)
        self.root_menu.withdraw()

    def contact2(self):
        from contact import contact
        self.new_window = Toplevel(self.root_menu)
        self.app = contact(self.new_window)
        self.home_root.withdraw()

    def about_us(self):
        from about_us import au
        self.new_window = Toplevel(self.root_menu)
        self.app = au(self.new_window)
        self.home_root.withdraw()



if __name__ == "__main__":
    root = Tk()
    obj = full_Menu_win(root)
    root.mainloop()