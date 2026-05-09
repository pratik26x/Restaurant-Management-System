from tkinter import *
from tkinter import font
from PIL import Image,ImageTk

class contact:
    def __init__(self,home_root):
        self.home_root=home_root
        self.home_root.title("Contact")
        self.home_root.geometry("1440x1080+0+0")
        self.home_root.maxsize(1440,1080)
        self.home_root.minsize(1440,1080)

        img1=Image.open("Group 29.png")
        img1=img1.resize((1440,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg=Label(self.home_root, image=self.photoimg1)
        lblimg.place(x=0, y=0,width=1440,height=140)


        

        main_frame=Frame(self.home_root,relief=RIDGE)
        main_frame.place(x=0,y=140,width=1440,height=98)

        cust_btn_home=Button (main_frame, text="HOME",width=25,height=4,font=("times new roman", 14,"bold"), bg="black", fg="gold",  cursor="hand1")
        cust_btn_home.grid(row=0,column=0)
        
        cust_btn_home=Button (main_frame, text="ABOUT US",width=25,height=4,font=("times new roman", 14,"bold"), bg="black", fg="gold",  cursor="hand1")
        cust_btn_home.grid(row=0,column=1)

        cust_btn_home=Button (main_frame, text="MENU",width=27,height=4,font=("times new roman",14,"bold"), bg="black", fg="gold",  cursor="hand1")
        cust_btn_home.grid(row=0,column=2)

        cust_btn_home=Button (main_frame, text="CONTACT",width=25,height=4,font=("times new roman", 14,"bold"), bg="#FFE5CA", fg="#000000",  cursor="hand1")
        cust_btn_home.grid(row=0,column=3)

        cust_btn_home=Button (main_frame, text="USER",width=25,height=4,font=("times new roman", 14,"bold"), bg="black", fg="gold",  cursor="hand1")
        cust_btn_home.grid(row=0,column=4)

        main_home=Frame(self.home_root,relief=RIDGE,bd=0,bg="#FFE5CA")
        main_home.place(x=0,y=238,width=1440,height=620)
        
        img2=Image.open("g_map.png")
        img2=img2.resize((523,457),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg=Label(self.home_root, image=self.photoimg2,relief=RIDGE)
        lblimg.place(x=152, y=348,width=523,height=457)

        img3=Image.open("details.png")
        img3=img3.resize((702,479),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        lblimg=Label(self.home_root, image=self.photoimg3)
        lblimg.place(x=716, y=348,width=702,height=479)
       
        main_home_last1=Frame(self.home_root,relief=RIDGE,bd=0,bg="#FFE5CA")
        main_home_last1.place(x=0,y=858,width=270,height=620)

        main_home_last2=Frame(self.home_root,relief=RIDGE,bd=0,bg="#FFE5CA")
        main_home_last2.place(x=270,y=858,width=300,height=620)

        #cust_btn_home=Button (main_home_last2, text="ORDER ONLINE",width=25,font=("times new roman", 14,"bold"), bg="black", fg="white",  cursor="hand1")
        #cust_btn_home.grid(row=0,column=4)
        
        main_home_last3=Frame(self.home_root,relief=RIDGE,bd=0,bg="#FFE5CA")
        main_home_last3.place(x=540,y=858,width=360,height=620)

        main_home_last4=Frame(self.home_root,relief=RIDGE,bd=0,bg="#FFE5CA")
        main_home_last4.place(x=900,y=858,width=300,height=620)

        # cust_btn_home=Button (main_home_last4, text="RESERVE THE TABLE",width=25,font=("times new roman", 14,"bold"), bg="black", fg="white",  cursor="hand1")
        # cust_btn_home.grid(row=0,column=4)

        main_home_last5=Frame(self.home_root,relief=RIDGE,bd=0,bg="#FFE5CA")
        main_home_last5.place(x=1170,y=858,width=270,height=620)

        


if __name__=="__main__":
    root=Tk()
    obj=contact(root)
    root.mainloop()