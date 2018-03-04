#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 10:46:32 2018

@author: valen
"""

class Employee():
    def __init__(self,name = "Gustavo", baseSalary = 10000, phoneNumber = "954- 651- 2821"):
        self.__name = str(name)
        self.__baseSalary = float(baseSalary)
        self.__phoneNumber = str(phoneNumber)
        
    def getName(self):
        return self.__name
    
    def getBaseSalary(self):
        return self.__baseSalary

    def getPhone(self):
        return self.__phoneNumber
    
    def salary_total(self):
        totalSalary = self.__baseSalary
        return totalSalary
    
    def setBaseSalary(self, newSalaryValue):
        self.__baseSalary = newSalaryValue
        
    def __str__(self):
        return ("{}(\"{}\",\"{}\", {})".format(self.__class__.__name__, self.getName(), self.getPhone(), self.salary_total()))
    
    def __repr__(self):
        #print(self.__str__())
        return("{}".format(self.__str__()))
    
class Manager(Employee):
    def __init__(self,name = "Gabi", baseSalary = 11000, phoneNumber = "954- 684- 2323", bonus = 0.0):
        Employee.__init__(self, name, baseSalary, phoneNumber)
        self.__bonus = bonus
        
    def getBonus():
        return self.__bonus
    
    def salary_total(self):
        totalSalary = Employee.getBaseSalary(self) + self.__bonus
        return totalSalary
        
    def __str__(self):
        result_str = Employee.__str__(self)
        #result str = result str + ' and mass {}'.format(self.mass) return result str
        return (result_str)
    
class Cfo(Manager):
    def __init__(self,name = "Gabi", baseSalary = 11000, phoneNumber = "954- 684- 2323", bonus = 0.0, stockOptions = 0.0):
        Manager.__init__(self, name, baseSalary, phoneNumber, bonus)
        self.__stockOptions = stockOptions
        
    def getStockOptions():
        return self.__stockOptions
    
    def salary_total(self):
        totalSalary = Manager.salary_total(self) + self.__stockOptions
        return totalSalary
    
    def __str__(self):
        result_str = Manager.__str__(self)
        return(result_str)
    
def main():
    p = Employee()
    #print(dir(p))
    m = Manager("Gabi", 15000, "9546 542 151", 2000)  
    c = Cfo("Luis", 20000, "954 656 2323", 5000, 5000)
    print(p)
    print(m)
    print(c)
main()
