# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 15:38:05 2023

@author: mognc
"""

import numpy as np

total_score = 100
no_of_tries =5
values = np.random.randint(10)
user_input =  int(input("Enter an integer: "))

if(user_input == values):
    print("Your guess is correct")
else:
    while(user_input != values):     
        if(user_input > values):
            print("Your input is greater than the number, try again")
            total_score = total_score-5
            no_of_tries -=1
            if(no_of_tries ==0):
                print("You have lost")
                break
            user_input =  int(input("Enter an integer: "))
        else:
            print("Your input is lower than the number, try again")
            total_score = total_score-5
            no_of_tries -=1
            if(no_of_tries==0):
                print("You have lost")
                break
            user_input =  int(input("Enter an integer: "))
if(total_score > 75):
    print("Your score is", total_score)
