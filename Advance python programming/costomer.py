
from tkinter import *
root=Tk()
root.geometry('430x550')

def add_stock():

    name = name_entry.get()

    name_entry.delete(0, END)
    quantity_entry.delete(0,END)




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
    # file=open("data.txt","a")
    print(f"\n\n name Of Product: {name.get()}\n Quantity Of Product:{quan.get()}\n Price of Product:{totalq.get()}\n  Total Price    :{total_all.get()}")


# Create the "Add Stock" section

name_label=Label(root,text="product Name",font='Verdana 10 bold',pady=10,padx=20)
name_label.place(x=60,y=100)
name_entry=Entry(bd=2,relief="raised",font='Verdana 10 bold',textvariable=name)
name_entry.place(x=200,y=100,width=150,height=30)

quantity_label=Label(root,text="Quantity",font='Verdana 10 bold')
quantity_label.place(x=80,y=150)
quantity_entry=Entry(bd=2,relief="raised",font='Verdana 10 bold',textvariable=quan)
quantity_entry.place(x=200,y=150,width=150,height=30)

total_lbl=Label(root,text="Price ",font='Verdana 10 bold')
total_lbl.place(x=80,y=200)
total_lbl=Entry(bd=2,relief="raised",font='Verdana 10 bold',textvariable=totalq)
total_lbl.place(x=200,y=200,width=150,height=30)

total_price=Label(root,text="total Cost",font='Verdana 10 bold')
total_price.place(x=80,y=250)
total_price=Entry(bd=2,relief="raised",font='Verdana 10 bold',textvariable=total_all)
total_price.place(x=200,y=250,width=150,height=30)

# Create the "delete Stock" button

add_stock_button=Button(text="purchase",font='Verdana 10 bold',bg="orange",fg="black",bd=5,relief="raised",command=total)
add_stock_button.place(x=150,y=300,width=130,height=40)




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

