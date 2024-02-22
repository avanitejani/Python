from tkinter import *
from tkinter import messagebox
import mysql.connector
from tkinter import ttk

# Uncomment and complete the database connection
# db = mysql.connector.connect(host="localhost", user="your_user", password="your_password", database="your_database")
# cursor = db.cursor()

# ... (other imports and root setup)

def add_stock():
    # Get the user input from the entry fields
    name = name_entry.get()
    quantity = quantity_entry.get()
    price = totalq.get()

    # Execute the SQL query to insert the new product stock
    # cursor.execute("INSERT INTO products (name, quantity, price) VALUES (%s, %s, %s)", (name, quantity, price))

    # Commit the changes to the database
    # db.commit()

    # Insert data into TreeView
    insert_data_to_treeview()

    # Clear the entry fields
    name_entry.delete(0, END)
    quantity_entry.delete(0, END)
    total_lbl.delete(0, END)

def insert_data_to_treeview():
    # Get the user input from the entry fields
    name = name_entry.get()
    quantity = quantity_entry.get()
    price = totalq.get()

    # Insert data into TreeView
    listBox.insert("", "end", values=(name, quantity, price))

def showdata():
    global name, quan, totalq, totalp, total_all
    print(f"\n\n Name Of Product: {name.get()}\n Quantity Of Product:{quan.get()}\n Price of Product:{totalq.get()}\n Total Price :{total_all.get()}")

# ... (other GUI components and configuration)

# Uncomment and complete the code for inserting and updating data in the TreeView
# def insert_data_to_treeview():
#     listBox.insert("", "end", values=(name.get(), quan.get(), totalq.get(), total_all.get()))

# ... (other code)

# Uncomment and complete the event binding for double-clicking on the TreeView rows
# listBox.bind('<Double-1>', GetValue)

# ... (other code)

# Uncomment and complete the code for applying a custom style to the TreeView
# style = ttk.Style()
# style.configure("Treeview.Heading", font=('Verdana', 10, 'bold'))

root.mainloop()
