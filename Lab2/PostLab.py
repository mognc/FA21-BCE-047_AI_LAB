# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 16:47:59 2023

@author: mognc
"""


student_grades = {
    "Ali": 10,
    "Ahmad": 50,
    "Abdullah": 90,
    "Javed": 40,
    "Farhan": 60,
    "Khan": 20,
    "farooq": 100
}

# Search for a specific student's grade
while True:
    student_name = input("Enter the student's name (or 'exit' to quit): ").strip()
    
    if student_name.lower() == 'exit':
        break
    
    if student_name in student_grades:
        grade = student_grades[student_name]
        if grade >= 90:
            category = "Excellent"
        elif grade >= 80:
            category = "Very Good"
        elif grade >= 70:
            category = "Good"
        else:
            category = "Needs Improvement"
        
        print(f"{student_name}'s grade is {grade} ({category})")
    else:
        print("Student not found. Please enter a valid student name.")
