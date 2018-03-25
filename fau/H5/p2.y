#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 11:19:19 2018

@author: Luis Gustavo Grubert Valensuela
*******************************************************************************
Name: Luis Gustavo Grubert Valensuela Z#:23351882 lvalensuela2015@fau.edu
Course: Python Programming COP 4045-001 Spring 2018
Professor: Dr. Ionut Cardei
Due Date:03/25/2018             Due Time: 11:30PM
Assignment Homework 5
Last Changed: 03/04/2018
Description:
    Implementation of a non-interactive Text Editing
*******************************************************************************
"""
import os
from testif import testif
'''
Method to open a filename
Takes the fileName and mode as arguments
'''
def openFile(fileName, mode):
    try:
        f = open(fileName, mode)
        #reader = csv.reader(f)
        return f
        #f.close()
    except:
        print("Coud not open the file {} with mode {}.".format(fileName, mode))
        f.close()
'''
Method used to write a string to a file
Takes the fileName and myString
'''        
def writeStringToFile(filename, myString):
    f = openFile(filename, "+w")
    f.write(myString)
    f.close

'''
Method that reads the file content and returns the string of what was read
Takes the fileName as argument
'''            
def stringFileContent(fn):
    try:
        f = open(fn,"r")
        fileContent = f.read()
        fileContentStr = ""
        for i in fileContent:
            fileContentStr += i
            
        return fileContentStr
    except:
        print("Error trying to read the file content")

'''
Method to clear the content of a file
Takes the fileName as argument
'''
def ed_clearContent(filename):
    f = openFile(filename, "+w")
    f.write("")
    f.close()

'''
Method to read a slice of the file content. 
Returns the string that was read
'''
def ed_read(filename, fromValue=0, to=-1):
    fileContentStr = stringFileContent(filename)
    lengthFileContent = len(fileContentStr)
    #print(lengthFileContent)
    if(fromValue > lengthFileContent):
      raise ValueError("Parameter exceeds the file length")  
    if(to == -1):
        return(fileContentStr[fromValue:])
    else:
        return(fileContentStr[fromValue:to])
'''
Method fo find a search_string on a file
Returns a list with the index position where the search_string was found.
Return [] if the string was not found inside the file content
'''
def ed_find(filename, search_str):
    listIndexesFound = []
    fileContentStr = stringFileContent(filename)
    #print("Content Type=> ",type(fileContentStr))
    if(fileContentStr is None):
        fileContentStr = ""
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
    
'''
Method to replace a search_str to a new string value.
Returns the numbes of strings that was written to the file.
Takes as arguments: filename, search_str, replace_with and occurrence.
If occurrence is =-1, it replaces all the occurrences, otherwise, it will
replace the position equal to occurrence where the search_str was found.
'''
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
            
    #print(stringContent)
    writeStringToFile(filename,stringContent)
    return replaceTimes

'''
Method to append a string to a file_content
Takes filename and string as arguments
'''
def ed_append(filename, string):
    length = len(string)
    f = openFile(filename, "a")
    f.write(string)
    f.close()
    return length

'''
Method to write a string to a file_content
Takes filename and a tuple pos_str_col as arguments
Example: ed_write("filename", ((2, "ABC"),(10, "DEFG")))
'''
def ed_write(filename, pos_str_col):
    stringFileContent = ed_read(filename)
    totalLengthString = len(stringFileContent)
    for key,value in pos_str_col:
        if(key > totalLengthString):
            raise ValueError("Position parameter is grater than the file contents size. Position: ", key)
        else:
            tempStr = stringFileContent[0:key]
            posStr = value + stringFileContent[key+len(value):]
            stringFileContent = tempStr+posStr
    writeStringToFile(filename,stringFileContent)
    #print(len(pos_str_col))
    return len(pos_str_col)
    
'''
Method to insert a string to a file_content
Takes filename and a tuple pos_str_col as arguments
Example: ed_insert("filename", ((2, "ABC"),(10, "DEFG")))
'''
def ed_insert(filename, pos_str_col):
    stringFileContent = ed_read(filename)
    totalLengthString = len(stringFileContent)
    slicePosition = 0
    for key,value in pos_str_col:
        if(key > totalLengthString):
            raise ValueError("Position parameter is grater than the file contents size. Position: ", key)
        else:
            tempStr = stringFileContent[0:key+slicePosition]
            posStr = value + stringFileContent[key+slicePosition:]
            stringFileContent = tempStr+posStr
            slicePosition += len(value)
    writeStringToFile(filename,stringFileContent)
    return len(pos_str_col)

'''
Method  ed_search(path, search_string) that searches for search_string
in all files in directory path and its immediate subdirectories using the
os.walk function.
'''
def ed_search(path, search_string):
    listProibitFiles = ['.DS_Store']
    listAbsoluteFileNames = []
    for dirname, dir_list, file_list in os.walk(path):
        for f in file_list:
            if f not in listProibitFiles:
                listIndexFound = ed_find(os.path.join(dirname,f),search_string)
                if len(listIndexFound) > 1:
                    listAbsoluteFileNames.append(os.path.join(dirname,f))
    return listAbsoluteFileNames


#unit test for append.
#this is superficial - it not deal with file I/o errors.
def test_append():
    test_name = "test_append"
    test_fn = "file1.txt"
    if os.path.isfile(test_fn):
        os.remove(test_fn)
    
    #write some initial content to the file
    initial_text = "ABCD"
    with open(test_fn, "w") as test_f:
        test_f.write(initial_text)
        
    #now test ed_append":
    try:
        new_text = "01234"
        #out test subject:
        ret = ed_append(test_fn,new_text)
        
        expected_text = initial_text + new_text
        
        # we need to check returned value and that the file has changed accordingly:
        current_text = open(test_fn, "r").read() #read the entire file
        
        #test the conditiou
        cond = (ret == len(new_text)) and (current_text == expected_text)
        
        return testif(cond, test_name)
    except Exception as exc:
        print("test {} failed due to exception: {}\n".format(test_name, str(exc)))
        
        
#unit test for replace.
def test_replace():
    test_name = "test_replace"
    test_fn = "file1.txt"
    if os.path.isfile(test_fn):
        os.remove(test_fn)
    
    #write some initial content to the file
    initial_text = "01234567890123456789"
    with open(test_fn, "w") as test_f:
        test_f.write(initial_text)
        
    #now test ed_append":
    try:
        new_text = "ABCDE"
        search_string = "345"
        #out test subject:
        ret = ed_replace(test_fn,search_string, new_text, 1)
        
        expected_text = "0123456789012ABCDE6789"
        
        # we need to check returned value and that the file has changed accordingly:
        current_text = open(test_fn, "r").read() #read the entire file
        
        #test the conditiou
        
        cond = (ret == 1) and (current_text == expected_text)
        
        return testif(cond, test_name)
    except Exception as exc:
        print("test {} failed due to exception: {}\n".format(test_name, str(exc)))
        
#unit test for replace.
def test_replace2():
    test_name = "test_replace2"
    test_fn = "file1.txt"
    if os.path.isfile(test_fn):
        os.remove(test_fn)
    
    #write some initial content to the file
    initial_text = "01234567890123456789"
    with open(test_fn, "w") as test_f:
        test_f.write(initial_text)
        
    #now test ed_append":
    try:
        new_text = "ABCDE"
        search_string = "345"
        #out test subject:
        ret = ed_replace(test_fn,search_string, new_text)
        
        expected_text = "012ABCDE6789012ABCDE6789"
        
        # we need to check returned value and that the file has changed accordingly:
        current_text = open(test_fn, "r").read() #read the entire file
        
        #test the conditiou
        
        cond = (ret == 2) and (current_text == expected_text)
        
        return testif(cond, test_name)
    except Exception as exc:
        print("test {} failed due to exception: {}\n".format(test_name, str(exc)))
        
        
#unit test for find.
def test_find():
    test_name = "test_find"
    test_fn = "file1.txt"
    if os.path.isfile(test_fn):
        os.remove(test_fn)
    
    #write some initial content to the file
    initial_text = "01234567890123456789"
    with open(test_fn, "w") as test_f:
        test_f.write(initial_text)
        
    #now test ed_append":
    try:
        new_text = "345"
        #out test subject:
        ret = ed_find(test_fn,new_text)
        
        expected_text = [3, 13]
                
        #test the conditiou
        cond = (ret == expected_text)
        
        return testif(cond, test_name)
    except Exception as exc:
        print("test {} failed due to exception: {}\n".format(test_name, str(exc)))
        
#unit test for find.
def test_find2():
    test_name = "test_find2"
    test_fn = "file1.txt"
    if os.path.isfile(test_fn):
        os.remove(test_fn)
    
    #write some initial content to the file
    initial_text = "01234567890123456789"
    with open(test_fn, "w") as test_f:
        test_f.write(initial_text)
        
    #now test ed_append":
    try:
        new_text = "356"
        #out test subject:
        ret = ed_find(test_fn,new_text)
        
        expected_text = []
                
        #test the conditiou
        cond = (ret == expected_text)
        
        return testif(cond, test_name)
    except Exception as exc:
        print("test {} failed due to exception: {}\n".format(test_name, str(exc)))
        

def test_read():
    test_name = "test_read"
    test_fn = "file1.txt"
    if os.path.isfile(test_fn):
        os.remove(test_fn)
    
    #write some initial content to the file
    initial_text = "01234567890123456789"
    with open(test_fn, "w") as test_f:
        test_f.write(initial_text)
        
    #now test ed_read":
    try:
        #out test subject:
        ret = ed_read(test_fn,3,9)
        
        expected_text = "345678"
        
        #test the conditiou
        cond = (str(ret) == str(expected_text))
        return testif(cond, test_name)
    except Exception as exc:
        print("test {} failed due to exception: {}\n".format(test_name, str(exc)))
        
def test_read2():
    test_name = "test_read2"
    test_fn = "file1.txt"
    if os.path.isfile(test_fn):
        os.remove(test_fn)
    
    #write some initial content to the file
    initial_text = "01234567890123456789"
    with open(test_fn, "w") as test_f:
        test_f.write(initial_text)
        
    #now test ed_read":
    try:
        #out test subject:
        ret = ed_read(test_fn,3)  
        expected_text = "34567890123456789"

        #test the conditiou
        cond = (str(ret) == str(expected_text))
        return testif(cond, test_name)
    except Exception as exc:
        print("test {} failed due to exception: {}\n".format(test_name, str(exc)))
        
        
#unit test for write.
def test_write():
    test_name = "test_write"
    test_fn = "file1.txt"
    if os.path.isfile(test_fn):
        os.remove(test_fn)
    
    #write some initial content to the file
    initial_text = "01234567890123456789"
    with open(test_fn, "w") as test_f:
        test_f.write(initial_text)
        
    #now test ed_append":
    try:
        new_text = ((2, "ABC"),(10, "DEFG"))
        #out test subject:
        ret = ed_write(test_fn,new_text)
        
        expected_text = "01ABC56789DEFG456789"
        
        # we need to check returned value and that the file has changed accordingly:
        current_text = open(test_fn, "r").read() #read the entire file
        
        #test the conditiou
        cond = (ret == 2) and (current_text == expected_text)
        
        return testif(cond, test_name)
    except Exception as exc:
        print("test {} failed due to exception: {}\n".format(test_name, str(exc)))
        
        
#unit test for write.
def test_write2():
    test_name = "test_write2"
    test_fn = "file1.txt"
    if os.path.isfile(test_fn):
        os.remove(test_fn)
    
    #write some initial content to the file
    initial_text = "01234567890123456789"
    with open(test_fn, "w") as test_f:
        test_f.write(initial_text)
        
    #now test ed_append":
    try:
        new_text = ((2, "ABC"), (30, "DEFG"))
        #out test subject:
        ret = ed_write(test_fn,new_text)
        
        expected_text = "01ABC56789DEFG456789"
        
        # we need to check returned value and that the file has changed accordingly:
        current_text = open(test_fn, "r").read() #read the entire file
        
        #test the conditiou
        cond = (ret == 2) and (current_text == expected_text)
        
        return testif(cond, test_name)
    except Exception as exc:
        print("test {} failed due to exception: {}\n".format(test_name, str(exc)))

#unit test for insert.
def test_insert():
    test_name = "test_insert"
    test_fn = "file1.txt"
    if os.path.isfile(test_fn):
        os.remove(test_fn)
    
    #write some initial content to the file
    initial_text = "01234567890123456789"
    with open(test_fn, "w") as test_f:
        test_f.write(initial_text)
        
    #now test ed_append":
    try:
        new_text = ((2, "ABC"), (10, "DEFG"))
        #out test subject:
        ret = ed_insert(test_fn,new_text)
        
        expected_text = "01ABC23456789DEFG0123456789"
        
        # we need to check returned value and that the file has changed accordingly:
        current_text = open(test_fn, "r").read() #read the entire file
        
        #test the conditiouprint(current_text, expected_text)
        cond = (ret == 2) and (current_text == expected_text)
        
        return testif(cond, test_name)
    except Exception as exc:
        print("test {} failed due to exception: {}\n".format(test_name, str(exc)))
        
#unit test for ed_search.
def test_search():
    test_name = "test_search"
    test_fn = "file2.txt"
    if os.path.isfile(test_fn):
        os.remove(test_fn)
    
    #write some initial content to the file
    initial_text = "Secret"
    with open(test_fn, "w") as test_f:
        test_f.write(initial_text)
        
    #now test ed_append":
    try:
        #out test subject:
        ret = ed_search(".","Secret")
        expected_text = ["./p2.py"]
        
        #test the conditiouprint(current_text, expected_text)
        cond = (ret == expected_text)
        
        return testif(cond, test_name)
    except Exception as exc:
        print("test {} failed due to exception: {}\n".format(test_name, str(exc)))


def main():
    fn = "file1.txt" #asssume this file does not exist yet.
       
    ed_clearContent(fn)
    
    print(ed_append(fn,"0123456789"))
    print(ed_append(fn,"0123456789\n"))
    print(ed_append(fn,"0123456789"))
    
    print(ed_search(".","ABC"))
        
    test_append()
    test_read()
    test_read2()
    test_find()
    test_find2()
    test_replace()
    test_replace2()
    test_write()
    test_write2() # test will fail with exception
    test_insert()
    test_search()
    


main()
