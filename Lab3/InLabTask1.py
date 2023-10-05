# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 14:50:53 2023

@author: mognc
"""

def count_even_numbers(number_list):
    
    even_count =0
    
    for num in number_list:
        if num%2==0:
            even_count +=1
    return even_count


numbers1 = [1,2,3,4,5,6,7,8,9,10]
numbers2 = [11,13,15,17]
numbers3 = []

print(count_even_numbers(numbers1))
print(count_even_numbers(numbers2))
print(count_even_numbers(numbers3))