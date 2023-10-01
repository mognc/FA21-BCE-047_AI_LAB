# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 16:33:12 2023

@author: mognc
"""

x = 2
y = 10
if x>2:
    print("x>2")
elif x ==2 and y >50:
    print("x==2 and y > 50")
elif x < 10 or y > 50:
    print("x < 10 or y > 50")
else:
    print("Nothing worked.")
    
name_list1 = ["Ali", "Ahmad"]
name_list2 = ["Ali", "Ahmad"]
print(not(name_list1 == name_list2))

name2 = " Ahmad"
print(name_list1 == name_list2)
print(name_list1 is name_list2)