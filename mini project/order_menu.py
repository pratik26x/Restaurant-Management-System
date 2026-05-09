from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
# from thankYou import Thank_win

win = Tk()

wrapper1 = LabelFrame(win, text="Our Menu")
# wrapper2 = LabelFrame(win, text="Your Order")
wrapper2 = LabelFrame(win,text="Your Order",bd=3,bg="#FFE5CA")

img1=Image.open(r"C:\Users\AKASH\.vscode\mini project\Images\full_menu\Reserve table logo.png")
img1=img1.resize((500,250),Image.ANTIALIAS)
photoimg1=ImageTk.PhotoImage(img1)
lblimg=Label(wrapper2, image=photoimg1, bd=0, relief=RIDGE)
lblimg.place(x=730, y=-8, width=500, height=250)



mycanvas = Canvas(wrapper1,background="#FFE5CA",height=300)
mycanvas.pack(side=LEFT, fill="both", expand="yes")

# mycanvas = Canvas(wrapper1)
# mycanvas.pack(side=TOP, fill="both", expand="yes")

yscrollbar = ttk.Scrollbar(wrapper1, orient="vertical", command=mycanvas.yview)
yscrollbar.pack(side=RIGHT, fill="y")

mycanvas.configure(yscrollcommand=yscrollbar.set)

mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion=mycanvas.bbox('all')))

myframe = Frame(mycanvas, bg="#FFE5CA")
mycanvas.create_window((0, 0), window=myframe, anchor="nw")

wrapper1.pack(fill="both", expand="yes", padx=10, pady=10)
wrapper2.pack(fill="both", expand="yes", padx=10, pady=10)
# wrapper2.place(x=600, y=200)


