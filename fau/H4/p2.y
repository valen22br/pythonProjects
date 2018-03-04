#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 10:29:53 2018

@author: Luis Gustavo Grubert Valensuela
*******************************************************************************
Name: Luis Gustavo Grubert Valensuela Z#:23351882 lvalensuela2015@fau.edu
Course: Python Programming COP 4045-001 Spring 2018
Professor: Dr. Ionut Cardei
Due Date:03/04/2018             Due Time: 11:30PM
Assignment Homework 3
Last Changed: 03/04/2018
Description:
This assingment will create a class Poly that will be able to execute
    operations to polynomials.     
*******************************************************************************
"""

"""
Class Poly: Main class to represent a polynomial
"""
class Poly(object):
    """ Constructor method """
    def __init__(self,listCoefficients):
        
        self.listFloatCoefficients = []
        for i in listCoefficients:
            self.listFloatCoefficients.append(float(i))
        self.polyDegree = len(self.listFloatCoefficients)
       
    """ __str__ method (print) """
    def __str__(self):
        """ print 'In __str__ method """
        stringResult = ""
        intCoefficient = 0;
        stringSign = ""
        stringAvalue = ""
        for i in self.listFloatCoefficients:
            if(i != 0):
                if(intCoefficient == 0):
                    if(i > 0):
                        stringResult += str(i)
                else:
                    if(i > 0):
                        stringSign = "+"
                    else:
                        stringSign = ""
                    if(intCoefficient == 1):
                        stringXvariable = "X"
                    else:
                        stringXvariable = "X^"+str(intCoefficient)
                    if(1 > 0):
                            stringAvalue = str(i)
                    stringResult += stringSign+stringAvalue+stringXvariable
                
                stringSign = ""
                stringXvariable = ""
                stringAvalue = ""
            else:
                intCoefficient += 1
                continue
            intCoefficient += 1
        return("{}".format(stringResult))

    """ __repr__ method (Representation of the Class """
    def __repr__(self):
        #print("in __repr__ method")  
        print(self.__str__())
        return("{}".format(self.__str__()))

    """ __eq__ method (Equal method) """
    def __eq__(self, other):
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            return self.listFloatCoefficients == other.listFloatCoefficients

    """ __ne__ method (Not Equal method) """ 
    def __ne__(self, other):
        if self is other:
            return False
        elif type(self) != type(other):
            return True
        else:
            return self.listFloatCoefficients != other.listFloatCoefficients

    """ __add__ method (Addition method) """
    def __add__(self,other):
        #print("in __add__ method")
        newSumList = []
        
        """ if the lengths of the list are equal, use comprehension to create the sum of the values of the lists """
        if(len(self.listFloatCoefficients) == len(other.listFloatCoefficients)):
            newSumList = [(x+y) for x, y in zip(self.listFloatCoefficients, other.listFloatCoefficients)]
        else:

            """ Swap values to let self,ListFloatCoefficients will be the biggest one """            
            if(len(self.listFloatCoefficients) < len(other.listFloatCoefficients)):
                self.listFloatCoefficients, other.listFloatCoefficients = other.listFloatCoefficients, self.listFloatCoefficients
    
            sumListDict = {}
            
            for i in range(len(self.listFloatCoefficients)):
                if(i in sumListDict):
                    sumListDict[i] += self.listFloatCoefficients[i]
                else:
                    sumListDict[i] = self.listFloatCoefficients[i]
            for j in range(len(other.listFloatCoefficients)):
                if(j in sumListDict):
                    sumListDict[j] += other.listFloatCoefficients[j]
            
            for key, value in sumListDict.items():
                newSumList.append(value)
        
        sumResult = Poly(newSumList)
        return(sumResult)
    
    """ __rmull__ method (Multiplication method) """
    def __rmul__(self, other):
        #print("in __rmult__ method")
        #print(type(other))
        
        sumListDict = {}
        newSumList = []
        
        if(type(other) == int or type(other) == float):
            print("aeeeee")
            
            for i in range(len(self.listFloatCoefficients)):
                if(i in sumListDict):
                    sumListDict[i] += self.listFloatCoefficients[i] * other
                else:
                    sumListDict[i] = self.listFloatCoefficients[i] * other
                    
                    
        for key, value in sumListDict.items():
            newSumList.append(value)
  
        sumResult = Poly(newSumList)
        return(sumResult) 

    """ __mull__ method (Multiplication method) """
    def __mul__(self, other):
        #print("in __mult__ method")
        #print(type(other))
        
        sumListDict = {}
        newSumList = []
        
        if(type(other) == int or type(other) == float):
            for i in range(len(self.listFloatCoefficients)):
                if(i in sumListDict):
                    sumListDict[i] += self.listFloatCoefficients[i] * other
                else:
                    sumListDict[i] = self.listFloatCoefficients[i] * other
            
        else:            
            """ Swap values to let self,ListFloatCoefficients will be the biggest one """            
            if(len(self.listFloatCoefficients) < len(other.listFloatCoefficients)):
                self.listFloatCoefficients, other.listFloatCoefficients = other.listFloatCoefficients, self.listFloatCoefficients
                      
            for i in range(len(self.listFloatCoefficients)):
                if(i in sumListDict):
                    sumListDict[i] += self.listFloatCoefficients[i] * other.listFloatCoefficients[0]
                else:
                    sumListDict[i] = self.listFloatCoefficients[i] * other.listFloatCoefficients[0]
    
            for j in range(1,len(other.listFloatCoefficients)):
                for i in range(len(self.listFloatCoefficients)):
                    if(i+j in sumListDict):
                        sumListDict[i+j] += self.listFloatCoefficients[i] * other.listFloatCoefficients[j]
                    else:
                        sumListDict[i+j] = self.listFloatCoefficients[i] * other.listFloatCoefficients[j]
    
        for key, value in sumListDict.items():
            newSumList.append(value)
            
        sumResult = Poly(newSumList)
        return(sumResult) 

    """ __rmull__ method (Get Index method) """
    def __getitem__(self, other):
        #print("==> ", other)
        try:
            return self.listFloatCoefficients[other]
        except:
            return "ValueError"
    """ evalAuxiliary() method (Auxiliary method for evaluate a polynomial) """
    def evalAuxiliary(self, listValue = []):
        #print("in __evalAuxiliary__ method")  
        intCoefficient = 0;
        resultFloat = 0
        for i in self.listFloatCoefficients:
            if(i != 0):
                if(intCoefficient == 0):
                    if(i > 0):
                        resultFloat += i
                else:
                    if(intCoefficient == 1):
                        resultFloat += listValue*i
                    else:
                        resultFloat += pow(listValue, intCoefficient)*i
            else:
                intCoefficient += 1
                continue
            intCoefficient += 1
        return("{}".format(resultFloat))  
    
    """ eval() method (Eval method for evaluate a polynomial) """
    def eval(self, listValue):
        #print("in __eval__ method")  
        if(type(listValue) == list or type(listValue) == tuple):
            listResultsFloat = [self.evalAuxiliary(i) for i in listValue]
            return("{}".format(listResultsFloat))
        else:
            print(self)
            intCoefficient = 0;
            resultFloat = 0
            for i in self.listFloatCoefficients:
                if(i != 0):
                    if(intCoefficient == 0):
                        if(i > 0):
                            resultFloat += i
                    else:
                        if(intCoefficient == 1):
                            resultFloat += listValue*i
                        else:
                            resultFloat += pow(listValue, intCoefficient)*i
                else:
                    intCoefficient += 1
                    continue
                intCoefficient += 1
            return("{}".format(resultFloat))

