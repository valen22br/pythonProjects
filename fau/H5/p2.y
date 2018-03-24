#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 11:19:19 2018

@author: valen
"""

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
        
def stringFileContent(fn):
    try:
        f = open(fn,"r")
        fileContent = f.readlines()
        fileContentStr = ""
        for i in fileContent:
            fileContentStr += i
            
        return fileContentStr
    except:
        print("Error trying to read the file content")
        
def ed_clearContent(filename):
    f = openFile(filename, "+w")
    f.write("")
    f.close()

def ed_read(filename, fromValue=0, to=-1):
    f = openFile(filename, "r")
    fileContent = f.readlines()
    fileContentStr = ""
    for i in fileContent:
        fileContentStr += i
    lengthFileContent = len(fileContent[0])
    print(lengthFileContent)
    if(fromValue > lengthFileContent):
      raise ValueError("Parameter exceeds the file length")  
      
    #f.seek(fromValue)
    return(fileContentStr[fromValue:to])
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
    print(ed_append(fn,"0123456789\n"))
    print(ed_append(fn,"0123456789"))

    print(ed_read(fn))
    
    print(ed_read(fn,3,9))
    
    print(ed_read(fn,3))
    
    
    ed_clearContent(fn)
    
    print(ed_append(fn,"0123456789"))
    print(ed_append(fn,"0123456789\n"))
    print(ed_append(fn,"0123456789"))
    
    
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
