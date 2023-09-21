# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 16:31:23 2023

@author: mognc
"""

Current_Cgpa = float(input("Enter current Cgpa: "))
Total_creditHrs = int(input("Enter number of credit hours studied: "))
old_points = Current_Cgpa*Total_creditHrs


current_CreditHrs = int(input("Enter number of current credit hours enrolled: "))
Required_Cgpa = float(input("Enter required Cgpa: "))

new_points = Required_Cgpa*(Total_creditHrs+current_CreditHrs)
points = new_points-old_points
result = points/current_CreditHrs

if(result > 4):
    print("You cannot achieve required Cgpa\nYour Cgpa after current semester will be: ", result)
else:
    print("You need {} cgpa to attain required cgpa".format(result))