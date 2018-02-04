#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 10:37:43 2018

@author: Luis Gustavo Grubert Valensuela
*******************************************************************************
Name: Luis Gustavo Grubert Valensuela Z#:23351882 lvalensuela2015@fau.edu
Course: Python Programming COP 4045-001 Spring 2018
Professor: Dr. Ionut Cardei
Due Date:02/04/2018             Due Time: 11:30PM
Assignment Homework 2
Last Changed: 02/04/2018
Description:
This program will require from the user the following data:
    function (Ex. 2 * math.sin(2*math.pi * x))
    number of samples,
    xmin,
    x max.
Them the program will calculate values of y in function of f(x) and plot its 
graph on the screen.
*******************************************************************************
"""

import math
import pylab

print("This program calculates quadratic equations in the format: axˆ2+bx+c\n\
      and also shows its graph throut the module pylab")


while True:

    fun_str = input ("Enter function with variable x: ")
    n_samples_int = int(input("Enter number os samples: "))
    x_min_int = int(input("Enter xmin: "))
    x_max_int = int(input("Enter xmax: "))
    

      
   
    xs = []
    ys = []
    # prepare the domain for the function we graph
    #x0 = -5.0
    #x1 = +5.0
    x = x_min_int
    #n = 100             # n points
    
    dx = (x_max_int - x_min_int) / n_samples_int  # delta between points
    while x <= x_max_int:
        xs.append(x)
        
        #y = a_int * x ** 2 + b_int *x + c_int
        y = eval(fun_str)
        #print(y)
        ys.append(y)
        x += dx
        
    print("{:>10} {:>10}".format("x","y"))
    print("----------------------")
    for i in range(len(xs)):
        print("{:>10.4f} {:>10.4f}".format(xs[i], ys[i]))
 
    pylab.xlabel("x")
    pylab.ylabel("y")
    pylab.title(fun_str)
    pylab.plot(xs, ys, "bo-")
    pylab.show
    pylab.pause(1)
    
    print("end")
