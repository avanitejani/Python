# from counsellor import *
from Counselor import *
from faculty import *
from student import *

print("""
Press 1 for Counselor
Press 2 for Faculty
Press 3 for Student
Press 4 For To Exit
""")

# print(item)
role=int(input("Enter A Role ID : "))
if role == 1:

# def counsellor():
    print("""
    1. Add Student
    2. Remove Student
    3. View All Student
    4. View Specific Student
    5. exit
    """)
    c_choice=int(input("Enter a choice by counsellor: "))
    if c_choice==1:

        choice=int(input("Enter  a choice by add student: "))
        if choice==1:
            add_student()
            yn=input("Press Y for yes and N for no : ")
            if yn == 'y':  #user 'y' for yes to continue to program
                add_student()
            elif yn == 'n':  #uesr 'n' for no to break to program
                print(all_record)
                # counsellor()

        choice=int(input("Enter 2 a choice by Remove Student: "))
        if choice==2:
            remove_student()
            yn=input("Press Y for yes and N for no : ")
            if yn == 'y':  #user 'y' for yes to continue to program
                remove_student()
            elif yn == 'n':  #uesr 'n' for no to break to program
                print(all_record)
                # counsellor()

        choice=int(input("Enter a choice by View All Student: "))
        if choice==3:
            view_all_student()
            if yn == 'y':  #user 'y' for yes to continue to program
                view_all_student()
            elif yn == 'n':  #uesr 'n' for no to break to program
                print(all_record)
                # counsellor()

        choice=int(input("Enter a choice by View Specific Student: "))
        if choice==4:
            view_sepcific_student()
            if yn == 'y':  #user 'y' for yes to continue to program
                view_sepcific_student()
            elif yn == 'n':  #uesr 'n' for no to break to program
                print(all_record)
                # counsellor() 
    else:
        print("Enter Correct Choice")

def faculty():
    print("""
    1. faculty detail
    2. head faculty
    """)
    c_choice=int(input("Enter a  choice by faculty "))
    if c_choice==2:

        choice=int(input("Enter a  choice by faculty detail: "))
        if choice==1:
            Add_mark_student()
            yn=input("Press Y for yes and N for no : ")
            if yn == 'y':  #user 'y' for yes to continue to program
                Add_mark_student()
            elif yn == 'n':  #uesr 'n' for no to break to program
                print(all_record)
                faculty()

        choice=int(input("Enter a  choice by head faculty : "))
        if choice==1:
            View_All_Student()
            yn=input("Press Y for yes and N for no : ")
            if yn == 'y':  #user 'y' for yes to continue to program
                View_All_Student()
            elif yn == 'n':  #uesr 'n' for no to break to program
                print(all_record)
                faculty()


   
def student():
    print("""
    1. student detail
    2. student parents
    """)
    c_choice=int(input("Enter a  choice by Student "))
    if c_choice==3:

        choice=int(input("Enter a  choice by student detail: "))
        if choice==1:
            student_derails()
            yn=input("Press Y for yes and N for no : ")
            if yn == 'y':  
                student_derails()
            elif yn == 'n': 
                print(all_record)
                student()

        choice=int(input("Enter a  choice by student  parents: "))
        if choice==1:
            student_parents()
            yn=input("Press Y for yes and N for no : ")
            if yn == 'y':  
                student_parents()
            elif yn == 'n':  
                print(all_record)
                student()


choice=int(input("Enter Role Id: "))
if choice==1:
    Counselor()
elif choice==2:
    faculty()
elif choice==3:
    student()
else:
    print("Enter Correct Choice")










