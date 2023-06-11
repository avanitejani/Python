from Counselor import *  # ------------------ import counselor file
from faculty import *  # -------------------- import counselor file
from student import *  # -------------------- import counselor file

print("""               
Press 1 for Counselor
Press 2 for Faculty
Press 3 for Student
Press 4 For Go To Exit
""")       #----------------------------------- print massage in student management system



role=int(input("Enter A Role ID : "))
if role == 1:

    cons=("""
    1. Add Student
    2. Remove Student
    3. View All Student
    4. View Specific Student
    5. exit
    """)    #------------------------------------ print massage for Counselor

    while True:

        print(cons)
        C_choice=int(input("Enter A Choice by Counsellor : "))

        if C_choice == 1:   # ------------------  if user select 1 to perform add student
            add_student()   # ------------------- import counselor in add student
            select=input("Do you want to perform more oiptions? ( press y or n) : ")
            if select == 'y': 
                continue
            elif select == 'n':
                print(all_record)
                break
        
        elif C_choice == 2:  # ------------------  if user select 2 to perform remove student
            remove_student() # ------------------- import counselor in Rmove student
            select=input("Do you want to perform more oiptions? ( press y or n)  : ")
            if select == 'y': 
                continue
            elif select == 'n':  
                print(all_record)
                break

        elif C_choice == 3:  # ------------------  if user select 3 to perform view all student
            view_all_student() # ----------------- import counselor in view all student
            select=input("Do you want to perform more oiptions? ( press y or n) : ")
            if select == 'y':  
                continue
            elif select == 'n': 
                # print("Over Counsellor")
                print(all_record)
                break

        elif C_choice == 4:  # -------------------- if user select 4 to perform viwe sepcific student
            view_sepcific_student() # ------------- import counselor in viwe sepcific student
            select=input("Do you want to perform more oiptions? ( press y or n): ")
            if select == 'y':  
                continue
            elif select == 'n':  
                # print("Over Counsellor")
                print(all_record)
                break

        elif C_choice == 5:  # --------------------  if user select 5 to Exit
            print("now you exit ")

        else:
            print("Counsellor")
        


elif role == 2:
    fac=('''
    1.Add Mark To Student
    2.View All Student
    ''')   #---------------------------------------- print massage for Faculty

    while True:
        print(fac)
        f_Choice=int(input("Enter A Choice by Faculty : "))
        if f_Choice == 1:   # ---------------------- if user select 1 to perform Add Mark To Student
            Add_mark_student() # ------------------- import Faculty in Add Mark To student
            select=input("Do you want to perform more oiptions? ( press y or n) : : ")
            if select == 'y':
                continue
            elif select == 'n':
                break
        elif f_Choice == 2:  # --------------------- if user select 2 to perform View All Student
            View_All_Student() # ------------------- import Faculty in View All student
            select=input("Do you want to perform more oiptions? ( press y or n) : : ")
            if select == 'y':
                continue
            elif select == 'n':
                break



elif role == 3:  
    stu=("""
    1. Student Derails
    2. Student Parents
    """)    #---------------------------------------- print massage for Student

    while True:
        print(stu)   
        s_choice=int(input("Enter A Choice by Student"))
        if s_choice == 1:  # ------------------------ if user select 1 to perform Student Derails
            student_details() # --------------------- import Student in add Student Derails
            select=input("Do you want to perform more oiptions? ( press y or n) : : ")
            if select == 'y':
                continue
            elif select == 'n':
                break

        elif s_choice == 2:  # ---------------------- if user select 2 to perform student Parents
            student_parents() # --------------------- import Student in add student Parents
            select=input("Do you want to perform more oiptions? ( press y or n) : : ")
            if select == 'y':
                continue
            elif select == 'n':
                break




elif role == 4:       # ----------------------------- if user select 4 to Exit
        while True:
            print("Thank You For Visit.")
            break        

 