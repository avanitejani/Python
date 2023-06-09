from tkinter import *
# import tkinter as tk
import mysql.connector

root=Tk()
# root.geometry('430x550')


# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="product"
)
# mycursor = db.cursor()
# query=f"""create database product"""
# mycursor.execute(query)

# Create a cursor object to execute SQL queries
cursor = db.cursor()

# cursor.execute(query,(emailvar.get(),uservar.get(),pwdvar.get()))
db.commit()

# Create the main application window
root = Tk()
root.title("Product Manager")

# Function to retrieve and display product stocks
def view_stock():
    # Clear the existing stock table
    for widget in frame.winfo_children():
        widget.destroy()

    # Execute the SQL query to fetch all product stocks
    cursor.execute("SELECT * FROM products")

    # Retrieve the results from the query
    stocks = cursor.fetchall()

    # Display the stock information in a table format
    for i, stock in enumerate(stocks):
        for j, value in enumerate(stock):
            label = Label(frame, text=value)
            label.grid(row=i, column=j)

# Function to add a new product stock
def add_stock():
    # Get the user input from the entry fields
    name = name_entry.get()
    quantity = quantity_entry.get()

    # Execute the SQL query to insert the new product stock
    cursor.execute("INSERT INTO products (name, quantity) VALUES (%s, %s)", (name, quantity))

    # Commit the changes to the database
    db.commit()

    # Clear the entry fields
    name_entry.delete(0, END)
    quantity_entry.delete(0,END)

    # Refresh the stock table
    view_stock()

# Create the stock table frame
frame = Frame(root)
frame.pack()

# Create the "View Stock" button
view_stock_button = Button(root, text="View Stock", command=view_stock)
view_stock_button.pack()

# Create the "Add Stock" section
name_label = Label(root, text="Product Name",fg='black' , font = 'Verdana 25 bold')
name_label.pack()
name_entry = Entry(root)
name_entry.pack()

quantity_label = Label(root, text="Quantity")
quantity_label.pack()
quantity_entry = Entry(root)
quantity_entry.pack()

add_stock_button = Button(root, text="Add Stock", command=add_stock)
add_stock_button.pack()

# Start the Tkinter event loop
root.mainloop()









root.mainloop()




































# import tkinter as tk
# import mysql.connector

# # Connect to the MySQL database
# db = mysql.connector.connect(
#     host="your_host",
#     user="your_username",
#     password="your_password",
#     database="your_database"
# )

# # Create a cursor object to execute SQL queries
# cursor = db.cursor()

# # Create the main application window
# window = tk.Tk()
# window.title("Product Manager")

# # Function to retrieve and display product stocks
# def view_stock():
#     # Clear the existing stock table
#     for widget in frame.winfo_children():
#         widget.destroy()

#     # Execute the SQL query to fetch all product stocks
#     cursor.execute("SELECT * FROM products")

#     # Retrieve the results from the query
#     stocks = cursor.fetchall()

#     # Display the stock information in a table format
#     for i, stock in enumerate(stocks):
#         for j, value in enumerate(stock):
#             label = tk.Label(frame, text=value)
#             label.grid(row=i, column=j)

# # Function to add a new product stock
# def add_stock():
#     # Get the user input from the entry fields
#     name = name_entry.get()
#     quantity = quantity_entry.get()

#     # Execute the SQL query to insert the new product stock
#     cursor.execute("INSERT INTO products (name, quantity) VALUES (%s, %s)", (name, quantity))

#     # Commit the changes to the database
#     db.commit()

#     # Clear the entry fields
#     name_entry.delete(0, tk.END)
#     quantity_entry.delete(0, tk.END)

#     # Refresh the stock table
#     view_stock()

# # Create the stock table frame
# frame = tk.Frame(window)
# frame.pack()

# # Create the "View Stock" button
# view_stock_button = tk.Button(window, text="View Stock", command=view_stock)
# view_stock_button.pack()

# # Create the "Add Stock" section
# name_label = tk.Label(window, text="Product Name")
# name_label.pack()
# name_entry = tk.Entry(window)
# name_entry.pack()

# quantity_label = tk.Label(window, text="Quantity")
# quantity_label.pack()
# quantity_entry = tk.Entry(window)
# quantity_entry.pack()

# add_stock_button = tk.Button(window, text="Add Stock", command=add_stock)
# add_stock_button.pack()

# # Start the Tkinter event loop
# window.mainloop()



