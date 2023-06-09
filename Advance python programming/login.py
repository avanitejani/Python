# pip install pillo
# pip install pymysql


from tkinter import *
# import mysql.connector
# from tkinter import messagebox
import pymysql
root=Tk()
root.geometry('430x550')
root.resizable(0,0) 
# def login_user():
#     if usernameEntry.get()=="" or passwordEntry.get()=="":
#         messagebox.showerror('Error',"All fieldes Are Required")

usename=StringVar()
pswd=StringVar()


def connect_database():

    
    import mysql.connector


    
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database="banking"
    )
    print(usename.get(),pswd.get())
    cursor = mydb.cursor()
    query=f"insert into user(usename,pswd) values(%s,%s)"
    # args=
    cursor.execute(query,(usename.get(),pswd.get()))
    mydb.commit()

def singup_page():
    root.destroy()
    import singup


def usrnm(event):
    if usernameEntry.get()== "User Name":
        usernameEntry.delete(0,END)

def pwds(event):
    if passwordEntry.get()== "Password":
        passwordEntry.delete(0,END)

root=Tk()
root.geometry('430x550') 
root.resizable(0,0) 
root.title('Login Page')

#heading label
heading = Label(root , text = "Login",fg='black' , font = 'Verdana 25 bold')
heading.place(x=160 , y=80)

#username label and text entry box  
# usernameLabel=Label(root,text="User Name*", font='Verdana 10 bold',pady=10,padx=20)
# usernameLabel.place(x=80,y=170)
usernameEntry=Entry(root,width=25,bd=0,fg='black' ,font='Verdana 10 bold')
usernameEntry.place(x=80,y=170,width=280,height=30)
usernameEntry.insert(0,"User Name")
usernameEntry.bind('<FocusIn>',usrnm)
f1=Frame(root,width=280,height=2,bg="black")
f1.place(x=80,y=205)


passwordEntry=Entry(root,width=25,bd=0,fg='black' ,font='Verdana 10 bold')
passwordEntry.place(x=80,y=220,width=280,height=30)
passwordEntry.insert(0,"password")
passwordEntry.bind('<FocusIn>',pwds)
f2=Frame(root,width=280,height=2,bg="black")
f2.place(x=80,y=255)

forgetButton=Button(root,text="Forgot Password ? ",bd=0,bg="white",activebackground="white",font='Verdana 10 bold',fg="black",activeforeground="orange",cursor='hand2') #cursor="hande2"
forgetButton.place(x=210,y=260)


#login button
  
loginButton=Button(root,text="Login", font='Verdana 10 bold',bg="orange",fg="black",bd=5,activebackground="grey",activeforeground="white",command=connect_database)
loginButton.place(x=80,y=330,width=280,height=40)

#signup button
signupLabel=Label(root,text=" Don't Have An Account ? ",bd=0,bg="white",activebackground="white",font='Verdana 8 bold',fg="black",activeforeground="orange") #cursor="hande2"
signupLabel.place(x=130,y=420)

signupButton=Button(root,text="Creact New One",bd=0,bg="white",activebackground="white",font='Verdana 9 bold',fg="orange",activeforeground="black",command=singup_page) #cursor="hande2"
signupButton.place(x=155,y=450)


 


root.mainloop()
