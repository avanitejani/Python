from Counselor import *  #------------------------------------------------ import conselor

def student_details():  #------------------------------------------------- creatc fuction for View All Student
    student=int(input("Enter Serial Number : "))
    if student in all_record.keys():
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
    else:
        print("Not A Student Serial Number")

stu={} #----------------------------------------------------------------- create empty Dictionary
def student_parents(): #------------------------------------------------- create fuction for Add student parents information
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name : ")
    Contect_number = int(input("Enter Contect Number : "))
    salary = int(input("Enter salary : "))
    global stu  #-------------------------------------------------------- store student details
    stu.update( {'fname': first_name, 'lname': last_name,'Contact': Contect_number, "salary": salary,})

