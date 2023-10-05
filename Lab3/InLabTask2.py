# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 14:55:25 2023

@author: mognc
"""

def calculate_gpa(student_list):

    student_updated_dict = {}
    
    for student in student_list.items():
            percentage = student_list[student]
            if percentage >= 85:
                grade_points = 4
            elif percentage <= 84 and percentage >= 80:
                grade_points = 3.66
            elif percentage <= 79 and percentage >= 75:
                grade_points = 3.33
            elif percentage <= 74 and percentage >= 71:
                grade_points = 3.00
            elif percentage <= 70 and percentage >= 68:
                grade_points = 2.66
            elif percentage <= 67 and percentage >= 64:
                grade_points = 2.33
            elif percentage <= 63 and percentage >= 61:
                grade_points = 2.00
            elif percentage <= 60 and percentage >= 58:
                grade_points = 1.66
            elif percentage <= 57 and percentage >= 54:
                grade_points = 1.30
            elif percentage <= 53 and percentage >= 50:
                grade_points = 1.00
            else:
                grade_points = 0.00

            grade = (sum(student.values()))/5
    
    return grade


student_dict = {
    "Ali": [10,20,30,40,50],
    "Ahmad": [10,20,30,40,50],
    "Abdullah": [10,20,30,40,50],
    "Javed": [10,20,30,40,50],
    "Farhan":  [10,20,30,40,50]
}

print(calculate_gpa(student_dict))