all_record = {}

# 1. Add Student

def add_student():
    serial = int(input("Enter Serial Number : "))
    first_name = input("Enter First Name : ")
    last_name = input("Enter Last Name : ")
    Contect_number = int(input("Enter Contect Number : "))
    faculty = input("Enter Faculty name: ")
    global all_record
    all_record.update({serial: {'fname': first_name, 'lname': last_name,
                      'Contact': Contect_number, "Faculty": faculty, "subject": {}}})
    # for i in range(2):
    #     subjectname = input("Enter Subjectname : ")
    #     marks = int(input("Enter Marks : "))
    #     fees = int(input("Enter Fees :"))
    #     all_record[serial]["subject"].update(
    #         {subjectname: {"marks": marks, "fees": fees}})
        

        

# 2. Remove Student

def remove_student():
   
   serial=int(input("Enter Remove Serial Number : "))
 
   if serial in all_record.keys():        
    all_record.pop(serial)
        
   else:
        print("Student not exiesting your Student List.")

  
        


# 3. View All Student

def view_all_student():
    

    print("View All Student")
   
    for student in all_record.keys():
        print(f"Student Serial Number : {student}")
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
        print("-----------------------------\n")

# print(all_record)




# 4. View Specific Student

def view_sepcific_student():


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

# print(all_record)

