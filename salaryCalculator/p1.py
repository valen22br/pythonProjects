#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 20:23:06 2018

@author: Luis Gustavo Grubert Valensuela
z23351882
lvalensuela2015@fau.edu
HOMEWORK 1.1
"""

print("\t This program determines the weekly salary for an employee. The salary \n\
      is the sum of the hourly rate times the hours worked, plus the bonus.\n\
      For work hours exceeding 40 per week, an overtime rate \n\
      of 1.5 is applied. The user must indicate if the worker has received a \n\
      bonus by answering a y/n question. \n\
      Input consists of: hours worked, hourly rate, bonus. \n\
      The output is the total salary for this week.")

hours_worked_str = input ("Enter the number of hours worked this week: ")
hours_worked_int = int(hours_worked_str)

total_salary_float, overtime_value_float = 0.0, 0.0;

hour_salary_str = input("Enter the salary rate per hour (do not include the \
                                                         '$' sign): ")
hour_salary_float = float(hour_salary_str)

got_bonus_str = input("Did the worker get a bonus ? (y/n) ")

if (got_bonus_str == 'y'):
    bonus_value_str = input("Enter Bonus: ")
    bonus_value_int = float(bonus_value_str)
    total_salary_float += bonus_value_int
    
if(hours_worked_int > 40):
    total_salary_float += 40 * hour_salary_float
    overtime_value_float = (hours_worked_int - 40) * hour_salary_float * 1.5
    total_salary_float += overtime_value_float
else:
    total_salary_float = hours_worked_int * hour_salary_float
    
print("The total salary is $", str(total_salary_float), " overtime pay $" + str(overtime_value_float));
