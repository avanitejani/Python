# print("1.pizza    price = 150rs/pcs\n")
# print("2.burger   price = 70rs/pcs\n")
# print("3.dosa     price = 100rs/pcs\n")
# print("4.idli     price = 50rs/pcs\n")
# print("4.cake     price = 150rs/pcs\n")
    

# print=int(input("enter your choice  :"))
# choise = 0
# quantity = 0

# if (choise == 1):
#     print("you have selected pizza \n")
    

# elif (choise == 2):
#     print("you have selected burger \n")
# elif (choise == 3):
#     print("you have selected dosa \n")
# elif (choise == 4):
#     print("you have selected burger \n")
# elif (choise == 5):
#     print("you have selected idli \n")

# print=int(input("enter Quantity: \n"))    

# if (choise == 1):
#     amount = quantity * 150
    
# elif (choise == 2):
#     amount = quantity * 70

# elif (choise == 3):
#     amount = quantity * 100

# elif (choise == 4):
#     amount = quantity * 50

# elif (choise == 5):
#     amount = quantity * 150

# total_amount=0
# option=0
# total_amount += amount 
# print("\n amount = %d \n", amount)
# print("total_amount = %d \n", total_amount)
# print=input(" do you want to plce more oders? y or n :\n")
    

# if (option == 'y'):
#     print("start")
# else:
#     print("total bill is %d \n", total_amount)
#     print("visit again \n")

# print("press 1 for Counsellor")
# print("press 2 for Faculty")
# print("press 3 for Student")

# choise = 0
# print=int(input("Enter a role id: :"))

# if (choise == 1):
#     print("Enter a role id: 1")
# print("1. Add Student")
# print("2. Remove Student")
# print("3.view All Student")
# print("3.view Specific Student")

# class rectangle:


