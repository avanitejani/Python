
from tkinter import *

class bill:
    def __init__ (self,root):
        self.root=root
        self.root.geometry("1920x1080")
        self.root.title("Billing Software")
        color="azure"
        title=Label(self.root,text="Food Billing Software",bd=12,relief=GROOVE,bg=color,fg="navy blue",font=("Gadugi",30,"bold"),pady=2).pack(fill=X)

        # .................cutomer detail frame  azure

        f0=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("Gadugi",15,"bold"),fg="orange",bg=color)
        f0.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(f0,text="Customer Name",bg=color,fg="navy blue",font=("Gadugi",18,"bold")).grid(row=0, column=0 ,padx=20,pady=5)
        cname_txt=Entry(f0,width=15,font="arial 15 ",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphn_lbl=Label(f0,text="Phone No.",bg=color,fg="navy blue",font=("Gadugi",18,"bold")).grid(row=0, column=2 ,padx=20,pady=5)
        cphn_txt=Entry(f0,width=15,font="arial 15 ",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        cbill_lbl=Label(f0,text="Bill Number",bg=color,fg="navy blue",font=("Gadugi",18,"bold")).grid(row=0, column=4 ,padx=20,pady=5)
        cbill_txt=Entry(f0,width=15,font="arial 15 ",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

        bill_btn=Button(f0,text="Search/Enter",width=10,bd=7,font=" arial 12 bold").grid(row=0,column=6,pady=10,padx=10)


        bill_btn=Button(f0,text="Total",width=10,bd=7,font=" arial 12 bold").grid(row=0,column=7,pady=10,padx=10)
        bill_btn=Button(f0,text="Generate Bill",width=12,bd=7,font=" arial 12 bold").grid(row=0,column=8,pady=10,padx=10)
        bill_btn=Button(f0,text="Clear",width=10,bd=7,font=" arial 12 bold").grid(row=0,column=9,pady=10,padx=10)
        bill_btn=Button(f0,text="Exit",width=10,bd=7,font=" arial 12 bold").grid(row=0,column=10,pady=10,padx=10)




        # box 1.................................. 1350x700 ..................................................................................................................................................................................................................................

        # Box 1.
        f1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Breverages",font=("Gadugi",15,"bold"),fg="orange",bg=color)
        f1.place(x=0,y=180,width=325,height=340)

        # 1.
        l1=Label(f1,text="HotDrink",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=0,column=0,padx=10,pady=10)
        t1=Entry(f1,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
        # 2.
        l2=Label(f1,text="ColdDrink",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=1,column=0,padx=10,pady=10)
        t2=Entry(f1,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=5,padx=10)
        # 3.
        l3=Label(f1,text="Cocktails",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=2,column=0,padx=10,pady=10)
        t3=Entry(f1,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=5,padx=10)
        # 4
        l4=Label(f1,text="Alcoholics",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=3,column=0,padx=10,pady=10)
        t4=Entry(f1,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=3,column=1,pady=5,padx=10)
        # 5.
        l5=Label(f1,text="Spirits",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        t5=Entry(f1,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=5,padx=10)
        # 6.
        l6=Label(f1,text="Shaks",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        t6=Entry(f1,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=5,column=1,pady=5,padx=10)



        # box 2..............................................................................................................................................................................................................................................................

        f2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Dessert",font=("Gadugi",15,"bold"),fg="orange",bg=color)
        f2.place(x=310,y=180,width=325,height=340)


        # 1.
        l1=Label(f2,text="Cakes",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        t1=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
        # 2.
        l2=Label(f2,text="Donuts",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        t2=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=5,padx=10)
        # 3.
        l3=Label(f2,text="Custards",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        t3=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=5,padx=10)
        # 4.
        l4=Label(f2,text="Ice-Creams",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        t4=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=3,column=1,pady=5,padx=10)
        # 5.
        l5=Label(f2,text="Waffles",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        t5=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=5,padx=10)
        # 6.
        l6=Label(f2,text="Cookies",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        t6=Entry(f2,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=5,column=1,pady=5,padx=10)







        # bow 3...................................................................................................................................................................................................................................................................

        f3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Italian Food",font=("Gadugi",15,"bold"),fg="orange",bg=color)
        f3.place(x=620,y=180,width=325,height=340)


        # 1.
        l1=Label(f3,text="Pizza",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        t1=Entry(f3,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
        # 2.
        l2=Label(f3,text="Pasta",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        t2=Entry(f3,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=5,padx=10)
        # 3.
        l3=Label(f3,text="RedWine",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        t3=Entry(f3,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=5,padx=10)
        # 4.
        l4=Label(f3,text="Salads",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        t4=Entry(f3,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=3,column=1,pady=5,padx=10)
        # 5.
        l5=Label(f3,text="Tiramisu",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        t5=Entry(f3,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=5,padx=10)
        # 6.
        l6=Label(f3,text="Lasagna",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        t6=Entry(f3,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=5,column=1,pady=5,padx=10)







        # Box 4..............................................................................................................................................................................................................................................................................
        f4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bengali Food",font=("Gadugi",15,"bold"),fg="orange",bg=color)
        f4.place(x=930,y=180,width=325,height=340)


        # 1.
        l1=Label(f4,text="Shukto",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        t1=Entry(f4,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
        # 2.
        l2=Label(f4,text="Sandesh",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        t2=Entry(f4,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=5,padx=10)
        # 3.
        l3=Label(f4,text="AlurDom",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        t3=Entry(f4,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=5,padx=10)
        # 4.
        l4=Label(f4,text="Luchi",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        t4=Entry(f4,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=3,column=1,pady=5,padx=10)
        # 5.
        l5=Label(f4,text="MishtiDoi",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        t5=Entry(f4,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=5,padx=10)
        # 6.
        l6=Label(f4,text="Patishpata",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        t6=Entry(f4,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=5,column=1,pady=5,padx=10)






        # Box 5...............................................................................................................................................................................................................................................................................
        f5=LabelFrame(self.root,bd=10,relief=GROOVE,text="Chaines Food",font=("Gadugi",15,"bold"),fg="orange",bg=color)
        f5.place(x=1240,y=180,width=325,height=340)


        # 1.
        l1=Label(f5,text="ChowMein",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        t1=Entry(f5,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
        # 2.
        l2=Label(f5,text="SpringRolls",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        t2=Entry(f5,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=5,padx=10)
        # 3.
        l3=Label(f5,text="FriedRice",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        t3=Entry(f5,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=5,padx=10)
        # 4.
        l4=Label(f5,text="Soup",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        t4=Entry(f5,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=3,column=1,pady=5,padx=10)
        # 5.
        l5=Label(f5,text="Noodles",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        t5=Entry(f5,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=5,padx=10)
        # 6.
        l6=Label(f5,text="Manchurian",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        t6=Entry(f5,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=5,column=1,pady=5,padx=10)






        # Box 6..............................................................................................................................................................................................................................................................................
        f6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Vegan Food",font=("Gadugi",15,"bold"),fg="orange",bg=color)
        f6.place(x=0,y=510,width=325,height=340)



        l1=Label(f6,text="Fruits",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        t1=Entry(f6,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
        # 
        l2=Label(f6,text="Tofu",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        t2=Entry(f6,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=5,padx=10)
        # 3.
        l3=Label(f6,text="Oats",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        t3=Entry(f6,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=5,padx=10)
        # 4.
        l4=Label(f6,text="Tempeh",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        t4=Entry(f6,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=3,column=1,pady=5,padx=10)
        # 5.
        l5=Label(f6,text="Smoothies",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        t5=Entry(f6,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=5,padx=10)
        # 6.
        l6=Label(f6,text="Rice",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        t6=Entry(f6,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=5,column=1,pady=5,padx=10)





        
        # # Box 7.............................................................................................................................................................................................................................................................................
        f7=LabelFrame(self.root,bd=10,relief=GROOVE,text="south Indian Food",font=("Gadugi",15,"bold"),fg="orange",bg=color)
        f7.place(x=310,y=510,width=325,height=340)


        1.
        l1=Label(f7,text="Dosa",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        t1=Entry(f7,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
        # 2.
        l2=Label(f7,text="Idli",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        t2=Entry(f7,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=5,padx=10)
        # 3.
        l3=Label(f7,text="Appam",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        t3=Entry(f7,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=5,padx=10)
        # 4.
        l4=Label(f7,text="Upma",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        t4=Entry(f7,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=3,column=1,pady=5,padx=10)
        # 5.
        l5=Label(f7,text="Vada",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        t5=Entry(f7,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=5,padx=10)
        # 6.
        l6=Label(f7,text="Rasam",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        t6=Entry(f7,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=5,column=1,pady=5,padx=10)




        
        # Box 8...............................................................................................................................................................................................................................................................................
        f8=LabelFrame(self.root,bd=10,relief=GROOVE,text="Gujrati food",font=("Gadugi",15,"bold"),fg="orange",bg=color)
        f8.place(x=620,y=510,width=325,height=340)



        1.
        l1=Label(f8,text="Khandvi",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        t1=Entry(f8,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
        # 2.
        l2=Label(f8,text="Dhokla",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        t2=Entry(f8,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=5,padx=10)
        # 3.
        l3=Label(f8,text="Undhiyu",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        t3=Entry(f8,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=5,padx=10)
        # 4.
        l4=Label(f8,text="Thepla",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        t4=Entry(f8,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=3,column=1,pady=5,padx=10)
        # 5.
        l5=Label(f8,text="Patra",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        t5=Entry(f8,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=5,padx=10)
        # 6.
        l6=Label(f8,text="Shrikhand",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        t6=Entry(f8,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=5,column=1,pady=5,padx=10)





        
        # Box 9...............................................................................................................................................................................................................................................................................
        f9=LabelFrame(self.root,bd=10,relief=GROOVE,text="Maharashtra Food",font=("Gadugi",15,"bold"),fg="orange",bg=color)
        f9.place(x=930,y=510,width=325,height=340)



        1.
        l1=Label(f9,text="PavBhaji",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        t1=Entry(f9,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
        # 2.
        l2=Label(f9,text="VadaPav",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        t2=Entry(f9,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=5,padx=10)
        # 3.
        l3=Label(f9,text="MisalPav",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        t3=Entry(f9,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=5,padx=10)
        # 4.
        l4=Label(f9,text="Poha",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        t4=Entry(f9,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=3,column=1,pady=5,padx=10)
        # 5.
        l5=Label(f9,text="PuranPoli",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        t5=Entry(f9,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=5,padx=10)
        # 6.
        l6=Label(f9,text="Thalipeeth",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        t6=Entry(f9,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=5,column=1,pady=5,padx=10)




       
        # Box 10..............................................................................................................................................................................................................................................................................
        f10=LabelFrame(self.root,bd=10,relief=GROOVE,text="Punjabi Food",font=("Gadugi",15,"bold"),fg="orange",bg=color)
        f10.place(x=1240,y=510,width=325,height=340)        



        # 1
        l1=Label(f10,text="Lassi",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        t1=Entry(f10,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
        # 2.
        l2=Label(f10,text="choleBhature",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        t2=Entry(f10,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=5,padx=10)
        # 3.
        l3=Label(f10,text="Paratha",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        t3=Entry(f10,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=5,padx=10)
        # 4.
        l4=Label(f10,text="DalMakhani",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        t4=Entry(f10,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=3,column=1,pady=5,padx=10)
        # 5.
        l5=Label(f10,text="Pinni",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        t5=Entry(f10,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=5,padx=10)
        # 6.
        l6=Label(f10,text="PaneerTikka",font=("Gadugi",16,"bold"),bg=color,fg="navy blue").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        t6=Entry(f10,width=10,font=("Gadugi" ,16,"bold "),bd=5,relief=SUNKEN).grid(row=5,column=1,pady=5,padx=10)





    # end .....................................................................................................................................................................................................................................................................................
 
        f11=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",font=("Gadugi",15,"bold"),fg="orange",bg=color)
        f11.place(x=0,y=850,relwidth=1,height=140)


        
        l=Label(f11,text="Total Breverages",bg=color,fg="navy blue",font=("Gadugi",11,"bold")).grid(row=0, column=0 ,padx=0,pady=5)
        t=Entry(f11,width=6,font="arial 15 ",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=0)
        l=Label(f11,text="Breverages Tax",bg=color,fg="navy blue",font=("Gadugi",11,"bold")).grid(row=1, column=0 ,padx=0,pady=5)
        t=Entry(f11,width=6,font="arial 15 ",bd=7,relief=SUNKEN).grid(row=1,column=1,pady=5,padx=0)

        l=Label(f11,text="  Total Dessert",bg=color,fg="navy blue",font=("Gadugi",11,"bold")).grid(row=0, column=2 ,padx=0,pady=5)
        t=Entry(f11,width=6,font="arial 15 ",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=0)
        l=Label(f11,text="  Dessert Tax",bg=color,fg="navy blue",font=("Gadugi",11,"bold")).grid(row=1, column=2 ,padx=0,pady=5)
        t=Entry(f11,width=6,font="arial 15 ",bd=7,relief=SUNKEN).grid(row=1,column=3,pady=5,padx=0)

        l=Label(f11,text='''  Total Italian''',bg=color,fg="navy blue",font=("Gadugi",11,"bold")).grid(row=0, column=4 ,padx=0,pady=5)
        t=Entry(f11,width=6,font="arial 15 ",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=0)
        l=Label(f11,text="  Italian Tax",bg=color,fg="navy blue",font=("Gadugi",11,"bold")).grid(row=1, column=4 ,padx=0,pady=5)
        t=Entry(f11,width=6,font="arial 15 ",bd=7,relief=SUNKEN).grid(row=1,column=5,pady=5,padx=0)

        l=Label(f11,text='''  Total Bengali''',bg=color,fg="navy blue",font=("Gadugi",11,"bold")).grid(row=0, column=6 ,padx=0,pady=5)
        t=Entry(f11,width=6,font="arial 15 ",bd=7,relief=SUNKEN).grid(row=0,column=7,pady=5,padx=0)
        l=Label(f11,text="  Bengali Tax",bg=color,fg="navy blue",font=("Gadugi",11,"bold")).grid(row=1, column=6 ,padx=0,pady=5)
        t=Entry(f11,width=6,font="arial 15 ",bd=7,relief=SUNKEN).grid(row=1,column=7,pady=5,padx=0)

        l=Label(f11,text='''  Total Chaines''',bg=color,fg="navy blue",font=("Gadugi",11,"bold")).grid(row=0, column=8 ,padx=0,pady=5)
        t=Entry(f11,width=6,font="arial 15 ",bd=7,relief=SUNKEN).grid(row=0,column=9,pady=5,padx=0)
        l=Label(f11,text="  Chaines Tax",bg=color,fg="navy blue",font=("Gadugi",11,"bold")).grid(row=1, column=8 ,padx=0,pady=5)
        t=Entry(f11,width=6,font="arial 15 ",bd=7,relief=SUNKEN).grid(row=1,column=9,pady=5,padx=0)

        l=Label(f11,text="  Total Vegan",bg=color,fg="navy blue",font=("Gadugi",11,"bold")).grid(row=0, column=10 ,padx=0,pady=5)
        t=Entry(f11,width=6,font="arial 15 ",bd=7,relief=SUNKEN).grid(row=0,column=11,pady=5,padx=0)
        l=Label(f11,text="  Vegan Tax",bg=color,fg="navy blue",font=("Gadugi",11,"bold")).grid(row=1, column=10 ,padx=0,pady=5)
        t=Entry(f11,width=6,font="arial 15 ",bd=7,relief=SUNKEN).grid(row=1,column=11,pady=5,padx=0)

        l=Label(f11,text="  Total South",bg=color,fg="navy blue",font=("Gadugi",11,"bold")).grid(row=0, column=12 ,padx=0,pady=5)
        t=Entry(f11,width=6,font="arial 15 ",bd=7,relief=SUNKEN).grid(row=0,column=13,pady=5,padx=0)
        l=Label(f11,text="  South Tax",bg=color,fg="navy blue",font=("Gadugi",11,"bold")).grid(row=1, column=12 ,padx=0,pady=5)
        t=Entry(f11,width=6,font="arial 15 ",bd=7,relief=SUNKEN).grid(row=1,column=13,pady=5,padx=0)

        l=Label(f11,text="  Total Gujrati",bg=color,fg="navy blue",font=("Gadugi",11,"bold")).grid(row=0, column=14 ,padx=0,pady=5)
        t=Entry(f11,width=6,font="arial 15 ",bd=7,relief=SUNKEN).grid(row=0,column=15,pady=5,padx=0)
        l=Label(f11,text="  Gujrati Tax",bg=color,fg="navy blue",font=("Gadugi",11,"bold")).grid(row=1, column=14 ,padx=0,pady=5)
        t=Entry(f11,width=6,font="arial 15 ",bd=7,relief=SUNKEN).grid(row=1,column=15,pady=5,padx=0)

        l=Label(f11,text="  Total Marathi",bg=color,fg="navy blue",font=("Gadugi",11,"bold")).grid(row=0, column=16 ,padx=0,pady=5)
        t=Entry(f11,width=6,font="arial 15 ",bd=7,relief=SUNKEN).grid(row=0,column=17,pady=5,padx=0)
        l=Label(f11,text="  Marathi Tax",bg=color,fg="navy blue",font=("Gadugi",11,"bold")).grid(row=1, column=16 ,padx=0,pady=5)
        t=Entry(f11,width=6,font="arial 15 ",bd=7,relief=SUNKEN).grid(row=1,column=17,pady=5,padx=0)

        l=Label(f11,text="  Total Punjabi",bg=color,fg="navy blue",font=("Gadugi",11,"bold")).grid(row=0, column=18 ,padx=0,pady=5)
        t=Entry(f11,width=6,font="arial 15 ",bd=7,relief=SUNKEN).grid(row=0,column=19,pady=5,padx=0)
        l=Label(f11,text="  Punjabi Tax",bg=color,fg="navy blue",font=("Gadugi",11,"bold")).grid(row=1, column=18 ,padx=0,pady=5)
        t=Entry(f11,width=6,font="arial 15 ",bd=7,relief=SUNKEN).grid(row=1,column=19,pady=5,padx=0)




    # Bill Area ..............................................................................................................

       
                  
        # F12=Frame(self.root,bd=10, relief=GROOVE)
        # F12.place(x=1010,y=180,width=350,height=380)
        # bill_title=Label (F12, text="Bill Area", font="arial 15 bold", bd=7,relief=-GROOVE).pack(fill=X) 
        # scrol_y=Scrollbar (F12, orient=VERTICAL)
        # self.txtarea-Text (F12,yscrollcommand=scrol_y.set)
        # scrol_y.pack(side=RIGHT, fill=Y)
        # scrol_y.config(command=self.txtarea.yview)
        # self.txtarea.pack (fill=BOTH, expand=1)

        f12=Frame(self.root,bd=10,relief=GROOVE,bg=color)
        f12.place(x=1565,y=180,width=350,height=670)
        bill_title=Label (f12, text="Bill Area", font="arial 15 bold",fg="navy blue",bg=color, bd=7,relief=GROOVE).pack(fill=X) 
        # scrol_y=Scrollbar (f12, orient=VERTICAL)
        # self.txtarea-Text (f12,yscrollcommand=scrol_y.set)
        # scrol_y.pack(side=RIGHT, fill=Y)
        # scrol_y.config(command=self.txtarea.yview)
        # self.txtarea.pack (fill=BOTH, expand=1)
        

root=Tk()


# root.geometry("955x644")
# photo = PhotoImage(file="1.png")
# avni_label=Label(Image=photo)
# avni_label.pack()


obj = bill(root)

root.mainloop()
