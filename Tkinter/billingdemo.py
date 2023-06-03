
from tkinter import *

class bill:
    def __init__ (self,root):
        self.root=root
        self.root.geometry("1920x1080")
        self.root.title("Billing Software")
        color="azure"
        title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=color,fg="navy blue",font=("Gadugi",30,"bold"),pady=2).pack(fill=X)

        # .................cutomer detail frame

        f1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("Gadugi",15,"bold"),fg="gold",bg=color)
        f1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(f1,text="Customer Name",bg=color,fg="navy blue",font=("Gadugi",18,"bold")).grid(row=0, column=0 ,padx=20,pady=5)
        cname_txt=Entry(f1,width=15,font="arial 15 ",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphn_lbl=Label(f1,text="Phone No.",bg=color,fg="navy blue",font=("Gadugi",18,"bold")).grid(row=0, column=2 ,padx=20,pady=5)
        cphn_txt=Entry(f1,width=15,font="arial 15 ",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        cbill_lbl=Label(f1,text="Bill Number",bg=color,fg="navy blue",font=("Gadugi",18,"bold")).grid(row=0, column=4 ,padx=20,pady=5)
        cbill_txt=Entry(f1,width=15,font="arial 15 ",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

        bill_btn=Button(f1,text="Search",width=10,bd=7,font=" arial 12 bold").grid(row=0,column=6,pady=10,padx=10)



        # box 1.................................. 1350x700 ..................................................................................................................................................................................................................................

        # Box 1.
        f2=LabelFrame(self.root,bd=10,relief=GROOVE,text="box 1",font=("Gadugi",15,"bold"),fg="gold",bg=color)
        f2.place(x=0,y=180,width=325,height=340)

        # 1.
        l1=Label(f2,text="Item 1",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=0,column=0,padx=10,pady=10)
        t1=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
        # 2.
        l2=Label(f2,text="Item 2",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=1,column=0,padx=10,pady=10)
        t2=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=5,padx=10)
        # 3.
        l3=Label(f2,text="Item 3",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=2,column=0,padx=10,pady=10)
        t3=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=5,padx=10)
        # 4.
        l4=Label(f2,text="Item 4",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=3,column=0,padx=10,pady=10)
        t4=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=3,column=1,pady=5,padx=10)
        # 5.
        l5=Label(f2,text="Item 5",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        t5=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=5,padx=10)
        # 6.
        l6=Label(f2,text="Item 6",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        t6=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=5,column=1,pady=5,padx=10)



        # box 2..............................................................................................................................................................................................................................................................

        f3=LabelFrame(self.root,bd=10,relief=GROOVE,text="box 2",font=("Gadugi",15,"bold"),fg="gold",bg=color)
        f3.place(x=310,y=180,width=325,height=340)


        # 1.
        # l1=Label(f2,text="Item 1",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        # t1=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
        # # 2.
        # l2=Label(f2,text="Item 2",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        # t2=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=5,padx=10)
        # # 3.
        # l3=Label(f2,text="Item 3",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        # t3=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=5,padx=10)
        # # 4.
        # l4=Label(f2,text="Item 4",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        # t4=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=3,column=1,pady=5,padx=10)
        # # 5.
        # l5=Label(f2,text="Item 5",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        # t5=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=5,padx=10)
        # # 6.
        # l6=Label(f2,text="Item 6",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        # t6=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=5,column=1,pady=5,padx=10)







        # bow 3...................................................................................................................................................................................................................................................................

        f4=LabelFrame(self.root,bd=10,relief=GROOVE,text="box 3",font=("Gadugi",15,"bold"),fg="gold",bg=color)
        f4.place(x=620,y=180,width=325,height=340)


        # # 1.
        # l1=Label(f2,text="Item 1",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        # t1=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
        # # 2.
        # l2=Label(f2,text="Item 2",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        # t2=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=5,padx=10)
        # # 3.
        # l3=Label(f2,text="Item 3",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        # t3=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=5,padx=10)
        # # 4.
        # l4=Label(f2,text="Item 4",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        # t4=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=3,column=1,pady=5,padx=10)
        # # 5.
        # l5=Label(f2,text="Item 5",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        # t5=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=5,padx=10)
        # # 6.
        # l6=Label(f2,text="Item 6",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        # t6=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=5,column=1,pady=5,padx=10)







        # Box 4..............................................................................................................................................................................................................................................................................
        f5=LabelFrame(self.root,bd=10,relief=GROOVE,text="Box 4",font=("Gadugi",15,"bold"),fg="gold",bg=color)
        f5.place(x=930,y=180,width=325,height=340)


        # # 1.
        # l1=Label(f2,text="Item 1",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        # t1=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
        # # 2.
        # l2=Label(f2,text="Item 2",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        # t2=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=5,padx=10)
        # # 3.
        # l3=Label(f2,text="Item 3",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        # t3=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=5,padx=10)
        # # 4.
        # l4=Label(f2,text="Item 4",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        # t4=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=3,column=1,pady=5,padx=10)
        # # 5.
        # l5=Label(f2,text="Item 5",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        # t5=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=5,padx=10)
        # # 6.
        # l6=Label(f2,text="Item 6",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        # t6=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=5,column=1,pady=5,padx=10)






        # Box 5...............................................................................................................................................................................................................................................................................
        f6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Box 5",font=("Gadugi",15,"bold"),fg="gold",bg=color)
        f6.place(x=1240,y=180,width=325,height=340)


        # # 1.
        # l1=Label(f2,text="Item 1",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        # t1=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
        # # 2.
        # l2=Label(f2,text="Item 2",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        # t2=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=5,padx=10)
        # # 3.
        # l3=Label(f2,text="Item 3",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        # t3=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=5,padx=10)
        # # 4.
        # l4=Label(f2,text="Item 4",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        # t4=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=3,column=1,pady=5,padx=10)
        # # 5.
        # l5=Label(f2,text="Item 5",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        # t5=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=5,padx=10)
        # # 6.
        # l6=Label(f2,text="Item 6",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        # t6=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=5,column=1,pady=5,padx=10)






        # Box 6..............................................................................................................................................................................................................................................................................
        f7=LabelFrame(self.root,bd=10,relief=GROOVE,text="Box 6",font=("Gadugi",15,"bold"),fg="gold",bg=color)
        f7.place(x=0,y=510,width=325,height=340)



        # l1=Label(f2,text="Item 1",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        # t1=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
        # # 2.
        # l2=Label(f2,text="Item 2",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        # t2=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=5,padx=10)
        # # 3.
        # l3=Label(f2,text="Item 3",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        # t3=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=5,padx=10)
        # # 4.
        # l4=Label(f2,text="Item 4",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        # t4=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=3,column=1,pady=5,padx=10)
        # # 5.
        # l5=Label(f2,text="Item 5",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        # t5=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=5,padx=10)
        # # 6.
        # l6=Label(f2,text="Item 6",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        # t6=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=5,column=1,pady=5,padx=10)





        
        # # Box 7.............................................................................................................................................................................................................................................................................
        f8=LabelFrame(self.root,bd=10,relief=GROOVE,text="Box 7",font=("Gadugi",15,"bold"),fg="gold",bg=color)
        f8.place(x=310,y=510,width=325,height=340)


        # 1.
        # l1=Label(f2,text="Item 1",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        # t1=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
        # # 2.
        # l2=Label(f2,text="Item 2",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        # t2=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=5,padx=10)
        # # 3.
        # l3=Label(f2,text="Item 3",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        # t3=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=5,padx=10)
        # # 4.
        # l4=Label(f2,text="Item 4",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        # t4=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=3,column=1,pady=5,padx=10)
        # # 5.
        # l5=Label(f2,text="Item 5",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        # t5=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=5,padx=10)
        # # 6.
        # l6=Label(f2,text="Item 6",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        # t6=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=5,column=1,pady=5,padx=10)




        
        # Box 8...............................................................................................................................................................................................................................................................................
        f9=LabelFrame(self.root,bd=10,relief=GROOVE,text="Box 8",font=("Gadugi",15,"bold"),fg="gold",bg=color)
        f9.place(x=620,y=510,width=325,height=340)



        # 1.
        # l1=Label(f2,text="Item 1",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        # t1=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
        # # 2.
        # l2=Label(f2,text="Item 2",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        # t2=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=5,padx=10)
        # # 3.
        # l3=Label(f2,text="Item 3",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        # t3=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=5,padx=10)
        # # 4.
        # l4=Label(f2,text="Item 4",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        # t4=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=3,column=1,pady=5,padx=10)
        # # 5.
        # l5=Label(f2,text="Item 5",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        # t5=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=5,padx=10)
        # # 6.
        # l6=Label(f2,text="Item 6",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        # t6=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=5,column=1,pady=5,padx=10)





        
        # Box 9...............................................................................................................................................................................................................................................................................
        f10=LabelFrame(self.root,bd=10,relief=GROOVE,text="Box 9",font=("Gadugi",15,"bold"),fg="gold",bg=color)
        f10.place(x=930,y=510,width=325,height=340)



        # 1.
        # l1=Label(f2,text="Item 1",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        # t1=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
        # # 2.
        # l2=Label(f2,text="Item 2",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        # t2=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=5,padx=10)
        # # 3.
        # l3=Label(f2,text="Item 3",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        # t3=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=5,padx=10)
        # # 4.
        # l4=Label(f2,text="Item 4",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        # t4=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=3,column=1,pady=5,padx=10)
        # # 5.
        # l5=Label(f2,text="Item 5",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        # t5=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=5,padx=10)
        # # 6.
        # l6=Label(f2,text="Item 6",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        # t6=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=5,column=1,pady=5,padx=10)




       
        # Box 10..............................................................................................................................................................................................................................................................................
        f11=LabelFrame(self.root,bd=10,relief=GROOVE,text="Box 10",font=("Gadugi",15,"bold"),fg="gold",bg=color)
        f11.place(x=1240,y=510,width=325,height=340)        

        # l1=Label(f2,text="Item 1",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        # t1=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
        # # 2.
        # l2=Label(f2,text="Item 2",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        # t2=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=5,padx=10)
        # # 3.
        # l3=Label(f2,text="Item 3",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        # t3=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=5,padx=10)
        # # 4.
        # l4=Label(f2,text="Item 4",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        # t4=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=3,column=1,pady=5,padx=10)
        # # 5.
        # l5=Label(f2,text="Item 5",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        # t5=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=5,padx=10)
        # # 6.
        # l6=Label(f2,text="Item 6",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        # t6=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=5,column=1,pady=5,padx=10)






 








        f100=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",font=("Gadugi",15,"bold"),fg="gold",bg=color)
        f100.place(x=0,y=850,relwidth=1,height=140)
















root=Tk()


# root.geometry("955x644")
# photo = PhotoImage(file="1.png")
# avni_label=Label(Image=photo)
# avni_label.pack()


obj = bill(root)

root.mainloop()
