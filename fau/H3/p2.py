#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Luis Gustavo Grubert Valensuela
*******************************************************************************
Name: Luis Gustavo Grubert Valensuela Z#:23351882 lvalensuela2015@fau.edu
Course: Python Programming COP 4045-001 Spring 2018
Professor: Dr. Ionut Cardei
Due Date:02/04/2018             Due Time: 11:30PM
Assignment Homework 2
Last Changed: 02/04/2018
Description:
In this assignment a program will calculate the Pythagorean Triples possible
in the range determined by the user. Will return a tuple with the results
*******************************************************************************
"""

import math

"""
*******************************************************************************
Name:findPythagoreanTriples(n)
Precondition: An int value will be the argument of the function
Postcondition: returns all pythagorean triples possibles having n as it max 
value for the hypothenuse 
Description:  returns all pythagorean triples possibles having n as it max 
value for the hypothenuse 
*******************************************************************************
"""
def compute_Pythagoreans(n):
    try:
        n +=1
        pitagoriamTuple = tuple([(a, int(math.sqrt(c * c - a * a)), c) 
        for c in range(n) 
        for a in range(1,c) 
        if (math.sqrt(c * c - a * a))% 1 == 0])
        
        return(pitagoriamTuple)
    except:
        print("An error has ocurried")
        return(())

try:    
    n = int(input("Please enter with a integer indicating the maximum value for the\
     hypothenuse and we will calculate all possible pythagorean triples  with it=> "));
    print(compute_Pythagoreans(n))
except:
    print("An error has ocurried")
    print(())
