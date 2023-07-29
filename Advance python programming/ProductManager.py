
from tkinter import *
# from tkinter import tk
from tkinter import messagebox
from tkinter import ttk, messagebox

import mysql.connector
root=Tk()
root.geometry('1000x750')
root.title("Insert Data")

def add_stock():
    # Get the user input from the entry fields
    name = name_entry.get()
    

    # Execute the SQL query to insert the new product stock
    # cursor.execute("INSERT INTO products (name, quantity) VALUES (%s, %s)", (name, quantity))

    # Commit the changes to the database
    # db.commit()

    # Clear the entry fields
    name_entry.delete(0, END)
    quantity_entry.delete(0,END)

    # Refresh the stock table
    # view_stock()



root.title("Product Manager")
name=StringVar()
quan=IntVar()
totalq=IntVar()
totalp=IntVar()
total_all=StringVar()

def total():
    global totalp,total_all
    totalp=(
        (quan.get() * totalq.get())
    )
    total_all.set("Rs. "+str(totalp))




def showdata():
    global name,quan,totalq,totalp,total_all
    print(f"\n\n name Of Product: {name.get()}\n Quantity Of Product:{quan.get()}\n Price of Product:{totalq.get()}\n Total Price :{total_all.get()}")


# Create the "Add Stock" section

name_label=Label(root,text="product Name",font='Verdana 10 bold',pady=10,padx=20)
name_label.place(x=60,y=100)
name_entry=Entry(bd=2,relief="raised",font='Verdana 10 bold',textvariable=name)
name_entry.place(x=250,y=100,width=250,height=30)

quantity_label=Label(root,text="Quantity",font='Verdana 10 bold')
quantity_label.place(x=80,y=150)
quantity_entry=Entry(bd=2,relief="raised",font='Verdana 10 bold',textvariable=quan)
quantity_entry.place(x=250,y=150,width=250,height=30)

total_lbl=Label(root,text="product Price",font='Verdana 10 bold')
total_lbl.place(x=80,y=200)
total_lbl=Entry(bd=2,relief="raised",font='Verdana 10 bold',textvariable=totalq)
total_lbl.place(x=250,y=200,width=250,height=30)

total_price=Label(root,text="Total Price",font='Verdana 10 bold')
total_price.place(x=80,y=250)
total_price=Entry(bd=2,relief="raised",font='Verdana 10 bold',textvariable=total_all)
total_price.place(x=250,y=250,width=250,height=30)

#Enter
add_stock_button=Button(text="Add Stock",font='Verdana 10 bold',bg="orange",fg="black",bd=5,relief="raised",command=total)
add_stock_button.place(x=100,y=330,width=150,height=40)
       
# Create the "delete Stock" button
delet_stock_button=Button(text="Delete Stock",font='Verdana 10 bold',bg="orange",fg="black",bd=5,relief="raised",command=total)
delet_stock_button.place(x=300 ,y=330,width=150,height=40)


delet_stock_button=Button(text="view Stock",font='Verdana 10 bold',bg="orange",fg="black",bd=5,relief="raised",command=showdata)
delet_stock_button.place(x=500,y=330,width=150,height=40)


cols = ('productName', 'Quantity', 'Price','TotalPrice')
listBox = ttk.Treeview(root, columns=cols, show='headings' )

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=80, y=400)



# style = ttk.Style()
# style.configure("Treeview.Heading", font='Verdana 10 bold')

# def GetValue(event):
#     name_entry.delete(0, END)
#     quantity_entry.delete(0, END)
#     total_lbl.delete(0, END)
#     total_price.delete(0, END)

#     row_id = listBox.selection()[0]
#     select = listBox.set(row_id)

#     name_entry.insert(0,select['product Name'])
#     quantity_entry.insert(0,select['Quantity'])
#     total_lbl.insert(0,select['product Price'])
#     total_price.insert(0,select['Total Price'])

# def show():
#         mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="banking")
#         mycursor = mysqldb.cursor()
#         mycursor.execute("SELECT id,empname,mobile,salary FROM registation")
#         records = mycursor.fetchall()
#         print(records)

#         for i, (id,stname, course,fee) in enumerate(records, start=1):
#             listBox.insert("", "end", values=(id, stname, course, fee))
#             mysqldb.close()

# show
# ()
# listBox.bind('Double-Button-1',GetValue)





# style=ttk.style()
# style.configure("Treeview.Heading",font=('Verdana 10 bold'))

# my_tree['columns']=("productName","Quantity","Price",'"TotalPrice")
# my_tree.column("")




# f1 = Frame(root)
# f1.pack()
# b1 = Button(f1, text="Cliuck ME")
# b1.pack()

# s1 = Scrollbar(f1)
# l1 = Listbox(f1, width=20, yscrollcommand=s1.set)
# s1.pack(side="right", fill="y")

# l1.pack()
# s1.config(command=l1.yview)
# s1.place(x=150,y=400,width=130,height=40)





root.mainloop()


