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
    fileContentStr = stringFileContent(filename)
    lengthFileContent = len(fileContentStr)
    #print(lengthFileContent)
    if(fromValue > lengthFileContent):
      raise ValueError("Parameter exceeds the file length")  
    return(fileContentStr[fromValue:to])

def ed_find(filename, search_str):
    listIndexesFound = []
    fileContentStr = stringFileContent(filename)
    findIndex = fileContentStr.find(search_str)
    if findIndex == -1:
       return  listIndexesFound
    else:
        listIndexesFound.append(findIndex)
        while(findIndex != -1):
            findIndex = fileContentStr.find(search_str,findIndex+len(search_str))
            if(findIndex != -1):
                listIndexesFound.append(findIndex)
            
    return listIndexesFound
    
    

def ed_replace(filename, search_str, replace_with, occurrence=-1):
    stringContent = ed_read(filename)
    listIndexFound = ed_find(filename,search_str)
    if(occurrence == -1):
        replaceTimes = len(listIndexFound)
        stringContent = stringContent.replace(search_str,replace_with,replaceTimes)
        #return stringContent
    else:
        replaceTimes = 1
        if(occurrence >= len(listIndexFound)):
            return 0
        else:
            tempString = stringContent[0:listIndexFound[occurrence]]
            stringContent = stringContent[listIndexFound[occurrence]:].replace(search_str,replace_with,replaceTimes)
            stringContent = tempString + stringContent
            
    print(stringContent)

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
    
    '''
    ed_clearContent(fn)
    
    print(ed_append(fn,"0123456789"))
    print(ed_append(fn,"0123456789\n"))
    print(ed_append(fn,"0123456789"))

    print(ed_read(fn))
    
    print(ed_read(fn,3,9))
    
    print(ed_read(fn,3))
    '''
    
    ed_clearContent(fn)
    
    print(ed_append(fn,"0123456789"))
    print(ed_append(fn,"0123456789\n"))
    print(ed_append(fn,"0123456789"))
    #print(ed_read(fn))
    
    print("\n")
    
    #print(ed_find(fn,"346"))
    
    #print(ed_find(fn,"345"))
    
    ed_replace(fn,"345", "ABCDE",2)
    ed_replace(fn,"345", "ABCDE",1)
    ed_replace(fn,"345", "ABCDE",0)
    ed_replace(fn,"345", "ABCDE",-1)
    ed_replace(fn,"345", "ABCDE")
    ed_replace(fn,"345", "ABCDE",3)
    
    
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
