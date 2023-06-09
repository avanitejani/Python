# # pip install mysql-connector 


# import mysql.connector

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="demo"
# )
# rollno=int(input("Enter Rollno: "))
# age=int(input("Enter Age: "))
# namee=input("Enter Name: ")
# email=input("Enter Email: ")
# mobile=input("Enter mobile: ")
# mycursor = mydb.cursor()
# query=f"""use demo"""
# mycursor.execute(query)


# mycursor = mydb.cursor()
# query=f"""create table student
# (
# rollno int auto_increment,
# namee varchar(20),
# email varchar(20),
# age int,
# mobail  varchar(20),
# primary key (rollno)
# )
# """


# mycursor.execute(query)
# mycursor = mydb.cursor()
# query=f"""insert into student values({rollno},"{namee}","{email}",{age},"{mobile}")"""
# mycursor.execute(query)

# mydb.commit()

# pip install mysql-connector 


import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="")
    
# mycursor = mydb.cursor()
# query=f"""create database office"""
# mycursor.execute(query)2


rollno=int(input("Enter Rollno: "))
age=int(input("Enter Age: "))
namee=input("Enter Name: ")
email=input("Enter Email: ")
mobile=input("Enter mobile: ")

mycursor = mydb.cursor()
query=f"""use office"""
mycursor.execute(query)

mycursor = mydb.cursor()
query=f"""create table user
(
rollno int auto_increment,
namee varchar(20),
email varchar(20),
age int,
mobail  varchar(20),
primary key (rollno)
)
"""


mycursor.execute(query)
mycursor = mydb.cursor()
query=f"""insert into user values({rollno},"{namee}","{email}",{age},"{mobile}")"""
mycursor.execute(query)

mydb.commit()