from tkinter import *
from tkinter import font
from PIL import Image
from PIL import ImageTk
from contact import Cont_Win
from user import User_Win

class RestaurantManagementSystem:
    def __init__(self,home_root):
        self.home_root=home_root
        self.home_root.title("RestaurantManagementSystem")
        self.home_root.geometry("1440x1080+0+0")
        self.home_root.maxsize(1520,850)
        self.home_root.minsize(1520,850)
       # self.home_root.minsize(1440,1080)

        img1=Image.open("Group 29.png")
        img1=img1.resize((1520,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg=Label(self.home_root, image=self.photoimg1)
        lblimg.place(x=0, y=0,width=1520,height=140)


        main_frame=Frame(self.home_root,relief=RIDGE)
        main_frame.place(x=0,y=140,width=1520,height=98)

        cust_btn_home=Button (main_frame, text="HOME",width=27,height=4,font=("times new roman", 14,"bold"), bg="black", fg="gold",  cursor="hand1")
        cust_btn_home.grid(row=0,column=0)
        
        cust_btn_home=Button (main_frame, text="ABOUT US",width=27,height=4,font=("times new roman", 14,"bold"), bg="black", fg="gold",  cursor="hand1")
        cust_btn_home.grid(row=0,column=1)

        cust_btn_home=Button (main_frame, text="MENU",width=27,height=4,font=("times new roman",14,"bold"), bg="black", fg="gold",  cursor="hand1")
        cust_btn_home.grid(row=0,column=2)

        cust_btn_home=Button (main_frame, text="CONTACT",command=self.cont_win,width=27,height=4,font=("times new roman", 14,"bold"), bg="black", fg="gold",  cursor="hand1")
        cust_btn_home.grid(row=0,column=3)

        cust_btn_home=Button (main_frame, text="USER",command=self.user_win,width=27,height=4,font=("times new roman", 14,"bold"), bg="black", fg="gold",  cursor="hand1")
        cust_btn_home.grid(row=0,column=4)

        main_home=Frame(self.home_root,relief=RIDGE,bd=0,bg="#FFE5CA")
        main_home.place(x=0,y=238,width=1520,height=620)
        
        img2=Image.open("LOGO.png")
        img2=img2.resize((1183,520),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg=Label(self.home_root, image=self.photoimg2,relief=RIDGE)
        lblimg.place(x=150, y=250,width=1183,height=520)

        main_home_last1=Frame(self.home_root,relief=RIDGE,bd=0,bg="#FFE5CA")
        main_home_last1.place(x=0,y=858,width=270,height=620)

        main_home_last2=Frame(self.home_root,relief=RIDGE,bd=0,bg="#FFE5CA")
        main_home_last2.place(x=270,y=858,width=300,height=620)

        cust_btn_home=Button (main_home_last2, text="ORDER ONLINE",width=25,font=("times new roman", 14,"bold"), bg="black", fg="white",  cursor="hand1")
        cust_btn_home.grid(row=0,column=4)
        
        main_home_last3=Frame(self.home_root,relief=RIDGE,bd=0,bg="#FFE5CA")
        main_home_last3.place(x=540,y=858,width=360,height=620)

        main_home_last4=Frame(self.home_root,relief=RIDGE,bd=0,bg="#FFE5CA")
        main_home_last4.place(x=900,y=858,width=300,height=620)

        cust_btn_home=Button (main_home_last4, text="RESERVE THE TABLE",width=25,font=("times new roman", 14,"bold"), bg="black", fg="white",  cursor="hand1")
        cust_btn_home.grid(row=0,column=4)

        main_home_last5=Frame(self.home_root,relief=RIDGE,bd=0,bg="#FFE5CA")
        main_home_last5.place(x=1170,y=858,width=270,height=620)

    def cont_win(self):
        self.new_window=Toplevel(self.home_root)
        self.app=Cont_Win(self.new_window)


    def user_win(self):
        self.new_window1=Toplevel(self.home_root)
        self.app1=User_Win(self.new_window1)



if __name__=="__main__":
    root=Tk()
    obj=RestaurantManagementSystem(root)
    root.mainloop()
