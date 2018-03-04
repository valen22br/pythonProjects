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
    Implementation of a class hierarchy for employees in a startup company. 
    The base class is Employee. This has subclasses Manager, Engineer. Class    
    Manager has a subclass called CEO.
*******************************************************************************
"""

"""
Class Employee: Main class to represent a employee
Arguments:
    str name
    float baseSalary
    str phoneNumber
"""
class Employee():
    def __init__(self,name = "Gustavo", baseSalary = 10000, phoneNumber = "954- 651- 2821"):
        self.__name = str(name)
        self.__baseSalary = float(baseSalary)
        self.__phoneNumber = str(phoneNumber)
    """ Acessor Method """
    def getName(self):
        return self.__name
    """ Acessor Method """
    def getBaseSalary(self):
        return self.__baseSalary
    """ Acessor Method """
    def getPhone(self):
        return self.__phoneNumber
    """ Mutator Method """
    def salary_total(self):
        totalSalary = self.__baseSalary
        return totalSalary
    """ Mutator Method """
    def setBaseSalary(self, newSalaryValue):
        self.__baseSalary = newSalaryValue
    """ __str__ method (print) """    
    def __str__(self):
        return ("{}(\"{}\",\"{}\", {})".format(self.__class__.__name__, self.getName(), self.getPhone(), self.salary_total()))
    """ __repr__ method (reresentation) """
    def __repr__(self):
        #print(self.__str__())
        return("{}".format(self.__str__()))

"""
Class Manager: Main class to represent a Manager
it inherits class Employee
Arguments:
    float bonus
"""
class Manager(Employee):
    def __init__(self,name = "Gabi", baseSalary = 11000, phoneNumber = "954- 684- 2323", bonus = 0.0):
        Employee.__init__(self, name, baseSalary, phoneNumber)
        self.__bonus = bonus
    """ Acessor Method """
    def getBonus():
        return self.__bonus
    """ Mutator Method """
    def salary_total(self):
        totalSalary = Employee.getBaseSalary(self) + self.__bonus
        return totalSalary
    """ __str__ method (print) """   
    def __str__(self):
        result_str = Employee.__str__(self)
        #result str = result str + ' and mass {}'.format(self.mass) return result str
        return (result_str)
"""
Class Engineer: Main class to represent a Engineer
it inherits class Employee
Same arguments of Class Employee
"""    
class Engineer(Employee):
    def __init__(self,name = "Gustavo", baseSalary = 10000, phoneNumber = "954- 651- 2821"):
        Employee.__init__(self,name, baseSalary, phoneNumber)
"""
Class Cfo: Main class to represent a CFO
it inherits class Manager
Arguments:
    float stockOptions
"""
class Cfo(Manager):
    def __init__(self,name = "Gabi", baseSalary = 20000, phoneNumber = "954- 684- 2323", bonus = 2500, stockOptions = 2500):
        Manager.__init__(self, name, baseSalary, phoneNumber, bonus)
        self.__stockOptions = stockOptions
    """ Acessor Method """
    def getStockOptions():
        return self.__stockOptions
    """ Mutator Method """
    def salary_total(self):
        totalSalary = Manager.salary_total(self) + self.__stockOptions
        return totalSalary
    """ __str__ method (print) """   
    def __str__(self):
        result_str = Manager.__str__(self)
        return(result_str)
"""Function that takes a list of objcts and prints it's content one by line """        
def print_staff(listObjects):
    for i in listObjects:
        print(i)
"""
main function that will concentrate the main execution of the program.
""" 
def main():
    p = Employee()
    e = Engineer("Jeff", 10000, "954 656 2314")
    #print(dir(p))
    m = Manager("Gabi", 15000, "9546 542 151", 2000)  
    c = Cfo("Luis", 20000, "954 656 2323", 5000, 5000)
    a = Cfo()
    """
    print(p)
    print(m)
    print(c)
    print(e)
    print(repr(p))
    print(repr(m))
    print(repr(c))
    print(repr(e))
    """
    print_staff((p,m,c,e, a))
    
    p.setBaseSalary(11111)
    m.setBaseSalary(22222)
    c.setBaseSalary(33333)
    e.setBaseSalary(44444)
    a.setBaseSalary(55555)
    
    print("\n")
    print_staff((p,m,c,e, a))
    
main()
