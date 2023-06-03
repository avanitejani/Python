from tkinter import *
root=Tk()

root.geometry("430x500")
name=StringVar()
contect=IntVar()
email=StringVar()

# def showdata():
#     file=open("data.txt","a")
#     file.write(f"name: {name.get()}\nage:{contect.get()}\nemail:{email.get()}")

l0 = Label(text="Please Enter details below",font=("Gadugi"), bg="orange", fg="white", padx=60,pady=12)
l0.pack(anchor="n", side="top", fill="x", padx=5)


l1=Label(root,text="Name",pady=10,padx=20)
# l1.pack()
l1.grid(row=1,column=1)

t1 = Entry(root, textvariable=name)
# t1.pack()
t1.grid(row=1,column=2)




l2 = Label(root, text="Contect", pady=10, padx=20)
# l1.pack()
l2.grid(row=2,column=1)       

t2 = Entry(root, textvariable=contect)
# t1.pack()
t2.grid(row=2,column=2)




l3 = Label(root, text="Email", pady=10, padx=20)
# l1.pack()
l3.grid(row=3,column=1)

t3 = Entry(root, textvariable=email)
# t1.pack()
t3.grid(row=3,column=2)


root.mainloop()  