# list of menu items with their images and prices
menu_items = [
    # Maharashtrian Food
    {'name': 'Puran Poli', 'price': 100, 'image': r"C:\Users\AKASH\.vscode\mini project\Images\full_menu\puranpoli.jpg"},
    {'name': 'Misal Pav', 'price': 120, 'image': r"C:\Users\AKASH\.vscode\mini project\Images\full_menu\misal pav.jpg"},
    {'name': 'Shrikhand', 'price': 300, 'image': r"C:\Users\AKASH\.vscode\mini project\Images\full_menu\Shrikhand.jpg"},
    {'name': 'Pithla Bhakari', 'price': 130, 'image': r"C:\Users\AKASH\.vscode\mini project\Images\full_menu\pithla bhakri.jpg"},
    {'name': 'Modak', 'price': 400, 'image': r"C:\Users\AKASH\.vscode\mini project\Images\full_menu\modak.jpg"},

    # Bengali Food
    {'name': 'Sandesh', 'price': 70, 'image': r"C:\Users\AKASH\.vscode\mini project\Images\full_menu\Sandesh.jpg"},
    {'name': 'Alur dom', 'price': 150, 'image': r"C:\Users\AKASH\.vscode\mini project\Images\full_menu\Alur Dom.jpg"},
    {'name': 'Luchi', 'price': 100, 'image': r"C:\Users\AKASH\.vscode\mini project\Images\full_menu\luchi.jpg"},
    {'name': 'Mishti Doi', 'price': 350, 'image': r"C:\Users\AKASH\.vscode\mini project\Images\full_menu\Mishti Doi.jpg"},
    {'name': 'Chholar Dal', 'price': 70, 'image': r"C:\Users\AKASH\.vscode\mini project\Images\full_menu\Chholar Dal.jpg"},

    # Gujarati Food
    {'name': 'Thepla', 'price': 70, 'image': r"C:\Users\AKASH\.vscode\mini project\Images\full_menu\thepla.jpg"},
    {'name': 'Gujarati Dal', 'price': 80, 'image': r"C:\Users\AKASH\.vscode\mini project\Images\full_menu\Gujarati Dal.jpg"},
    {'name': 'Undhiyu', 'price': 450, 'image': r"C:\Users\AKASH\.vscode\mini project\Images\full_menu\undhiyu.jpg"},
    {'name': 'Khaman', 'price': 60, 'image': r"C:\Users\AKASH\.vscode\mini project\Images\full_menu\Khaman.jpg"},
    {'name': 'Khichu', 'price': 100, 'image': r"C:\Users\AKASH\.vscode\mini project\Images\full_menu\Khichu.jpg"},

    # Kashmiri Food
    {'name': 'Kashmiri Saag', 'price': 100, 'image': r"C:\Users\AKASH\.vscode\mini project\Images\full_menu\Kashmiri Saag.jpg"},
    {'name': 'Pulao', 'price': 200, 'image': r"C:\Users\AKASH\.vscode\mini project\Images\full_menu\Pulao.jpg"},
    {'name': 'Kashmiri Rajma', 'price': 120, 'image': r"C:\Users\AKASH\.vscode\mini project\Images\full_menu\Kashmiri Rajma.jpg"},
    {'name': 'Kashmiri Baingan', 'price': 140, 'image': r"C:\Users\AKASH\.vscode\mini project\Images\full_menu\Kashmiri Baingan.jpg"},
    {'name': 'Panner Chaman', 'price': 120, 'image': r"C:\Users\AKASH\.vscode\mini project\Images\full_menu\Panner Chaman.jpg"},

    # Mughalai Food
    {'name': 'Biryani', 'price': 150, 'image': r"C:\Users\AKASH\.vscode\mini project\Images\full_menu\Biryani.jpg"},
    {'name': 'Chicken Chap', 'price': 300, 'image': r"C:\Users\AKASH\.vscode\mini project\Images\full_menu\Chicken Chap.jpg"},
    {'name': 'Khichda', 'price': 170, 'image': r"C:\Users\AKASH\.vscode\mini project\Images\full_menu\Khichda.jpg"},
    {'name': 'Shahi Paneer', 'price': 140, 'image': r"C:\Users\AKASH\.vscode\mini project\Images\full_menu\shahi paneer.jpg"},
    {'name': 'Mughalai Paratha', 'price': 100, 'image': r"C:\Users\AKASH\.vscode\mini project\Images\full_menu\Mughalai Paratha.webp"},

    # Panjabi Food
    {'name': 'Paneer Masala', 'price': 150, 'image': r"C:\Users\AKASH\.vscode\mini project\Images\full_menu\Paneer Masala.jpg"},
    {'name': 'Butter Chicken', 'price': 300, 'image': r"C:\Users\AKASH\.vscode\mini project\Images\full_menu\Butter Chicken.jpg"},
    {'name': 'Chole Bhature', 'price': 150, 'image': r"C:\Users\AKASH\.vscode\mini project\Images\full_menu\chole bhature.jpg"},
    {'name': 'Dal Makhani', 'price': 135, 'image': r"C:\Users\AKASH\.vscode\mini project\Images\full_menu\Dal Makhani.jpg"},
    {'name': 'Rajma Chawal', 'price': 100, 'image': r"C:\Users\AKASH\.vscode\mini project\Images\full_menu\Rajma Chawal.jpeg"},

    # Rajasthani Food
    {'name': 'Dal Bhati', 'price': 150, 'image': r"C:\Users\AKASH\.vscode\mini project\Images\full_menu\Dal Bhati.jpg"},
    {'name': 'Shahi Gatte', 'price': 130, 'image': r"C:\Users\AKASH\.vscode\mini project\Images\full_menu\Shahi Gatte.jpg"},
    {'name': 'Ghever', 'price': 250, 'image': r"C:\Users\AKASH\.vscode\mini project\Images\full_menu\Ghever.webp"},
    {'name': 'Moong Dal Halwa', 'price': 400, 'image': r"C:\Users\AKASH\.vscode\mini project\Images\full_menu\Moog dal halwa.jpg"},
    {'name': 'Malpua', 'price': 225, 'image': r"C:\Users\AKASH\.vscode\mini project\Images\full_menu\Malpua.webp"},

    # South Indian Food
    {'name': 'Idli Sambar', 'price': 80, 'image': r"C:\Users\AKASH\.vscode\mini project\Images\full_menu\Idli Sambar.jpg"},
    {'name': 'Masala Dosa', 'price': 100, 'image': r"C:\Users\AKASH\.vscode\mini project\Images\full_menu\Masala Dosa.jpg"},
    {'name': 'Uttappa', 'price': 110, 'image': r"C:\Users\AKASH\.vscode\mini project\Images\full_menu\Uttappa.jpg"},
    {'name': 'Medu Wada', 'price': 60, 'image': r"C:\Users\AKASH\.vscode\mini project\Images\full_menu\Medu Wada.jpg"},
    {'name': 'Appa', 'price': 50, 'image': r"C:\Users\AKASH\.vscode\mini project\Images\full_menu\Appa.jpg"}
]

