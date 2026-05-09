from tkinter import *
from tkinter import font
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
from tkinter import ttk
import datetime as dt

class tableReserve:
    def __init__(self,root):
        self.root = root
        self.root.attributes('-fullscreen', True)
        self.root.title("Reserve Table")
        self.root.geometry("1800x2000+4+4") 
        self.root.maxsize(1440,1080)
        self.root.minsize(1440,1080)
        
        img1 = Image.open(r"D:\VS Code\DBMS\images\Group 36.png")
        img1=img1.resize((1440,140),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lblimg = Label(self.root,image=self.photoimg1,bd=2,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1440,height=140)
        
        main_frame=Frame(self.root,relief=RIDGE)
        main_frame.place(x=0,y=140,width=1440,height=98)
        
        cust_btn_home=Button (main_frame, text="HOME",width=25,height=4,font=("times new roman", 14,"bold"), bg="black", fg="gold",  cursor="hand1")
        cust_btn_home.grid(row=0,column=0)
        
        cust_btn_home=Button (main_frame, text="ABOUT US",width=25,height=4,font=("times new roman", 14,"bold"), bg="black", fg="gold",  cursor="hand1")
        cust_btn_home.grid(row=0,column=1)

        cust_btn_home=Button (main_frame, text="MENU",width=27,height=4,font=("times new roman",14,"bold"), bg="black", fg="gold",  cursor="hand1")
        cust_btn_home.grid(row=0,column=2)

        cust_btn_home=Button (main_frame, text="CONTACT",width=25,height=4,font=("times new roman", 14,"bold"), bg="black", fg="gold",  cursor="hand1")
        cust_btn_home.grid(row=0,column=3)

        cust_btn_home=Button (main_frame, text="USER",width=25,height=4,font=("times new roman", 14,"bold"), bg="black", fg="gold",  cursor="hand1")
        cust_btn_home.grid(row=0,column=4)
        
        main_home=Frame(self.root,relief=RIDGE,bd=0,bg="#FFE5CA")
        main_home.place(x=0,y=238,width=1440,height=620)
        
        img2 = Image.open(r"D:\VS Code\DBMS\images\Reserve table.png")
        #img1=img1.resize((1440,140),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(self.root,image=self.photoimg2,bd=2,relief=RIDGE)
        lblimg2.place(x=412,y=258,width=615,height=53)
        
        img3 = Image.open(r"D:\VS Code\DBMS\images\Name_.png")
        #img1=img1.resize((1440,140),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(self.root,image=self.photoimg3,bd=2,relief=RIDGE)
        lblimg3.place(x=505,y=325,width=180,height=53)
        global name
        name = Entry(self.root,width = 20,font=('Arial 30'))
        name.place(x=704,y=325)
        
        img4 = Image.open(r"D:\VS Code\DBMS\images\Table No..png")
        #img1=img1.resize((1440,140),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        lblimg4 = Label(self.root,image=self.photoimg4,bd=2,relief=RIDGE)
        lblimg4.place(x=480,y=400,width=220,height=53)
        global Table_No
        Table_No = ttk.Combobox(self.root,font=('Arial 30'),width=10)
        Table_No["value"] =  ("1","2","3","4","5","6","7")
        Table_No.place(x=704,y=400)
        
        img5 = Image.open(r"D:\VS Code\DBMS\images\Date_.png")
        #img1=img1.resize((1440,140),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        lblimg5 = Label(self.root,image=self.photoimg5,bd=2,relief=RIDGE)
        lblimg5.place(x=533,y=485,width=149,height=62)
        # Create an instance of datetime module
        date1 = dt.datetime.now()
        # Format the date
        format_date=f"{date1:%a, %b %d %Y}"
        global date
        date = Entry(self.root,width = 20,font=('Arial 30'))
        date.insert(END,format_date)
        date.place(x=704,y=485)
        
        img6= Image.open(r"D:\VS Code\DBMS\images\Time Slot_.png")
        #img1=img1.resize((1440,140),Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        lblimg6 = Label(self.root,image=self.photoimg6,bd=2,relief=RIDGE)
        lblimg6.place(x=402,y=574,width=288,height=62)
        global time
        time = Entry(self.root,width = 20,font=('Arial 30'))
        time.place(x=704,y=574)
        
        img7 = Image.open(r"D:\VS Code\DBMS\images\Email_.png")
        #img1=img1.resize((1440,140),Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        lblimg7 = Label(self.root,image=self.photoimg7,bd=2,relief=RIDGE)
        lblimg7.place(x=402,y=663,width=288,height=54)
        global email
        email = Entry(self.root,width = 20,font=('Arial 30'))
        email.place(x=704,y=663)
            
        img8 = Image.open(r"D:\VS Code\DBMS\images\Mobile Number _.png")
        #img1=img1.resize((1440,140),Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        lblimg8 = Label(self.root,image=self.photoimg8,bd=2,relief=RIDGE)
        lblimg8.place(x=222,y=745,width=453,height=55)
        global phone_no
        phone_no = Entry(self.root,width = 20,font=('Arial 30'))
        phone_no.place(x=704,y=745)
        
        cust_btn_home = Button(self.root, text="Book a table", width=25, height=1, font=(
        "times new roman", 14, "bold"), bg="black", fg="gold",  cursor="hand1",command=insert)
        
       # cust_btn_home = Button(self.root, text="Book a table", width=25, height=1, font=(
       # "times new roman", 14, "bold"), bg="black", fg="gold",  cursor="hand1",command=destroyWindow)
        cust_btn_home.place(x=600, y=810)


def destroyWindow():
    root.withdraw()
    
#mysql      
conn = mysql.connector.connect(
    user='root',password='pranav@010',host='localhost',database='reservtable')

cursor = conn.cursor()

def insert():
    sql = f"INSERT INTO booking(Name,Table_No,Phone_No,Date,Time,Email) VALUES('{name.get()}','{Table_No.get()}','{phone_no.get()}','{date.get()}','{time.get()}','{email.get()}')"
    
    try:
        #Executing the SQL command
        cursor.execute(sql)

        #Commit your changes in the database
        conn.commit()
        conn.close()
        messagebox.showinfo("Success","Table has been booked successfully.")
        root.withdraw()
        

    except:
        # Rolling back in case of error
        conn.rollback()
        messagebox.showerror("Error","Try another table number or fill all the fields.")
        cursor.execute(sql)
    conn.close()
    

if __name__ == "__main__":
    root = Tk()
    obj = tableReserve(root)
    root.mainloop()
    
