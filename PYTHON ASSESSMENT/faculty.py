from Counselor import *  #------------------------------------------------- import conselor

def Add_mark_student():  #------------------------------------------------- creatc fuction for Add mark student
    while True:
        user_choice=int(input("select Your Serial Number : "))
        if user_choice in all_record.keys():
            U_Subject=input("Enter Subject :")
            if U_Subject in all_record[user_choice]["Subject"]:
                u_marks=int(input("Enter A Add Marks :")) #---------------  Enterd marks
                position=all_record[user_choice]["Subject"].index(U_Subject)
                all_record[user_choice]["Marks"][position]+=u_marks
                print(f"Add Marks : {all_record}")
        
        else:
            print("Student not exiesting your list")

def View_All_Student(): #------------------------------------------------- creatc fuction for View All Student
    for student in all_record:
        print(f"All Student Serial Number : {student}")   #---------------  print all data
        print("First Name--------------")
        print(all_record[student]["First_Name"])
        print("Last Name--------------")
        print(all_record[student]["Last_Name"])
        print("Contact Number--------------")
        print(all_record[student]["Countect_Number"])
        print("Subject--------------")
        print(all_record[student]["Subject"])
        print("Marks--------------")
        print(all_record[student]["Marks"])
        print("Fees--------------")
        print(all_record[student]["Fees"])
        print("----------------------------------\n")
