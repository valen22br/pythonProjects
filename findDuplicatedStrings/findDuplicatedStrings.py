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
This program searches for repeated strings with the length determined by the 
user, and also returns the repeated string with max length. If no repeated 
strings were found, "" is returned
*******************************************************************************
"""

def ind_dup_str(s,n):
    stringLength = len(s)
    count = 0;
    for i in range(0,((stringLength+1) - n)):
        count = 0;
        for j in range(0,((stringLength+1) - n)):
            if (s[i:i+n] == s[j:j+n]):
                count +=1
            if(count > 1):
                return s[i:i+n]
                break;
    return""
    
def find_max_dup(s):
    longestStrFound = ""
    for i in range(1, len(s)):
        if (ind_dup_str(s,i) != ""):
            longestStrFound = ind_dup_str(s,i)
    return longestStrFound

while True:
    userString = str(input("Please enter with a string: "))
    userLength = int(input("Please enter with the length of the string: "))

    repetedString = ind_dup_str(userString,userLength)
    print("\n\nThe first occurrence of a repeated string with length " + str(userLength) + " was '" + repetedString + "'")
    
    print("\n\nThe repeated string with max length found was '" + find_max_dup(userString) + "'")
