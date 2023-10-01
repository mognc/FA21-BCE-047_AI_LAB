# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 16:42:33 2023

@author: mognc
"""

count = 1
while count <= 5:
    print(count)
    count+=1
    
text = "Hello"
index = 0
while index < len(text):
    print(text[index])
    index +=1
    
student_grades = {"Ali":1, "Ahmad":2, "Abdullah":3}
keys = list(student_grades.keys())
index = 0
while index < len(keys):
    key = keys[index]
    value = student_grades[key]
    print(f"{key}: {value}")
    index +=1