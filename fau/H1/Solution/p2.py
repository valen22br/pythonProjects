# Homework 1
# problem 2  solution

#
#  Do not distribute.
#

import math
import pylab

a = float(input("Enter a: "))

if a == 0:
    # this is now a linear equation and we can't apply the given formula:
    print("Cannot proceed with a==0")
    exit(1)    # terminate program
    # no need for else
    
b = float(input("Enter b: "))
c = float(input("Enter c: "))

delta = b * b - 4 * a * c

if delta < 0:
    print("no real solutions")
elif delta == 0:
    x = -b /(2 * a)
    print("one solutions", x)
else:
    x1 = (-b - math.sqrt(delta)) / (2 * a)
    x2 = (-b + math.sqrt(delta)) / (2 * a)
    print("two solutions: x1 =",x1,"x2 =",x2)


# graph:
xs = []
ys = []
# prepare the domain for the function we graph
x0 = -4.0    # lower bound
x1 = +4.0    # upper bound

n = 50                     # n points
dx = (x1 - x0) / n          # delta between points

x = x0

while x <= x1:
    xs.append(x)
    y = a * x**2 + b * x + c
    
    ys.append(y)
    x += dx

# after the loop:
pylab.plot(xs, ys, "b.-")    # creates the graph figure, but does not show it yet
pylab.title("{}x^2 + {}x + {}".format(a,b,c))
pylab.xlabel("x")
pylab.ylabel("y")

# draw axes:
pylab.axhline(0, color='black')
pylab.axvline(0, color='black')

pylab.show()     # what it says...

# end

