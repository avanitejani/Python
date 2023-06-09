# from tkinter import *
# root=Tk()
# root.geometry("430x500")

print('''
1. Product Manager
2. Customer
''')

role=int(input("select a number :"))
if role == 1:
	print("Enter A Choice by Product Manager : ")
    
	pm=('\n1. Can Register \n2. Can Login \n3. Can manage all product stocks\n4. Can View all stocks')

	while True:

		print(pm)
		role1=int(input("Enter A Choice by A Number : "))
		if role1 == 1:
			print("you selected Register ")
			from registrestion_from import *
			
		elif role1 == 2:
			print("you selected Login ")
			from singup import *

		elif role1 == 3:
			print("you selected manage all product stocks ")
			from ProductManager import *
			

		elif role1 == 4:
			print("you selected View all stocks ")
			pass


elif role == 2:
	print("Enter A Choice by Customer :" )
	Customer=('\n1. Can register \n2. Can Login \n3. Can purchase stock \n4. Can view all orders')
	print(Customer)
	role2=int(input("Enter A Choice A Number : "))
	if role2 == 1:
		print("you selected Register ")
		from registrestion_from import *

	elif role2 == 2:
		print("you selected Login ")
		from singup import *

	elif role2 == 3:
		print("you selected purchase stock ")
		from costomer import *

	elif role2 == 4:
		print("you selected View all stocks ")
		pass







