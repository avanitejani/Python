all_record = {}  #----------------------------------------------------- create empty Dictionary

# # # 1. Add Student

def add_student(): #--------------------------------------------------  creatc fuction for add student
    serial=int(input("Enter student Serial Number : ")) #-------------  input serial Number
    first_name=input("Enter student First Name : ") #-----------------  input student first name
    last_name=input("Enter student Last Name : ") #-------------------  input student last name
    Contect_number=int(input("Enter student Contect Number : ")) #----  input student contect number
    faculty = input("Enter Faculty name: ") #-------------------------  input facult name
    subjectlist=[] #--------------------------------------------------  Creta Empty subject List 
    marklist=[] #-----------------------------------------------------  Creta Empty mark List 
    feeslist=[] #-----------------------------------------------------  Creta Empty fees List 
    for i in range(1,3): 
        subjectname=input(f"Enter Subjectname {i}: ")
        subjectlist.append(subjectname) #-----------------------------  Use Append Method
        marks=int(input(f"Enter student {subjectname} marks -> {i}: "))
        marklist.append(marks)
        fees=int(input(f"Enter student {subjectname} Fees -> {i}: "))
        feeslist.append(fees)
        print("--------------------------------------")
    

    global all_record #------------------------------------------------- store student details
    all_record.update({serial:{"First Name":first_name,"Last Name":last_name,"Countect Number":Contect_number,"Faculty name":faculty,
                                         "Subject":subjectlist,"Marks":marklist,"Fees":feeslist}})
                      #------------------------------------------------- Use Update to print all data in Dictionary formet

def remove_student(): #------------------------------------------------- creatc fuction for remove student
    print(" choice Remove Student ")
    serial_number=int(input("Enter  student Remove Serial Number : ")) # Enter serial number to remove a student data
    if serial_number in all_record.keys():
        all_record.pop(serial_number)  #-------------------------------- Use pop function remove student data
    else:
        print("Student not exiesting your Student List.")



def view_all_student(): #----------------------------------------------- creatc fuction for View All Student
    print(" chioce View All Student")
    for Serial_num in all_record:
        print(f"serial num = {Serial_num}\n")
        print("first name ->",all_record[Serial_num]["First_Name"])
        print("Last_name  ->",all_record[Serial_num]["Last_Name"])
        print("Countect Number ->",all_record[Serial_num]["Countect_Number"])
        print("Subject ->",all_record[Serial_num]["Subject"])
        print("Marks ->",all_record[Serial_num]["Marks"])
        print("Fees ->",all_record[Serial_num]["Fees"])
        



def view_sepcific_student(): #----------------------------------------------- creatc fuction for View view sepcific Student
    print("Enter serial number to show student details ")
    Serial_num=int(input("Enter Serial Number : "))
    if Serial_num in all_record:
      
        print("first name ->",all_record[Serial_num]["First_Name"])
        print("Last_name  ->",all_record[Serial_num]["Last_Name"])
        print("Countect Number ->",all_record[Serial_num]["Countect_Number"])
        print("Subject ->",all_record[Serial_num]["Subject"])
        print("Marks ->",all_record[Serial_num]["Marks"])
        print("Fees ->",all_record[Serial_num]["Fees"])
        
