from tkinter import *
root=Tk()
root.geometry("430x500")
root.resizable(0,0) 
# namee StringVar(20)
# contact IntVar
# email StringVar(20)
# gen StringVar(20)
# city StringVar(20)
# state StringVar(20)

def showdata():
    # file=open("Registration.txt","a")
    # file.write(f"name: {name.get()}\ncontect: {contact.get()}\nemail: {email.get()}\nGender : {Gen.get()}\nCity : {selcton1.get()}\nState : {selcton2.get()}\n\n")
    print(f"name: {namee.get()}\ncontect: {contact.get()}\nemail: {email.get()}\nGender : {gen.get()}\nCity : {city.get()}\nState : {state.get()}\n\n")
    

namee=StringVar()
contact=IntVar()
contact.set(" ")
email=StringVar()
Male=IntVar()
Female=IntVar()
gen=StringVar()
gen.set("Male")

city=StringVar()
city.set( " " )
state=StringVar()
state.set( " " )

Button1=StringVar()


l0 = Label(text="Please Enter details below", font='Verdana 10 bold', bg="orange", fg="white", padx=60,pady=12)
l0.pack(fill=X)


def connect_databas():
    
    import mysql.connector
    
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database="banking",
        port='3306'
    )
    print(namee.get(),contact.get(),email.get(),gen.get(),city.get(),state.get())
    cursor = mydb.cursor()
    query=f"insert into user(namee,contact,email,gen,city,state) values(%s,%s,%s,%s,%s,%s)"
    # args=
    cursor.execute(query,(namee.get(),contact.get(),email.get()),gen.get(),city.get(),state.get())
    mydb.commit()
# l0.pack(anchor="n", side="top", fill=X, padx=5)

root.title("Registration From")

LName=Label(root,text="Name*",font='Verdana 10 bold',pady=10,padx=20)
LName.place(x=80,y=100)
EName=Entry(bd=2,relief="raised",font='Verdana 10 bold',textvariable=namee)
EName.place(x=200,y=100,width=150,height=30)


LContact=Label(root,text="Contact*",font='Verdana 10 bold')
LContact.place(x=80,y=150)
EContact=Entry(bd=2,relief="raised",font='Verdana 10 bold',textvariable=contact)
EContact.place(x=200,y=150,width=150,height=30)


Label_Email=Label(root,text="Email*",font='Verdana 10 bold')
Label_Email.place(x=100,y=200)
Entry_Email=Entry(bd=2,relief="raised",font='Verdana 10 bold',textvariable=email)
Entry_Email.place(x=200,y=200,width=150,height=30)


LGender=Label(root,text="Gender*",font='Verdana 10 bold')
LGender.place(x=80,y=250)
RadioMale=Radiobutton(root,text="Male",value="Male",font='Verdana 10 bold',variable=gen)
RadioMale.place(x=180,y=250,width=100,height=30)
RadioFemale=Radiobutton(root,text="Female",value="Female",font='Verdana 10 bold',variable=gen)
RadioFemale.place(x=270,y=250,width=100,height=30)


LabelCity=Label(root,text="City*",font='Verdana 10 bold')
LabelCity.place(x=110,y=300)
LabelCity=Entry(bd=2,relief="raised",font='Verdana 10 bold',textvariable=city)
LabelCity.place(x=200,y=300,width=150,height=30)
options1 = [
    "Surat",
    "New Delhi",
    "Bengaluru",
    "Mumbai",
    "London",
    "Paris",
    "Rio",
    "Tokyo",
    "Bangkok",
    "Helsinki",
    "Nairobi",
    "istanbul"
]        
CityDropdown= OptionMenu( root,city , *options1)
CityDropdown.place(x=330,y=300,width=25,height=30)
  

LabelState=Label(root,text="State*",font='Verdana 10 bold')
LabelState.place(x=100,y=350)
LabelState=Entry(bd=2,relief="raised",font='Verdana 10 bold',textvariable=state)
LabelState.place(x=200,y=350,width=150,height=30)
options2 = [
    "Gujarat",
    "Delhi",
    "Karnataka",
    "Maharashtra",
    "UK",
    "France",
    "Brazil",
    "Japan",
    "Maryand",
    "Hong Kong",
    "Kenya",
    "Turkey"
]
StateDropdown = OptionMenu( root ,state, *options2)
StateDropdown.place(x=330,y=350,width=25,height=30)

RagisterButton=Button(text="Register",font='Verdana 10 bold',bg="orange",fg="black",bd=5,relief="raised",command=connect_databas)
RagisterButton.place(x=150,y=400,width=130,height=40)
       

root.mainloop()  