import datetime
str1="Wellcome To Food cafe"
# print(str1.center(50))
name=input("Enter Your Name :")
bill_num=int(input("Enter bill number : "))
item='''
    No.\t\tFood Item\t\tPrice
    1.\t\t sendwich \t\t180.00
    2.\t\t pizaa \t\t\t210.00
    3.\t\t Waffles \t\t150.00
    4.\t\t cheeseCake \t\t250.00
    5.\t\t coffee \t\t150.00
    6.\t\t French Fries \t\t200.00
    7.\t\t Burger \t\t120.00
    8.\t\t Ice-cream \t\t150.00
    9.\t\t Coctail \t\t200.00
    10.\t\tExit
    
'''
data={}
while True:
    print(item)
    net_amount=0

    s_item=int(input("Enter A Select food Item in Number : "))
    if s_item == 1:
        print("Thank You For Your Order\n You Have Selected sendwich.")
        q1=int(input("Enter A Quntity : "))
        amount1= q1 * 180.00
        print(f"\nAmount is {amount1}")
        net_amount+=amount1
        if "item1" in data.keys():
            data["item1"]["quntity"]+=q1
            data["item1"]["amount"]+=amount1
        else:
            data.update({"item1":{"quntity":q1,"amount":amount1}})
    elif s_item == 2:
        print("Thank You For Your Order\n You Have Selected pizaa.")
        q2=int(input("Enter A Quntity : "))
        amount2= q2 * 210.00
        print(f"\nAmount is {amount2}")
        net_amount+=amount2
        if "item2" in data.keys():
            data["item2"]["quntity"]+=q2
            data["item2"]["amount"]+=amount2
        else:
            data.update({"item2":{"quntity":q2,"amount":amount2}})
    elif s_item == 3:
        print("Thank You For Your Order\n You Have Selected Waffles.")
        q3=int(input("Enter A Quntity : "))
        amount3= q3 * 150.00
        print(f"\nAmount is {amount3}")
        net_amount+=amount3
        if "item3" in data.keys():
            data["item3"]["quntity"]+=q3
            data["item3"]["amount"]+=amount3
        else:
            data.update({"item3":{"quntity":q3,"amount":amount3}})
    elif s_item == 4:
        print("Thank You For Your Order\n You Have Selected CheeseCake.")
        q4=int(input("Enter A Quntity : "))
        amount4= q4 * 250.00
        print(f"\nAmount is {amount4}")
        net_amount+=amount4
        if "item4" in data.keys():
            data["item4"]["quntity"]+=q4
            data["item4"]["amount"]+=amount4
        else:
            data.update({"item4":{"quntity":q4,"amount":amount4}})
    elif s_item == 5:
        print("Thank You For Your Order\n You Have Selected coffee.")
        q5=int(input("Enter A Quntity : "))
        amount5= q5 * 200.00
        print(f"\nAmount is {amount5}")
        net_amount+=amount5
        if "item5" in data.keys():
            data["item5"]["quntity"]+=q5
            data["item5"]["amount"]+=amount5
        else:
            data.update({"item5":{"quntity":q5,"amount":amount5}})
    elif s_item == 6:
        print("Thank You For Your Order\n You Have Selected French Fries.")
        q5=int(input("Enter A Quntity : "))
        amount5= q5 * 200.00
        print(f"\nAmount is {amount5}")
        net_amount+=amount5
        if "item5" in data.keys():
            data["item5"]["quntity"]+=q5
            data["item5"]["amount"]+=amount5
        else:
            data.update({"item5":{"quntity":q5,"amount":amount5}})
    elif s_item == 7:
        print("Thank You For Your Order\n You Have Selected Burger.")
        q5=int(input("Enter A Quntity : "))
        amount5= q5 * 120.00
        print(f"\nAmount is {amount5}")
        net_amount+=amount5
        if "item5" in data.keys():
            data["item5"]["quntity"]+=q5
            data["item5"]["amount"]+=amount5
        else:
            data.update({"item5":{"quntity":q5,"amount":amount5}})
    elif s_item == 8:
        print("Thank You For Your Order\n You Have Selected Ice-cream.")
        q5=int(input("Enter A Quntity : "))
        amount5= q5 * 150.00
        print(f"\nAmount is {amount5}")
        net_amount+=amount5
        if "item5" in data.keys():
            data["item5"]["quntity"]+=q5
            data["item5"]["amount"]+=amount5
        else:
            data.update({"item5":{"quntity":q5,"amount":amount5}})
    elif s_item == 9:
        print("Thank You For Your Order\n You Have Selected Coctail.")
        q5=int(input("Enter A Quntity : "))
        amount5= q5 * 200.00
        print(f"\nAmount is {amount5}")
        net_amount+=amount5
        if "item5" in data.keys():
            data["item5"]["quntity"]+=q5
            data["item5"]["amount"]+=amount5
        else:
            data.update({"item5":{"quntity":q5,"amount":amount5}})
    
    elif s_item == 10:
        print("Thank You For Visit.")
        break
print(data)
file=open("Total Bill.txt","a")
keys_all=data.keys()
final_amount=0
for i in keys_all:
    main_data=data[i]
    final_amount+=main_data["amount"]
print(file.write("\n\nWellcome To Food cafe\n"))
x=datetime.datetime.now()
print(file.write(x.strftime("%Y/%B/%d,%H:%M:%S\n")))
print(file.write (f"Customer Name : {name}\n"))
print(file.write(f"Bill No. : {bill_num}\n"))
print(file.write("--------------------------------------------------------\n"))

print(file.write("food item\t\t\tqun\t\t\tamount\n"))

print(file.write("--------------------------------------------------------\n"))
for i in keys_all:
    main_data=data[i]
    q=data[i]["quntity"]
    a=data[i]["amount"]
    print(file.write(f"{i}\t\t\t{q}\t\t\t{a}\n"))
print(file.write("--------------------------------------------------------\n"))
print(file.write("--------------------------------------------------------\n"))
print(file.write(f"Total  amount : {final_amount}\n"))

file.close()
    
