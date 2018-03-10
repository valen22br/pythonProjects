# Homework 1
# Solution to problem 1

#
#  Do not distribute.
#

# good style to use a variable and not a numeric literal, in case Congress
# votes to reduce the federal work week...
weekly_hours = 40   
overtime_scale = 1.5

# strings enclosed in """ (or ''') preseve format, like newlines
print("""This program determines the weekly salary for an employee.
The salary is the sum of the hourly rate times the
hours worked, plus the bonus.
For work hours exceeding 40 per week, an overtime rate
of 1.5 is applied.
The user must indicate if the worker has received a
bonus by answering a y/n question.
Input consists of: hours worked, hourly rate, bonus.
The output is the total salary for this week.""")

hours = float(input("Enter the number of hours worked this week: "))
rate = float(input("Enter the salary rate per hour (do not include the '$' sign): "))
has_bonus = input("Did the worker get a bonus ? (y/n) ")

if has_bonus.lower() == "y":
    bonus = float(input("Enter bonus: "))
else:
    bonus = 0

# now compute the salary:
overtime_pay = 0
weekly_pay = 0
if hours > weekly_hours:
    overtime_pay = (hours - weekly_hours) * rate * overtime_scale
    weekly_pay = weekly_hours * rate
else:
    weekly_pay = hours * rate
    
salary = weekly_pay + overtime_pay + bonus
print("The total salary is", salary,"(overtime pay", overtime_pay, ")")
