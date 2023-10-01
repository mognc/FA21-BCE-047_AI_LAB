# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 16:17:48 2023

@author: mognc
"""

number = 1+2 * 3 /4.0
print("1+2 * 3 /4.0 is ",number)

remainder = 11%3
print("11%3 is ",remainder)

squared = 7**2
print("7**2 is", squared)

cubed = 2**3
print("2**3 is ",cubed)

#List operators 
even_numebrrs = [2,4,6,8]
uneven_numbers = [1,3,5,7]
all_numbers = uneven_numbers+even_numebrrs
print("List of numbers: ", all_numbers)

print("Repeating sequence of list: ", [1,2,3]*3)

x = object()
y = object()

x_list = [x]
y_list = [y]
concat_list = []
print("x_list contains {} objects".format(len(x_list)))
print("y_list contains {} objects".format(len(y_list)))
print("big_list contains {} objects".format(len(concat_list)))

if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if concat_list.count(x) == 10 and concat_list.count(y) == 10:
    print("Great!")