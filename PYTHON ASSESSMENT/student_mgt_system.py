from Counselor import *
from faculty import *
from student import *

print("""
Press 1 for Counselor
Press 2 for Faculty
Press 3 for Student
Press 4 For Go To Exit
""")



role=int(input("Enter A Role ID : "))
if role == 1:

    cons=("""
    1. Add Student
    2. Remove Student
    3. View All Student
    4. View Specific Student
    5. exit
    """)

    while True:

        print(cons)
        C_choice=int(input("Enter A Choice by Counsellor : "))
        if C_choice == 1:
            add_student()
            select=input("Do you want to perform more oiptions? ( press y or n) : ")
            if select == 'y': 
                continue
            elif select == 'n':
                # print("Over Counsellor") 
                print(all_record)
                break
        
        elif C_choice == 2:
            remove_student()
            select=input("Do you want to perform more oiptions? ( press y or n)  : ")
            if select == 'y': 
                continue
            elif select == 'n':  
                # print("Over Counsellor")
                print(all_record)
                break

        elif C_choice == 3:
            view_all_student()
            select=input("Do you want to perform more oiptions? ( press y or n) : ")
            if select == 'y':  
                continue
            elif select == 'n': 
                # print("Over Counsellor")
                print(all_record)
                break

        elif C_choice == 4:
            view_sepcific_student()
            select=input("Do you want to perform more oiptions? ( press y or n): ")
            if select == 'y':  
                continue
            elif select == 'n':  
                # print("Over Counsellor")
                print(all_record)
                break

        elif C_choice == 5:
            print("now you exit ")

        else:
            print("Counsellor")
        


elif role == 2:
    fac=('''
    1.Add Mark To Student
    2.View All Student
    ''')

    while True:
        print(fac)
        f_Choice=int(input("Enter A Choice by Faculty : "))
        if f_Choice == 1:
            Add_mark_student()
            select=input("Do you want to perform more oiptions? ( press y or n) : : ")
            if select == 'y':
                continue
            elif select == 'n':
                break
        elif f_Choice == 2:
            View_All_Student()
            select=input("Do you want to perform more oiptions? ( press y or n) : : ")
            if select == 'y':
                continue
            elif select == 'n':
                break



elif role == 3:
    stu=("""
    1. student_derails
    2. student_parents
    """) 
    while True:
        print(stu)   
        s_choice=int(input("Enter A Choice by Student"))
        if s_choice == 1:
            student_details()
            select=input("Do you want to perform more oiptions? ( press y or n) : : ")
            if select == 'y':
                continue
            elif select == 'n':
                break

        elif s_choice == 2:
            student_parents()
            select=input("Do you want to perform more oiptions? ( press y or n) : : ")
            if select == 'y':
                continue
            elif select == 'n':
                break




elif role == 4:
        while True:
            print("Thank You For Visit.")
            break        

 