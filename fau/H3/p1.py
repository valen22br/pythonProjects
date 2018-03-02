#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 12:28:25 2018

@author: Luis Gustavo Grubert Valensuela
*******************************************************************************
Name: Luis Gustavo Grubert Valensuela Z#:23351882 lvalensuela2015@fau.edu
Course: Python Programming COP 4045-001 Spring 2018
Professor: Dr. Ionut Cardei
Due Date:02/18/2018             Due Time: 11:30PM
Assignment Homework 3
Last Changed: 02/18/2018
Description:
In this assignment tree functions will be created:
    a) A function called input_tuple (in a new file p1.py) that reads from the
    terminal a sequence of objects with types provided by a tuple given as
    parameter and that returns the sequence of objects read as a tuple.
    b) a function called input_tuple_lc that is identical to input_tuple except 
    that it uses list comprehension(s).
    c) a function read_tuple that works similarly to input_tuple, but instead 
    of reading input from the terminal, it reads text from a file object passed 
    as argument. 
*******************************************************************************
"""
def treatTrueFalseStrings(booleanString):
    """ Function to parse true of false values from a string """
    booleanInt = booleanString
    listFalseString = ["False","false","0",""," ","FALSE"]
    if (booleanString in listFalseString):
        booleanInt = 0
    return booleanInt

def input_tuple(prompt, types, sep = ","):
    """  that reads from the
    terminal a sequence of objects with types provided by a tuple given as
    parameter and that returns the sequence of objects read as a tuple. """
    inputString = str(input(prompt))
    listString = inputString.split(sep)
    try:
        if(len(listString) == len(types)):
            for i in range(len(listString)):
                listString[i] = types[i](treatTrueFalseStrings(listString[i]))
            
            myTuple = tuple(listString)
        else:
            #print("An error has occurred 1.")
            myTuple = ()
    except:
        #print("An error has occurred 2.")
        myTuple = ()
    return myTuple

def input_tuple_lc(prompt, types, sep = ","):
    """  a function called input_tuple_lc that is identical to input_tuple
    except that it uses list comprehension(s) """
    try:
        inputString = str(input(prompt))
        listString = inputString.split(sep)
        lst = [types[i](treatTrueFalseStrings(listString[i])) for i in range(len(listString)) if (len(listString) == len(types)) ]
        myTuple = tuple(lst);
    except:
        #print("An error has occurred 3.")
        myTuple=[]
    return myTuple;

def read_tuple(file_obj, types, sep):
    """reads text from a file object passed 
    as argument. """
    try:
        
        line_str_list = []
        
        
        """
        The commented code below was transformed in two comprehension lists.
        
        for line_str in file_obj:
            line_str_list.append(line_str.split(sep))
            
        for i in range(len(line_str_list)):
            print(line_str_list[i])
            for j in range(len(line_str_list[i])):
                print(line_str_list[i][j])
                line_str_list[i][j] = types[j](treatTrueFalseStrings(line_str_list[i][j].replace("\n", "")))
            
       """
        
        [line_str_list.append(line_str.split(sep)) for line_str in file_obj]
        line_str_list2 = []
        line_str_list2 = [types[j](treatTrueFalseStrings(line_str_list[i][j].replace("\n", "")))
            for i in range(len(line_str_list))
            for j in range(len(line_str_list[i]))]
       
        # get only the first line read from the file.
        myTuple = tuple(line_str_list2[0:len(types)]);
        return(myTuple)
           
    except:
        print("An error has occurred 3.")
        myTuple = ()
        return myTuple

def testif(b, testname, msgOK = "", msgFailed = ""):
    """ function created to test the program. Reurns true if a tuple is 
    returned as the return statement"""
    if type(b):
        print("Success: " + testname + "; "+ msgOK)
    else:
        print("Failed: " + testname + "; "+ msgFailed)
        
    print("\n")
    return b

print(input_tuple("Enter first name, last name, age ( float), ID (int), fulltime (bool): ",
(str, str,  float, int, bool), # this is the tuple with expected types
","))

testif(isinstance(input_tuple("Enter first name, last name, age ( float), ID (int), fulltime (bool): ",
(str, str,  float, int, bool), # this is the tuple with expected types
","), tuple), "input_tuple test")

testif(isinstance(input_tuple_lc("Enter first name, last name, age ( float), ID (int), fulltime (bool): ",
(str, str,  float, int, bool), # this is the tuple with expected types
","),tuple), "input_tuple_lc test")

f = open("cars.csv", "r")
testif(isinstance(read_tuple(f, (str, str, float, int, bool), ","), tuple), "read_tuple test")
f.close()
