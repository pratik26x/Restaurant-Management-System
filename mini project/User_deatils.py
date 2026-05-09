from tkinter import *
from tkinter import font
from PIL import Image,ImageTk




class ud:
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

        cust_btn_home=Button (main_frame, text="HOME",command=self.home,width=25,height=4,font=("times new roman", 14,"bold"), bg="black", fg="gold",  cursor="hand1")
        cust_btn_home.grid(row=0,column=0)
        
        cust_btn_home=Button (main_frame, text="ABOUT US",width=25,height=4,font=("times new roman", 14,"bold"), bg="#FFE5CA", fg="black",  cursor="hand1")
        cust_btn_home.grid(row=0,column=1)

        cust_btn_home=Button (main_frame, text="MENU",command=self.menu,width=27,height=4,font=("times new roman",14,"bold"), bg="black", fg="gold",  cursor="hand1")
        cust_btn_home.grid(row=0,column=2)

        cust_btn_home=Button (main_frame, text="CONTACT",command=self.contact1,width=25,height=4,font=("times new roman", 14,"bold"), bg="black", fg="gold",  cursor="hand1")
        cust_btn_home.grid(row=0,column=3)

        cust_btn_home=Button (main_frame, text="USER",width=25,height=4,font=("times new roman", 14,"bold"), bg="black", fg="gold",  cursor="hand1")
        cust_btn_home.grid(row=0,column=4)

        main_home=Frame(self.home_root,relief=RIDGE,bd=0,bg="#FFE5CA")
        main_home.place(x=0,y=238,width=1520,height=620)

        # self.home_root=home_root
        # self.home_root.title("User Details")
        # self.home_root.geometry("1520x520+0+270")

        # self.var_ref =StringVar()
        # x = random.randint(1000,9999)
        # self.var_ref.set(str(x))

        self.var_fname = StringVar()
        # self.var_lname = StringVar()
        self.var_mobno = StringVar()
        self.var_address = StringVar()
        self.var_email = StringVar()

        
        def create_Profile():
            
            if self.var_fname.get()=="" or self.var_mobno.get()=="" or self.var_address.get()=="":
                messagebox.showerror("ERROR","All fields are required")
            else:
                try:
                    conn = mysql.connector.connect(host="localhost",username="root",password="rutu@123",database="user")
                    my_cursor = conn.cursor()
                    my_cursor.execute("insert into user_details values(%s,%s,%s,%s)",(
                                                                    #    self.var_ref.get(),
                                                                       self.var_fname.get(),
                                                                    #    self.var_lname.get(),
                                                                       self.var_address.get(),
                                                                       self.var_mobno.get(),
                                                                       self.var_email.get()                
                                                                  ))
                    conn.commit()
                    fname = entry_fname.get()
                    add = entry_add.get()
                    mob = entry_mob.get()
                    email = entry_email.get()

                    tableframe = LabelFrame(self.home_root,bd=2,relief=RIDGE,text="View User Details",font=("times new roman",22,"bold"),padx=2)
                    tableframe.place(x=900,y=300,width=610,height=460)

                    lbl_fname = Label(tableframe,text="Name : " + fname,font=("times new roman",20,"bold"),padx=5,pady=5)
                    lbl_fname.grid(row=0,column=0,padx=5,pady=5)

                    lbl_add = Label(tableframe,text="Address : " + add,font=("times new roman",20,"bold"),padx=5,pady=5)
                    lbl_add.grid(row=1,column=0,padx=5,pady=5)

                    lbl_mob = Label(tableframe,text="Mobile no : " + mob,font=("times new roman",20,"bold"),padx=5,pady=5)
                    lbl_mob.grid(row=2,column=0,padx=5,pady=5)

                    lbl_email = Label(tableframe,text="Email ID : " + email,font=("times new roman",20,"bold"),padx=5,pady=5)
                    lbl_email.grid(row=3,column=0,padx=5,pady=5)
                    conn.close()
                    messagebox.showinfo("Success","Your details has been Saved",parent=self.home_root)
                except Exception as es:
                    messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.home_root)
        
        
        def update():
            if self.var_fname.get()=="" or self.var_mobno.get()=="" or self.var_address.get()=="":
                messagebox.showerror("Error","Please enter your details",parent=self.home_root)
            else:
                conn = mysql.connector.connect(host="localhost",username="root",password="rutu@123",database="user")
                my_cursor = conn.cursor()
                my_cursor.execute("update user_details set Name=%s,Address=%s,Email=%s where Mobile_No=%s",(
                                                                                            self.var_fname.get(),
                                                                                            # self.var_lname.get(),
                                                                                            self.var_address.get(),
                                                                                            self.var_email.get(),
                                                                                            self.var_mobno.get()
                                                                                            # self.var_ref.get()  
                                                                                       )) 
                conn.commit()
                # ref = entry_ref.get()
                fname = entry_fname.get()
                # lname = entry_lname.get()
                add = entry_add.get()
                mob = entry_mob.get()
                email = entry_email.get()

                tableframe = LabelFrame(self.home_root,bd=2,relief=RIDGE,text="View User Details",font=("times new roman",22,"bold"),padx=2)
                tableframe.place(x=900,y=300,width=610,height=460)

            # lbl_user_ref = Label(tableframe,text="Ref : " + ref,font=("times new roman",20,"bold"),padx=5,pady=5)
            # lbl_user_ref.grid(row=0,column=0,padx=5,pady=5)

                lbl_fname = Label(tableframe,text="First Name : " + fname,font=("times new roman",20,"bold"),padx=5,pady=5)
                lbl_fname.grid(row=0,column=0,padx=5,pady=5)
            
            # lbl_lname = Label(tableframe,text="Last Name : " + lname,font=("times new roman",20,"bold"),padx=5,pady=5)
            # lbl_lname.grid(row=2,column=0,padx=5,pady=5)

                lbl_add = Label(tableframe,text="Address : " + add,font=("times new roman",20,"bold"),padx=5,pady=5)
                lbl_add.grid(row=1,column=0,padx=5,pady=5)

                lbl_mob = Label(tableframe,text="Mobile no : " + mob,font=("times new roman",20,"bold"),padx=5,pady=5)
                lbl_mob.grid(row=2,column=0,padx=5,pady=5)

                lbl_email = Label(tableframe,text="Email ID : " + email,font=("times new roman",20,"bold"),padx=5,pady=5)
                lbl_email.grid(row=3,column=0,padx=5,pady=5)
                
                conn.close()
                messagebox.showinfo("Update","Your details has been updated",parent=self.home_root)


        def Delete():
            Delete = messagebox.askyesno("User Profile","Do you want to delete this user details?",parent=self.home_root)
            if Delete>0:
                conn =  mysql.connector.connect(host="localhost",username="root",password="rutu@123",database="user")
                my_cursor = conn.cursor()
                query = "delete from user_details where Mobile_No=%s"
                value = (self.var_mobno.get(),)
                my_cursor.execute(query,value)
            else:
                if not Delete:
                    return
            
            conn.commit()
            # ref = entry_ref.get()
            fname = entry_fname.get()
            # lname = entry_lname.get()
            add = entry_add.get()
            mob = entry_mob.get()
            email = entry_email.get()

            tableframe = LabelFrame(self.home_root,bd=2,relief=RIDGE,text="View User Details",font=("times new roman",22,"bold"),padx=2)
            tableframe.place(x=900,y=300,width=610,height=460)

            # lbl_user_ref = Label(tableframe,text="Ref : ",font=("times new roman",20,"bold"),padx=5,pady=5)
            # lbl_user_ref.grid(row=0,column=0,padx=5,pady=5)

            lbl_fname = Label(tableframe,text="First Name : ",font=("times new roman",20,"bold"),padx=5,pady=5)
            lbl_fname.grid(row=0,column=0,padx=5,pady=5)
            
            # lbl_lname = Label(tableframe,text="Last Name : ",font=("times new roman",20,"bold"),padx=5,pady=5)
            # lbl_lname.grid(row=2,column=0,padx=5,pady=5)

            lbl_add = Label(tableframe,text="Address : ",font=("times new roman",20,"bold"),padx=5,pady=5)
            lbl_add.grid(row=1,column=0,padx=5,pady=5)

            lbl_mob = Label(tableframe,text="Mobile no : ",font=("times new roman",20,"bold"),padx=5,pady=5)
            lbl_mob.grid(row=2,column=0,padx=5,pady=5)

            lbl_email = Label(tableframe,text="Email ID : ",font=("times new roman",20,"bold"),padx=5,pady=5)
            lbl_email.grid(row=3,column=0,padx=5,pady=5)

            conn.close()
        
        
        lbl_title = Label(self.home_root,text="ADD USER DETAILS", font=("times new roman", 25,"bold"), bg="black", fg="gold")
        lbl_title.place(x=0,y=250,width=1520,height=50)

        labelframe = LabelFrame(self.home_root,bd=2,relief=RIDGE,text="User Details",font=("times new roman",22,"bold"),padx=2)
        labelframe.place(x=10,y=300,width=880,height=460)

        # lbl_user_ref = Label(labelframe,text="User Ref",font=("times new roman",20,"bold"),padx=2,pady=6)
        # lbl_user_ref.grid(row=0,column=0,sticky=W)

        # entry_ref = ttk.Entry(labelframe,textvariable=self.var_ref,width=20,font=("times new roman",20,"bold"),state="readonly")
        # entry_ref.grid(row=0,column=1,padx=10)

        lbl_fname = Label(labelframe,text="Name",font=("times new roman",20,"bold"),padx=2,pady=6)
        lbl_fname.grid(row=0,column=0,sticky=W)

        entry_fname = ttk.Entry(labelframe,textvariable=self.var_fname,width=20,font=("times new roman",20,"bold"))
        entry_fname.grid(row=0,column=1,padx=10)

        # lbl_lname = Label(labelframe,text="Last Name",font=("times new roman",20,"bold"),padx=2,pady=6)
        # lbl_lname.grid(row=2,column=0,sticky=W)

        # entry_lname = ttk.Entry(labelframe,textvariable=self.var_lname,width=20,font=("times new roman",20,"bold"))
        # entry_lname.grid(row=2,column=1,padx=10)

        lbl_add = Label(labelframe,text="Address",font=("times new roman",20,"bold"),padx=2,pady=6)
        lbl_add.grid(row=1,column=0,sticky=W)

        entry_add = ttk.Entry(labelframe,textvariable=self.var_address,width=20,font=("times new roman",20,"bold"))
        entry_add.grid(row=1,column=1,padx=10)

        lbl_mob = Label(labelframe,text="Mobile No.",font=("times new roman",20,"bold"),padx=2,pady=6)
        lbl_mob.grid(row=2,column=0,sticky=W)

        entry_mob = ttk.Entry(labelframe,textvariable=self.var_mobno,width=20,font=("times new roman",20,"bold"))
        entry_mob.grid(row=2,column=1,padx=10)

        lbl_email = Label(labelframe,text="Email ID",font=("times new roman",20,"bold"),padx=2,pady=6)
        lbl_email.grid(row=3,column=0,sticky=W)

        entry_email = ttk.Entry(labelframe,textvariable=self.var_email,width=20,font=("times new roman",20,"bold"))
        entry_email.grid(row=3,column=1,padx=10)

        btn_frame = Frame(labelframe,bd=2,relief=RIDGE)
        btn_frame.place(x=10,y=330,width=610,height=45)

        btnAdd = Button(btn_frame,text="Save & Display",font=("times new roman",18,"bold"),bg="black",fg="gold",width=14,command=create_Profile)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate = Button(btn_frame,text="UPDATE",font=("times new roman",18,"bold"),bg="black",fg="gold",width=14,command=update)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete = Button(btn_frame,text="DELETE",font=("times new roman",18,"bold"),bg="black",fg="gold",width=14,command=Delete)
        btnDelete.grid(row=0,column=2,padx=1)

    def contact1(self):
        from contact import contact
        self.new_window = Toplevel(self.home_root)
        self.app = contact(self.new_window)
        self.home_root.withdraw()

    def menu(self):
        from full_menu import full_Menu_win
        self.new_window = Toplevel(self.home_root)
        self.app = full_Menu_win(self.new_window)
        self.home_root.withdraw()

    def home(self):
        from home_page import RestaurantManagementSystem
        self.new_window = Toplevel(self.home_root)
        self.app = RestaurantManagementSystem(self.new_window)
        self.root_menu.withdraw()

        


if __name__=="__main__":
    root=Tk()
    obj=ud(root)
    root.mainloop()