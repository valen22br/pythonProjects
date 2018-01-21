#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 20:23:06 2018

@author: Luis Gustavo Grubert Valensuela

*******************************************************************************
Name: Luis Gustavo Grubert Valensuela Z#:23351882 lvalensuela2015@fau.edu
Course: Python Programming COP 4045-001 Spring 2018
Professor: Dr. Ionut Cardei
Due Date:01/21/2018             Due Time: 11:30PM
Assignment Homework 1
Last Changed: 01/21/2018

Description:
In this assignment a program will solve quadratic equations
*******************************************************************************


"""


import pylab

print("This program calculates quadratic equations in the format: axˆ2+bx+c\n\
      and also shows its graph throut the module pylab")


while True:

    #variables initilization
    solution_int1 = 0;
    solution_int2 = 0;
    
    a_str = input ("Enter a value: ")
    a_int = int(a_str);

    b_str = input ("Enter b value: ")
    b_int = int(b_str)

    c_str = input ("Enter c value: ")
    c_int = int(c_str)
    
    number_solutions_int = 0
    determinant_value_float = (b_int ** 2 -(4 * a_int * c_int))
    
    if(determinant_value_float < 0):
        number_solutions_int = 0
        print("no real solutions")
    elif (determinant_value_float > 0):
        number_solutions_int = 2
        solution_int1 = (b_int * -1 + (determinant_value_float ** 0.5))/ (2 * a_int)
        solution_int2 = (b_int * -1 - (determinant_value_float ** 0.5))/ (2 * a_int)
        print("two solutions:  x1= ", solution_int1, " x2= ", solution_int2)
    else:
        number_solutions_int = 1
        solution_int1 = (b_int * -1 + determinant_value_float)/ 2 * a_int
        print("one solutions:  x1= ", solution_int1)
      
    if(number_solutions_int != 0):
        xs = []
        ys = []
        # prepare the domain for the function we graph
        x0 = -5.0
        x1 = +5.0
        x = x0
        n = 100             # n points
        dx = (x1 - x0) / n  # delta between points
        while x <= x1:
            xs.append(x)
            
            y = a_int * x ** 2 + b_int *x + c_int
            
            ys.append(y)
            x += dx
            
        pylab.plot(xs, ys, "bo")
        pylab.show
        pylab.pause(1)
        
        print("end")
