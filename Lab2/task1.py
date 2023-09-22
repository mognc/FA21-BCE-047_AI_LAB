# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 21:17:15 2023

@author: FA21-BCE-047
"""

student_record = {}

choice = 1

while(choice!=-1):
    print("Press 1 to add student record")
    print("Press 2 to update student record")
    print("Press 3 to delete student record")
    print("Press -1 to exit")
    
    option = int(input())
    
    if(option==1):
        name = input("Please enter name: ")
        registeration_no = input("Enter registeration#:")
        email = input("Enter email:")
        student_record[registeration_no] = [name, email]
        
    elif(option==2):
        registeration_no = input("Enter registeration# of student to update his/her record:")
        name = input("Enter new name:")
        email = input("Enter new email:")
        student_record[registeration_no] = [name, email]
        
    elif(option==3):
        registeration_no = input("Enter registeration# you want to delete record of:")
        del student_record[registeration_no]
    
    else:
        print("Enter valid option")
        
    print("\nPress -1 to exit or 1 to continue")
    choice = int(input())
print(student_record)