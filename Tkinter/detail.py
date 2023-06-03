from tkinter import *
root = Tk()
root.geometry("500x500")

age = StringVar()

e1 = Entry(root,textvariable=age)
e1.pack()

root.mainloop()
