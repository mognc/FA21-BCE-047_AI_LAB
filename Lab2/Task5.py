# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 16:38:34 2023

@author: mognc
"""

numeric_data = [10,20,30,40,50]

for number in numeric_data:
    result = number *2
    print(result)

text = "Hello, World!"

for char in text:
    print(char)

new_text = ""
for char in text:
    if char.isalpha():
        new_text += char.upper()
    else:
        new_text += char
print(new_text)

numeric_data = []

for i in range(1,11):
    numeric_data.append(i)
    
print(numeric_data)