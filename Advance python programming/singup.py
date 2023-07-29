# pip install pillo
# pip install pymysql

from tkinter import *
from tkinter import messagebox
import pymysql

root=Tk()

root.geometry('430x550')
root.resizable(0,0) 
emailvar=StringVar()
uservar=StringVar()
pwdvar=StringVar()
def clear():
    emailEntry.delete(0,END)
    UsernameEntry.delete(0,END)
    PswdEntry.delete(0,END)
    CpswdEntry.delete(0,END)
    check.set(0)
    root.destroy()
    import login




def connect_database():
    
    import mysql.connector
    
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database="banking"
    )
    print(emailvar.get(),uservar.get(),pwdvar.get())
    cursor = mydb.cursor()
    query=f"insert into user(uemail,uname,pwd) values(%s,%s,%s)"
    # args=
    cursor.execute(query,(emailvar.get(),uservar.get(),pwdvar.get()))
    mydb.commit()
    
def login_page():
    root.destroy()
    import login





f1=Frame(root,width=70,height=40)
f1.place(x=50,y=20)
heading = Label(f1 , text = "  Crate An Account  ",fg='black' , font = 'Verdana 21 bold',bg="orange")
heading.grid(row=0,column=0,padx=15,pady=20)

emailLabel=Label(f1,text='email', font = 'Verdana 10 bold',)
emailLabel.grid(row=1,column=0,sticky='w',padx=15,pady=2)
emailEntry=Entry(f1,width=20, font = 'Verdana 15 bold',fg='black',textvariable=emailvar)
emailEntry.grid(row=2,column=0,sticky='w',padx=15,pady=5)


UsernameLabel=Label(f1,text='User Name', font = 'Verdana 10 bold',)
UsernameLabel.grid(row=3,column=0,sticky='w',padx=15,pady=5)
UsernameEntry=Entry(f1,width=20, font = 'Verdana 15 bold',fg='black',textvariable=uservar)
UsernameEntry.grid(row=4,column=0,sticky='w',padx=15,pady=2)


PswdLabel=Label(f1,text='Password', font = 'Verdana 10 bold',)
PswdLabel.grid(row=5,column=0,sticky='w',padx=15,pady=5)
PswdEntry=Entry(f1,width=20, font = 'Verdana 15 bold',fg='black',textvariable=pwdvar)
PswdEntry.grid(row=6,column=0,sticky='w',padx=15,pady=2)


CpswdLabel=Label(f1,text='Confirm Password', font = 'Verdana 10 bold',)
CpswdLabel.grid(row=7,column=0,sticky='w',padx=15,pady=5)
CpswdEntry=Entry(f1,width=20, font = 'Verdana 15 bold',fg='black')
CpswdEntry.grid(row=8,column=0,sticky='w',padx=15,pady=2)

check=IntVar()
termsandcoditions=Checkbutton(f1,text=' I  Agree to Terms & Conditions   ', font = 'Verdana 12 bold',cursor='hand2',variable=check)
termsandcoditions.grid(row=9,column=0,sticky='w',pady=10)


SignupButton=Button(root,text="Signup", font='Verdana 16 bold',bg="orange",fg="black",bd=5,activebackground="grey",activeforeground="white",command=connect_database)
SignupButton.grid(row=10,column=15,sticky='w',pady=400,padx=170)


#signup button
LoginLabel=Label(root,text=" Don't Have An Account ? ",bd=0,bg="white",activebackground="white",font='Verdana 8 bold',fg="black",activeforeground="orange") #cursor="hande2"
LoginLabel.place(x=50,y=500)
# LoginLabel.grid(row=12,column=0,sticky='w',pady=0,padx=10)


# loginburron=Button(f1,text="Log in", font='Verdana 16 bold',bg="orange",fg="black",bd=5,activebackground="grey",activeforeground="white")
# # loginburron.grid(row=11,column=1)
# loginburron.place(x=100,width=80,height=40,y=550)

loginburron=Button(root,text="Log in",bd=0,bg="white",activebackground="white",font='Verdana 9 bold',fg="orange",activeforeground="black",command=login_page) #cursor="hande2"
loginburron.place(x=250,y=495)

root.mainloop()
