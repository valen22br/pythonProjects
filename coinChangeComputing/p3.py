#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 11:37:57 2018

@author: Luis Gustavo Grubert Valensuela

*******************************************************************************
Name: Luis Gustavo Grubert Valensuela Z#:23351882 lvalensuela2015@fau.edu
Course: Python Programming COP 4045-001 Spring 2018
Professor: Dr. Ionut Cardei
Due Date:01/21/2018             Due Time: 11:30PM
Assignment Homework 1
Last Changed: 01/21/2018

Description:
In this assignment a program will compute change
*******************************************************************************


"""



while True:
    
    amount_str = input("Enter amount: ")
    amount_float = float(amount_str)

    quartes_int , dimes_int , pennies_int, total_float = 0 , 0 , 0 , 0.0
    total_coins_int = 0
    if(amount_float < 0):
        print("Invalid input, try it again: ")
        continue
    
    total_amount_int = int(amount_float * 100);
    quartes_int = total_amount_int // 25;
    dimes_int = total_amount_int % 25//10
    pennies_int = ((total_amount_int % 25)%10)
    
    total_coins_int = quartes_int + dimes_int + pennies_int
    
    print("$%.2f" % amount_float+" makes "+ str(quartes_int) + " quartes, "
          + str(dimes_int) + " dimes, "+ str(pennies_int) + " penies ("
          + str(total_coins_int) + " coins), total amount in coins: $%.2f"
          % amount_float+ ".")


