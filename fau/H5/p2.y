#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 11:19:19 2018

@author: valen
"""

import csv

"""
Function to open a csv falue and iterate through it using the csv module
"""
def openFile(fileName, mode):
    try:
        f = open(fileName, mode)
        #reader = csv.reader(f)
        return f
        #f.close()
    except:
        print("Coud not open the file {} with mode {}.".format(fileName, mode))
        f.close()
        
def ed_clearContent(filename):
    f = openFile(filename, "+w")
    f.write("")
    f.close()

def ed_read(filename, fromValue=0, to=-1):
    f = openFile(filename, "r")
    #print(f.readlines())
    lengthFileContent = f.readlines()
    lengthFileContent = len(lengthFileContent)
    print(lengthFileContent)
    if(fromValue > lengthFileContent):
      raise ValueError("Parameter exceeds the file length")  
      
    
    f.seek(fromValue)
    return(f.read())
    f.close()

def ed_find(filenam, search_str):
    pass

def ed_replace(fliename, search_str):
    pass

def ed_append(filename, string):
    length = len(string)
    f = openFile(filename, "a")
    f.write(string)
    f.close()
    return length


def ed_write(filename, pos_str_col):
    pass

def ed_insert(filaneme, pos_str_col):
    pass




def main():
    fn = "file1.txt" #asssume this file does not exist yet.
    
    ed_clearContent(fn)
    
    print(ed_append(fn,"0123456789"))
    print(ed_append(fn,"0123456789"))
    
    print(ed_read(fn, 2, -1))
    
    #ed_append(fn,"GUTI")
    
    '''
    f = open(fn, "+w")
    f.write("0123456789")
    f.write("0123456789")
    
    
    f = open(fn, "+w")
    f.write("a")
    f.write("b")
    f.close()
    
    f = open(fn, "+w")
    f.write("c")
    f.write("d")
    f.close()
    '''
    


main()
