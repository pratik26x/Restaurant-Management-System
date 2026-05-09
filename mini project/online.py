from tkinter import *
from tkinter.ttk import *
from tkinter import font
import mysql.connector
from home_page import RestaurantManagementSystem
from contact import contact
from PIL import Image, ImageTk



class res:
    def __init__(self,window):

        window.resizable(width=TRUE, height=TRUE)
        window.geometry("1440x1080")
        window.configure(background='#FFF3E2')
        window.title("Order Online")

        

        canvas = Canvas(window, bg="#FFF3E2", width=1440, height=1000)
        canvas.pack()

        Label(image=logo).place(x=0, y=-20)

        b1 = Button(window, text="OK", command=lambda: [insert(), connadd()])
        b1.place(x=700, y=750)



        Label(image=fullmenu).place(x=600, y=150)


        bhome = Button(window, text="BACK",width=10, command=lambda : [home1()])
        bhome.place(x=600,y=750)

        my_var1 = IntVar(window)
        my_var1.set(0)
        my_var2 = IntVar(window)
        my_var2.set(0)
        my_var3 = IntVar(window)
        my_var3.set(0)
        my_var4 = IntVar(window)
        my_var4.set(0)
        my_var5 = IntVar(window)
        my_var5.set(0)
        my_var6 = IntVar(window)
        my_var6.set(0)
        my_var7 = IntVar(window)
        my_var7.set(0)
        my_var8 = IntVar(window)
        my_var8.set(0)

        labels = Label(window, text="Shreekhand:\nRs.50/Serve", font=('calibre', 10, 'bold'))
        labels.place(x=0, y=420)
        Shreekhand = Spinbox(window, from_=0, to=10, textvariable=my_var1)
        Shreekhand.place(x=100, y=420)

        img1=Image.open("shrikhand.png")
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg=Label(window, image=self.photoimg1)
        lblimg.place(x=50, y=200)
        # ShreeImg = PhotoImage(file=r"C:\Users\AKASH\.vscode\mini project\shrikhand.png")
        # canvas.create_image(140, 320, image=ShreeImg)



        labels = Label(window, text="Alur Dom:\nRs.150", font=('calibre', 10, 'bold'))
        labels.place(x=400, y=420)
        Alur_Dom = Spinbox(window, from_=0, to=10, textvariable=my_var2)
        Alur_Dom.place(x=80 + 400, y=420)
        img2=Image.open("alurdom.png")
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg=Label(window, image=self.photoimg2)
        lblimg.place(x=350, y=200)
        
        # ADImg = PhotoImage(file=r"C:\Users\AKASH\.vscode\mini project\DBMS PBL(Order Online)\alurdom.png")
        # canvas.create_image(500, 320, image=ADImg)

        labels = Label(window, text="Thepla:\nRs.70", font=('calibre', 10, 'bold'))
        labels.place(x=800, y=420)
        Thepla = Spinbox(window, from_=0, to=10, textvariable=my_var3)
        Thepla.place(x=70 + 800, y=420)
        img3=Image.open("Thepla.png")
        self.photoimg3=ImageTk.PhotoImage(img3)
        lblimg=Label(window, image=self.photoimg3)
        lblimg.place(x=750, y=225)

        labels = Label(window, text="Kashmiri_Baingan:\nRs.140", font=('calibre', 10, 'bold'))
        labels.place(x=1100, y=420)
        Kashmiri_Baingan = Spinbox(window, from_=0, to=10, textvariable=my_var4)
        Kashmiri_Baingan.place(x=130 + 1100, y=420)
        img4=Image.open("kb.png")
        self.photoimg4=ImageTk.PhotoImage(img4)
        lblimg=Label(window, image=self.photoimg4)
        lblimg.place(x=1100, y=240)

        labels = Label(window, text="Biryani:\nRs.150", font=('calibre', 10, 'bold'))
        labels.place(x=0, y=700)
        Biryani = Spinbox(window, from_=0, to=10, textvariable=my_var5)
        Biryani.place(x=70, y=700)
        img6=Image.open("dal.png")
        self.photoimg6=ImageTk.PhotoImage(img6)
        lblimg=Label(window, image=self.photoimg6)
        lblimg.place(x=800, y=500)

        labels = Label(window, text="Paneer_Masala:\nRs.150", font=('calibre', 10, 'bold'))
        labels.place(x=350, y=700)
        Paneer_Masala = Spinbox(window, from_=0, to=10, textvariable=my_var6)
        Paneer_Masala.place(x=120 + 350, y=700)
        img5=Image.open("panee.png")
        self.photoimg5=ImageTk.PhotoImage(img5)
        lblimg=Label(window, image=self.photoimg5)
        lblimg.place(x=350, y=500)

        labels = Label(window, text="Dal_Bhati:\nRs.150", font=('calibre', 10, 'bold'))
        labels.place(x=800, y=700)
        Dal_Bhati = Spinbox(window, from_=0, to=10, textvariable=my_var7)
        Dal_Bhati.place(x=100 + 800, y=700)
        img7=Image.open("bir.png")
        self.photoimg7=ImageTk.PhotoImage(img7)
        lblimg=Label(window, image=self.photoimg7)
        lblimg.place(x=20, y=500)
        

        labels = Label(window, text="Masala_Dosa:\nRs.100", font=('calibre', 10, 'bold'))
        labels.place(x=1100, y=700)
        Masala_Dosa = Spinbox(window, from_=0, to=10, textvariable=my_var8)
        Masala_Dosa.place(x=100 + 1100, y=700)
        img8=Image.open("dosa.png")
        self.photoimg8=ImageTk.PhotoImage(img8)
        lblimg=Label(window, image=self.photoimg8)
        lblimg.place(x=1150, y=475)

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ak@sh",
            database="mini_project")
        # Creating a cursor object using the cursor() method
        cursor = conn.cursor()


        # Preparing SQL query to INSERT a record into the database.
        def insert():
            sk = Shreekhand.get()
            ad = Alur_Dom.get()
            th = Thepla.get()
            kb = Kashmiri_Baingan.get()
            bir = Biryani.get()
            pm = Paneer_Masala.get()
            db = Dal_Bhati.get()
            md = Masala_Dosa.get()
            blank = "0"

            total_bill = int(sk) * 50 + int(ad) * 150 + int(th) * 70 + int(kb) * 140 + int(bir) * 150 + int(pm) * 150 + int(
                db) * 150 + int(md) * 100 + 60
            print(total_bill)

            sql = "INSERT INTO online_menu(sh,AD,Th,Kb,Bir,PM,DB,MD,Bill,Addr,Tid,PS) VALUES({},{},{},{},{},{},{},{},{},{},{},{})".format(
                sk, ad, th, kb, bir, pm, db, md, total_bill, blank, blank, blank)
            try:
                # Executing the SQL command
                cursor.execute(sql)

                # Commit your changes in the database
                conn.commit()

            except:
                # Rolling back in case of error
                conn.rollback()


        def connadd():
            window.withdraw()
            window2 = Toplevel(window)
            window2.title("Order online")
            window2.resizable(width=TRUE, height=TRUE)
            window2.geometry("1440x1000")
            window2.configure(background='#FFF3E2')

            Label(window2, image=logo).place(x=0, y=-20)

            

            labels = Label(window2, text="Enter Your Address:", font=('Arial', 20, 'bold', 'italic'), background="#FFF3E2")
            labels.place(x=50, y=250)
            address = Entry(window2, width=20, font='Arial 24', )
            address.place(x=330, y=250)

            label2 = Label(window2, text="Your order is:", font=('Arial', 17, 'bold', 'italic'), background="#FFF3E2")
            label2.place(x=50, y=350)

            label2 = Label(window2, text="NOTE: *TOTAL BILL IS INCLUDING 60 RUPEES STANDARD DELIVERY CHARGES",
                        font=('Arial', 8, 'bold', 'italic'), background="#FFF3E2")
            label2.place(x=50, y=650)

            next = Button(window2, text="Proceed for Payment", command=lambda: [payment(), insadd(), exit2()])
            next.place(x=650, y=750)

            try:
                # Executing the SQL command
                trv = Treeview(window2, selectmode='browse')
                trv.grid(row=1, column=1)
                trv.place(x=190, y=400)

                # number of columns
                trv["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9")

                # Defining heading
                trv['show'] = 'headings'

                # width of columns and alignment
                trv.column("1", width=80, anchor='c')
                trv.column("2", width=80, anchor='c')
                trv.column("3", width=80, anchor='c')
                trv.column("4", width=80, anchor='c')
                trv.column("5", width=80, anchor='c')
                trv.column("6", width=80, anchor='c')
                trv.column("7", width=80, anchor='c')
                trv.column("8", width=80, anchor='c')
                trv.column("9", width=80, anchor='c')

                # Headings
                # respective columns
                trv.heading("1", text="Shreekhand")
                trv.heading("2", text="Alur_Dom")
                trv.heading("3", text="Thepla")
                trv.heading("4", text="Kashmiri_Baingan")
                trv.heading("5", text="Biryani")
                trv.heading("6", text="Paneer_Masala")
                trv.heading("7", text="Dal_Bhati")
                trv.heading("8", text="Masala_Dosa")
                trv.heading("9", text="Total_Bill")

                # getting data from MySQL student table
                cursor.execute('''SELECT sh,AD,Th,KB,Bir,PM,DB,MD,Bill FROM online_menu WHERE o_n = (
                                        SELECT MAX(o_n)
                                        FROM online_menu)''')
                i = 0
                for dt in cursor:
                    trv.insert('', i, text="",
                            values=(dt[0], dt[1], dt[2], dt[3], dt[4], dt[5], dt[6], dt[7], dt[8]))
                    i = i + 1

                # Commit your changes in the database
                conn.commit()

            except:
                # Rolling back in case of error
                conn.rollback()

            def insadd():
                add = address.get()
                blank = "0"
                sql_update_query = """Update online_menu set Addr = %s where Addr = %s"""
                input_data = (add, blank)
                cursor.execute(sql_update_query, input_data)
                conn.commit()

            def exit2():
                window2.withdraw()

            def back():
                window2.withdraw()


        def payment():
            window3 = Toplevel(window)
            window3.title("Payment")
            window3.resizable(width=TRUE, height=TRUE)
            window3.geometry("400x600")

            label5 = Label(window3, text="Click Pay now to complete payment", font=('Arial', 17, 'bold', 'italic'))
            label5.place(x=0, y=0)
            paynow = Button(window3, text="Pay now", command=lambda: [transuc(), exit3()])
            paynow.place(x=150, y=80)

            label5 = Label(window3, text="OR", font=('Arial', 17, 'bold', 'italic'))
            label5.place(x=180, y=160)
            label5 = Label(window3, text="Scan the QR to pay", font=('Arial', 17, 'bold', 'italic'))
            label5.place(x=90, y=190)
            Label(window3,image=qr).place(x=65,y=220)

            paynow = Button(window3, text="Paid with QR", command=lambda: [transuc(), exit3()])
            paynow.place(x=150, y=500)

            def exit3():
                window3.withdraw()


        def transuc():
            import random
            import string
            blank = "0"
            s = "DONE"
            res = ''.join(
                random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase + string.ascii_letters,
                            k=10))
            print(res)
            sql_update_query1 = """Update online_menu set Tid = %s where Tid = %s"""
            input_data = (res, blank)
            cursor.execute(sql_update_query1, input_data)
            conn.commit()

            sql_update_query2 = """Update online_menu set PS = %s where P = %s"""
            input_data = (s, blank)
            cursor.execute(sql_update_query2, input_data)
            conn.commit()
            paysuc()


        def paysuc():
            window4 = Toplevel(window)
            window4.title("Payment Successful")
            window4.resizable(width=TRUE, height=TRUE)
            window4.geometry("1440x1000")
            window4.configure(background='#FFF3E2')

            canvas1 = Canvas(window, bg="#FFF3E2", width=1440, height=1000)
            canvas1.pack()

            Label(window4, image=logo).place(x=0, y=-20)
            Label(window4, image=pay).place(x=360, y=140)
            Label(window4, image=g).place(x=0, y=500)
            text = Label(window4, text="Payment Successful", background="#43b14b", font=('Arial', 17, 'bold', 'italic'))
            text1 = Label(window4, text="Thanks for ordering food from us...", background="#43b14b",
                        font=('Arial', 17, 'bold', 'italic'))
            text.place(x=620, y=600)
            text1.place(x=550, y=650)

        


        def home1():
            new_window = Toplevel()
            app = RestaurantManagementSystem(new_window)
            window.withdraw()


if __name__=="__main__": 
    window=Tk()
    logo = PhotoImage(file=r"C:\Users\AKASH\.vscode\mini project\top.png")
    fullmenu = PhotoImage(file=r"C:\Users\AKASH\.vscode\mini project\DBMS PBL(Order Online)\Order Online.png")
    pay = PhotoImage(file=r"C:\Users\AKASH\.vscode\mini project\DBMS PBL(Order Online)\1.png")
    g = PhotoImage(file=r"C:\Users\AKASH\.vscode\mini project\DBMS PBL(Order Online)\g.png")
    qr = PhotoImage(file=r"C:\Users\AKASH\.vscode\mini project\DBMS PBL(Order Online)\qr.png")
    obj=res(window)
    
    window.mainloop()