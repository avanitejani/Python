from tkinter import *  

root=Tk()
root.geometry("500x300")

l1 = Label(text="TOP",font=("Algerian 11 bold"), bg="grey", fg="black", padx=60,pady=12)
l2 = Label(text="RIGHT",font=("Algerian 11 bold"), bg="azure", fg="blue", pady=60)
l3 = Label(text="BOTTOM",font=("Algerian 11 bold"), bg="pink", fg="maroon", pady=12)
l4 = Label(text="LEFT", font=("Verdana 11 bold"),bg="lavender", fg="purple", padx=5)


l1.pack(anchor="n", side="top", fill="x", padx=5 )
l1.pack(anchor="n", side="top", fill="x", padx=5)
l2.pack(anchor="e", side="right", fill="y", padx=20)
l3.pack(anchor="s", side="bottom", fill="x", padx=0.20)
l4.pack(anchor="w", side="left", fill="y", pady=10)



root.mainloop()
