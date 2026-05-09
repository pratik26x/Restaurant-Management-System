from tkinter import *
from tkinter import font
from PIL import Image, ImageTk


class RestaurantManagementSystem:
    def __init__(self, home_root):
        self.home_root = home_root
        self.home_root.title("RestaurantManagementSystem")
        self.home_root.geometry("1440x1080+0+0")
        self.home_root.maxsize(1440, 1080)
        self.home_root.minsize(1440, 1080)

        img1 = Image.open("Group 29.png")
        img1 = img1.resize((1440, 150))
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lblimg = Label(self.home_root, image=self.photoimg1)
        lblimg.place(x=0, y=0, width=1440, height=150)

        main_frame = Frame(self.home_root, relief=RIDGE,background="#FFE5CA")
        main_frame.place(x=0, y=140, width=1440, height=1080)

        cust_btn_home = Button(main_frame, text="HOME", width=25, height=4, font=("times new roman", 14, "bold"),
                               bg="black", fg="gold", cursor="hand1")
        cust_btn_home.grid(row=0, column=0)

        cust_btn_home = Button(main_frame, text="ABOUT US", width=25, height=4, font=("times new roman", 14, "bold"),
                               bg="#FFE5CA", fg="black", cursor="hand1")
        cust_btn_home.grid(row=0, column=1)

        cust_btn_home = Button(main_frame, text="MENU", width=27, height=4, font=("times new roman", 14, "bold"),
                               bg="black", fg="gold", cursor="hand1")
        cust_btn_home.grid(row=0, column=2)

        cust_btn_home = Button(main_frame, text="CONTACT", width=25, height=4,
                               font=("times new roman", 14, "bold"), bg="black", fg="gold", cursor="hand1")
        cust_btn_home.grid(row=0, column=3)

        cust_btn_home = Button(main_frame, text="USER", width=25, height=4, font=("times new roman", 14, "bold"),
                               bg="black", fg="gold", cursor="hand1")
        cust_btn_home.grid(row=0, column=4)

        Label(root, image=au).place(x=0,y=248)



if __name__ == "__main__":
    root = Tk()
    au = PhotoImage(file="au.png")
    obj = RestaurantManagementSystem(root)
    root.mainloop()