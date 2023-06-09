# # Tkinter is a python GYI Module
# # Geaphical User Interface
# # first install tkinter
# # pip install tk

# from tkinter import *  # import everything from tkinter module
# root=Tk()  # create a screen
# # "widthxheight"

# root.geometry("800x500")  # set screen initial size
# root.minsize(200,200) #set minsize for window scree
# root.maxsize(600, 500)  # set maxsize for window scree

# root.mainloop()  # show screen until se close it





from tkinter import *
# from PIL import ImageTk
# from tkinter import messagebox
# import ast

root=Tk()
root.title('Login')
root.geometry("430x500")
# root.configure(bg="#fff")
root.resizable(False,False)

f=Frame(root,width=350,height=350,bg="red")
f.place(x=480,y=70)

h=Label(f,text="Singn in",fg="red",border=0,bg="white",font=("Gadugi",20,"bold"))
h.place(x=100,y=5)

#................................................................................

user=Entry(f,width=25,fg="red",bg="white",font="Gadugi")
user.place(x=30,y=80)
user.insert(0,"Username")


Frame(f,width=200,height=2,bg="red").place(x=25,y=100)
#.................................................................
code=Entry(f,width=25,fg="red",bg="white",font="Gadugi")
code.place(x=30,y=150)
code.insert(0,"Password")


Frame(f,width=200,height=2,bg="red").place(x=254,y=150)




root.mainloop()






# import tkinter as tk
# import mysql.connector
# from tkinter import *
  
 
# def submitact():
     
#     user = Username.get()
#     passw = password.get()
  
#     print(f"The name entered by you is {user} {passw}")
  
#     logintodb(user, passw)
  
 
# def logintodb(user, passw):
     
#     # If password is entered by the
#     # user
#     if passw:
#         db = mysql.connector.connect(host ="localhost",
#                                      user = user,
#                                      password = passw,
#                                      db ="College")
#         cursor = db.cursor()
         
#     # If no password is entered by the
#     # user
#     else:
#         db = mysql.connector.connect(host ="localhost",
#                                      user = user,
#                                      db ="College")
#         cursor = db.cursor()
         
#     # A Table in the database
#     savequery = "select * from STUDENT"
     
#     try:
#         cursor.execute(savequery)
#         myresult = cursor.fetchall()
         
#         # Printing the result of the
#         # query
#         for x in myresult:
#             print(x)
#         print("Query Executed successfully")
         
#     except:
#         db.rollback()
#         print("Error occurred")
  
 
# root = tk.Tk()
# root.geometry("300x300")
# root.title("DBMS Login Page")
  
 
# # Defining the first row
# lblfrstrow = tk.Label(root, text ="Username -", )
# lblfrstrow.place(x = 50, y = 20)
 
# Username = tk.Entry(root, width = 35)
# Username.place(x = 150, y = 20, width = 100)
  
# lblsecrow = tk.Label(root, text ="Password -")
# lblsecrow.place(x = 50, y = 50)
 
# password = tk.Entry(root, width = 35)
# password.place(x = 150, y = 50, width = 100)
 
# submitbtn = tk.Button(root, text ="Login",
#                       bg ='blue', command = submitact)
# submitbtn.place(x = 150, y = 135, width = 55)
 
# root.mainloop()
