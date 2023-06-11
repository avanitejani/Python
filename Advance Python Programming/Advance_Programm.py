# from tkinter import *
# root=Tk()
# root.geometry("430x500")

print('''
1. Product Manager
2. Customer
''') #---------------------------------------------- print massage to managr and customer


role=int(input("select a number :"))
if role == 1:
	print("Enter A Choice by Product Manager : ")
    
	pm=('\n1. Can Register \n2. Can Login \n3. Can manage all product stocks\n4. Can View all stocks')

	while True:

		print(pm)
		role1=int(input("Enter A Choice by A Number : "))
		if role1 == 1:  # -------------------------  if user select 1 to perform Register
			print("you selected Register ")
			from registrestion_from import * # ----  import registrestion_from file
			
		elif role1 == 2: # ------------------------  if user select 2 to perform Login
			print("you selected Login ")
			from singup import * # ----------------  import singup file

		elif role1 == 3: # ------------------------  if user select 3 to perform manage all product stocks
			print("you selected manage all product stocks ")
			from ProductManager import *  #--------  import ProductManager file
			

		elif role1 == 4: # ------------------------  if user select 4 to View all stocks
			print("you selected View all stocks ")
			from ProductManager import * # --------  import ProductManager file
			showdata() # --------------------------  import showdata


elif role == 2:
		
	while True:

		print("Enter A Choice by Customer :" )
		Customer=('\n1. Can register \n2. Can Login \n3. Can purchase stock \n4. Can view all orders')
		print(Customer)
		role2=int(input("Enter A Choice A Number : "))
		if role2 == 1: # -------------------------  if user select 1 to perform Register
			print("you selected Register ")
			from registrestion_from import * # ----  import registrestion_from file

		elif role2 == 2: # -----------------------  if user select 2 to perform Login
			print("you selected Login ")
			from singup import *  # --------------  import singup file

		elif role2 == 3: # -----------------------  if user select 3 to perform purchase stock
			print("you selected purchase stock ")
			from costomer import *  # ------------  import costomer file

		elif role2 == 4: # -----------------------  if user select 4 to perform View all stocks
			print("you selected View all stocks ")
			from costomer import *  # ------------  import costomer file
			showdata() # -------------------------  import showdata
			







