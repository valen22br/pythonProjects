# Python Programming.
# Homework 2, problem 1
# Instructor: Dr. Ionut Cardei
# Do not distribute.

# a) The algorithm:
# 1.  read string n_str from terminal
# 2.  convert n_str to int n
# 3.  if conversion fails or n <=0,
# 3.1    print error message: "Error: n must be positive integer"
# 3.2    exit program
# 4.  for a=1, a<=n, a++
# 4.1    for b=1, a<=int(sqrt(n*n - a*a)), a++
# 4.1        hyp_sq = a**2 + b**2
# 4.2        c = sqrt(hyp_sq)
# 4.3        if c == int(sqrt(hyp_sq))
# 4.3.1          print(a,b,c)


# now in Python:

import math

n_str = input("Enter n: ")
# assume this represents an int number
n = int(n_str)    # ... so this expression succeeds.

if (n < 0):
    print("Error: n must be positive integer")
    exit(1)

for a in range(1, n+1):
    bmax = int(math.sqrt(n**2 - a**2))
    for b in range(1, bmax + 1):
        hyp_sq = a**2 + b**2
        c_float = math.sqrt(hyp_sq)

        # if c is an int (a whole number):
        if c_float == int(math.sqrt(hyp_sq)):
            # no need to check for c<=n since b is limited
            c = int(c_float)
            print(a, b, c)

