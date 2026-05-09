from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import font

class Cont_Win:
    def __init__(self,home_root):
        self.home_root=home_root
        self.home_root.title("Contact Us")
        self.home_root.geometry("1520x1080+0+0")
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

        cust_btn_home=Button (main_frame, text="CONTACT",width=27,height=4,font=("times new roman", 14,"bold"), bg="#FFE5CA", fg="black",  cursor="hand1")
        cust_btn_home.grid(row=0,column=3)

        cust_btn_home=Button (main_frame, text="USER",width=27,height=4,font=("times new roman", 14,"bold"), bg="black", fg="gold",  cursor="hand1")
        cust_btn_home.grid(row=0,column=4)

        main_home=Frame(self.home_root,relief=RIDGE,bd=0,bg="#FFE5CA")
        main_home.place(x=0,y=238,width=1520,height=620)
        # self.home_root=home_root
        # self.home_root.title("Contact Us")
        # self.home_root.geometry("1520x520+0+270")


        img=Image.open("contact_img.png")
        img=img.resize((1520,520),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        lblimg1=Label(self.home_root, image=self.photoimg)
        lblimg1.place(x=0, y=250,width=1520,height=520)

        #form_btn = Button(text="For more information",font=("times new roman",14 ,"bold"), bg="beige", fg="black",width=1520,height=1)
        #form_btn.place(x=0,y=475)



if __name__ == "__main__":
    home_root=Tk()
    obj = Cont_Win(home_root)
    home_root.mainloop()