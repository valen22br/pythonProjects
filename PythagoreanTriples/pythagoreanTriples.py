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
in the range determined by the user
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
def findPythagoreanTriples(n):
    count = 0;
    n +=1
    for c in range(n):
        for a in range(1,c):
            b = math.sqrt(c * c - a * a)
            if b% 1 == 0:
                #print("{:04d}".format(42))    
                print("({:03d}, {:03d}, {:03d})".format(a, int(b), c))
                count +=1
    print("{} possible(s) Pythagorean Triples".format(count))
    
n = int(input("Please enter with a integer indicating the maximum value for the\
 hypothenuse and we will calculate all possible pythagorean triples  with it=> "));
findPythagoreanTriples(n)