# categories = [
#     {'grp':'Maharashtrian Food'},
#     {'grp':'Bengali Food'},
#     {'grp':'Gujarati Food'},
#     {'grp':'Kashmiri Food'},
#     {'grp':'Mughalai Food'},
#     {'grp':'Panjabi Food'},
#     {'grp':'Rajasthani Food'},
#     {'grp':'xyz'}
# ]

# loop over the menu items to create the menu
row_num = 0
col_num = 1
for item in menu_items:

    # load and resize the image
    img = Image.open(item['image'])
    img = img.resize((245, 245), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)

    # create a label for the image
    img_label = Label(myframe, image=img)
    img_label.image = img  # to prevent garbage collection of the image
    img_label.grid(row=row_num+1, column=col_num, padx=15, pady=5)
    
    # create a label for the name of the item
    name_label = Label(myframe, text=item['name'], font=('Arial', 12, 'bold'), bg="#FFE5CA")
    name_label.grid(row=row_num+2, column=col_num, sticky='w', padx=20, pady=2)
    
    # create a label for the price of the item
    price_label = Label(myframe, text='Rs.{:.2f}'.format(item['price']), font=('Arial', 10), bg="#FFE5CA")
    price_label.grid(row=row_num+3, column=col_num, sticky='w', padx=20, pady=2)
    
    # create a spinbox to select the quantity of the item
    quantity_var = IntVar()
    quantity_spinbox = Spinbox(myframe, from_=0, to=10, width=3, textvariable=quantity_var)
    quantity_spinbox.grid(row=row_num+4, column=col_num, padx=45, pady=2)
    
    # create a button to add the item to the order list
    def add_to_order(name, price, quantity):
        item_price = price * quantity
        order_list.insert(END, f"{name} x {quantity} - Rs.{item_price:.2f}")
    

    add_to_order_button = Button(myframe, text="Add to Order", command=lambda name=item['name'], price=item['price'], quantity_var=quantity_var: add_to_order(name, price, quantity_var.get()))
    add_to_order_button.grid(row=row_num+5, column=col_num, padx=5, pady=5)
    
    # # update column and row numbers
    # col_num += 1
    # if col_num == 5:
    #     col_num = 0
    #     row_num += 5



    # update column and row numbers
    col_num += 1
    if col_num == 6:
        col_num = 1
        row_num += 6
        # for i in categories:
        #     grp_label = Label(myframe, text=i['grp'], font=('Arial', 12, 'bold'), bg="#FFE5CA")
        #     grp_label.grid(row=row_num, column=2, sticky='w', padx=5, pady=2)




# # create a label for the order list
# order_list_label = Label(wrapper2, text="Order List", font=('Arial', 14, 'bold'))
# order_list_label.pack(pady=0)

# create a listbox to display the order list
order_list = Listbox(wrapper2, font=('Arial', 40), height=1)
order_list.pack(fill="y", side='left', padx=10, pady=0)


def open_new_window():
    new_window = Toplevel()
    thank_win = Thank_win(new_window)

order_btn = Button(wrapper2, text="Order", command=open_new_window, font=("times new roman", 35,"bold"), bg="black", fg="gold",  cursor="hand2")
# order_btn = Button (wrapper2, text="Order",font=("times new roman", 14,"bold"), bg="black", fg="gold",  cursor="hand2")
order_btn.place(x=900, y=200)


win.geometry("1440x1080+0+0")
win.resizable(False, False)
win.title("Menu")
win.mainloop()