"""
main function that will concentrate the main execution of the program.
""" 
def main():
    p1 = Poly([1, -2, -4])     
    p2 = Poly([0,0,0,0,0,0,0,0,0,0,0,0,0,-6, 0, 0,0,0,0,0,-101])
    p7 = Poly([5,6,-7])
    p4 = Poly([0])
    p5 = Poly([1, -2, -4]) 
    p6 = Poly((0,1))
    
    print("p1=> ",p1)
    print("p2=> ", p2)
    p3 = p2 + p1
    print("sum=>",p3)
    
    print("\n")
    print("p1=> ",p1)
    print("p6=> ", p6)
    p3 = p1 * p6
    print("mul=>",p3)

    print("\n")
    print("p1=> ",p1)
    print("p5=> ", p5)
    p3 = p1 * p5
    print("mul=>",p3)
   
    print("\n")
    print("p6=> ",p6)
    print("p6=> ",p6)
    p3 = p6 * p6
    print("mul=>",p3)
    
    print("\n")
    print("p1=> ",p1)
    print("p7=> ",p7)
    p3 = p1 * p7
    print("mul=>",p3)    
   
    print("\n")
    print("p6=> ",p6)
    print("eval=> 10 => ",p6.eval(10))
    
    print("\n")
    print("p5=> ",p5)    
    print("eval=> -1 => ",p5.eval(-1))
    
    print("\n")
    print("p5=> ",p5)    
    print("eval=> -2 => ",p5.eval(-2))
    
    print("\n")
    print("p1=> ",p1)    
    print("eval=> -1 => ",p1.eval(-1))

    print("\n")
    print("p1=> ",p1)    
    print("eval=> [0,-1,1] => ",p1.eval([0,-1,1]))     
    
main()
