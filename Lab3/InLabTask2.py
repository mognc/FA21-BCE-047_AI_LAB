# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 14:55:25 2023

@author: mognc
"""

def getMarkGrade(mark):
    grade = ""
    grade_point = 0.0
    if mark < 50:
        grade = "F"
        grade_point = 0.00
    elif mark >= 50 and mark <= 53:
        grade = "D"
        grade_point = 1.00
    elif mark >= 54 and mark <= 57:
        grade = "D+"
        grade_point = 1.30
    elif mark >= 58 and mark <= 60:
        grade = "C-"
        grade_point = 1.66
    elif mark >= 61 and mark <= 63:
        grade = "C"
        grade_point = 2.00
    elif mark >= 64 and mark <= 67:
        grade = "C+"
        grade_point = 2.33
    elif mark >= 68 and mark <= 70:
        grade = "B-"
        grade_point = 2.6
    elif mark >= 71 and mark <= 74:
        grade = "B"
        grade_point = 3.00
    elif mark >= 75 and mark <= 79:
        grade = "B+"
        grade_point = 3.33
    elif mark >= 80 and mark <= 84:
        grade = "A-"
        grade_point = 3.66
    elif mark >= 85:
        grade = "A"
        grade_point = 4.00
    
    return {
        "grade": grade,
        "point": grade_point
        }
    

def calculate_gpa(student_list):
    #Check for list length
    if(len(student_list) == 0):
        print("List is empty")
        return 0
    
    #Initialize the list to return
    newList = []
    
    #Loop over student list
    for student in student_list:
        #Initialze a new student dict
        newStdDict = student
        #Initialze cgpa
        cgpa = 0.0
        #Initialze grade points list
        grdpts = []
        #Initialze grades list
        grds = []
        #Loop over each student marks to get grade and grade point
        for mark in student["marks"]:
            grds.append(getMarkGrade(mark)["grade"])
            grdpts.append(getMarkGrade(mark)["point"])
            
        #Loop over grade points to summ
        for gpa in grdpts:
            cgpa = cgpa + gpa
        #Take average to get cgpa
        cgpa = cgpa / 5
        
        #Add grades, grade points and gpa in new dict
        newStdDict["grades"] = grds
        newStdDict["grade_points"] = grdpts
        newStdDict["gpa"] = cgpa
        
        #Add new student dict to return list
        newList.append(newStdDict)
        
    return newList


student_dict = [
    {
    "name" : "Ali",
    "marks": [10,20,30,40,50]
    },
    {
    "name" : "Ahmad",
    "marks": [10,20,30,40,50]
    },
    {
    "name" : "Abdullah",
    "marks": [10,20,30,40,50]
    },
    {
    "name" : "Javed",
    "marks": [10,20,30,40,50]
    },
    {
    "name" : "Farhan" ,
    "marks" : [10,20,30,40,50]
    }
]

print(calculate_gpa(student_dict))