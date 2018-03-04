#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 12:21:42 2018

@author: valen
"""
class Poly(object):
    """ Polynomials class. """
    def __init__(self,listCoefficients):
        
        self.listFloatCoefficients = []
        for i in listCoefficients:
            self.listFloatCoefficients.append(float(i))
        self.polyDegree = len(self.listFloatCoefficients)
       
    def __str__(self):
        """ print 'In __str__ method """
        #print("in __str__ method")  
        stringResult = ""
        intCoefficient = 0;
        stringSign = ""
        sringXvariable = ""
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

    def __repr__(self):
        #print("in __repr__ method")  
        print(self.__str__())
        return("{}".format(self.__str__()))
        
    def __eq__(self, other):
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            return self.listFloatCoefficients == other.listFloatCoefficients
        
    def __ne__(self, other):
        if self is other:
            return False
        elif type(self) != type(other):
            return True
        else:
            return self.listFloatCoefficients != other.listFloatCoefficients
        
    def __add__(self,other):
        print("in __add__ method")
        newSumList = []
        
        """ if the lengths of the list are equal, use comprehension to create the sum of the values of the lists """
        if(len(self.listFloatCoefficients) == len(other.listFloatCoefficients)):
            newSumList = [(x+y) for x, y in zip(self.listFloatCoefficients, other.listFloatCoefficients)]
        else:

            """ Swap values to let self,ListFloatCoefficients will be the biggest one """            
            if(len(self.listFloatCoefficients) < len(other.listFloatCoefficients)):
                self.listFloatCoefficients, other.listFloatCoefficients = other.listFloatCoefficients, self.listFloatCoefficients
    
            
            sumListDict = {}
            
            print(self.listFloatCoefficients)
            print(other.listFloatCoefficients)
            
            for i in range(len(self.listFloatCoefficients)):
                print("i=> ", i)
                print(self.listFloatCoefficients[i])
                if(i in sumListDict):
                    sumListDict[i] += self.listFloatCoefficients[i]
                else:
                    sumListDict[i] = self.listFloatCoefficients[i]
            for j in range(len(other.listFloatCoefficients)):
                if(j in sumListDict):
                    sumListDict[j] += other.listFloatCoefficients[j]
                        #print(other.listFloatCoefficients[i])
                    """
                    else:
                        sumListDict[j] = other.listFloatCoefficients[j]
                    """
            print(sumListDict)
            for key, value in sumListDict.items():
                newSumList.append(value)
        
        
        #print(self.listFloatCoefficients)
        #print(other.listFloatCoefficients)
        #print(newSumList)
        sumResult = Poly(newSumList)
        return(sumResult)
    
        

def main():
    p1 = Poly([1, -2, -4])     
    p2 = Poly([0,0,0,0,0,0,0,0,0,0,0,0,0,-6, 0, 0,0,0,0,0,-101])
    p3 = Poly([5,6,-7])
    p4 = Poly([0])
    p5 = Poly([1, -2, -4])  
    
    """
    print(p2)
    repr(p1)
    repr(p3)
    repr(p5)
    
    print(p1 == p2)
    print(p1 == p5)
    print(p5 == Poly((1, -2, -4)))
    
    print(p1 != p2)
    print(p1 != p5)
    """
    print("p1=> ",p1)
    print("p2=> ", p2)
    p3 = p2 + p1
    print("sum=>",p3)


    """
    print(p1)    
    print(p2)
    print(p3)
    print(p4)
    """
    
main()
