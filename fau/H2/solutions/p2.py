# Python Programming.
# Homework 2, problem 2
# Instructor: Dr. Ionut Cardei
# Do not distribute.

# part a)
# This file presents two versions of the algorithm.

# The algorithm look for non-overlapping subsctrings.

# Version 1 is the direct approach:

# 1.  function find_dup_str(s, n)
# 2.    foundss = ""
#       # index i marks the start of the substring to look for
# 3.    for i=0; i<=len(s) - 2 * n and foundss=="";  i++
#          # start looking at j:
# 3.1      for j=i+n; j<len(s)-n and  foundss==""; j++
#             # compare s[i:i+n] with s[j:j+n]:
# 3.1.1       for k=0; k<n and s[j + k] == s[i + k]; k++    # no loop body 
#             # did we find all n characters equal ?
# 3.1.2       if k == n
# 3.1.2.1        foundss = s[i:i+n]    # slice with substring of length n to return
# 4.    return foundss


# Version 2 does the same thing but breaks down the problem and relies on a
#   function find_substring to find a substring starting from a position:

# 1.  function find_dup_str(s, n)
# 2.    foundss = ""
# 3.    for i=0; i<=len(s) - n; i++
# 3.1       subs = s[i:i+n]     # get the current substring of length n using slice
# 3.2       # find the first index of subs in s, starting from index i+n:
# 3.3       m = find_substring(s, subs, i+n)   
# 3.4       if m > 0
# 3.4.1        foundss = subs
# 3.4.2        break
# 4.    return foundss    # either the n-size substring or "" if not found


# find_substring() searches for a substring in a string s starting from
# position with index start_index;
# returns index >0 where found, or -1 if not found

# 1.   function find_substring(s, substring, start_index)
# 2.     found_index = -1    # -1 means not found yet
# 3.     for i=start_index; i<len(s) - len(substring) and found_index == -1; i++
# 3.1        j = 0   # iterate through substring's characters
# 3.2        while j < len(substring) and s[i+j] == substring[j]
# 3.3.1         j = j + 1
# 3.4        if j == len(substring)
# 3.5           found_index = i
# 4.     return found_index


def find_dup(s, n):
    foundss = ""
    # index i marks the start of the substring to look for
    i = 0
    while i <= len(s) - 2*n and foundss == "":
        j = i + n
        while j <= len(s) - n and foundss == "":
            # compare up to n chars from index i with  k chars from index j: 
            k = 0
            while k < n and s[i + k] == s[j + k]:
                k = k + 1
            # did we find all n characters equal ?
            if k == n:
                foundss =  s[i:i+n]    # slice with substring of length n to return
            j = j + 1
        i = i + 1
    return foundss



def testif(b, testname, msgOK="", msgFailed=""):
    """Function used for testing. 
    param b: boolean, normally a tested condition: true if test passed, false otherwise
    param testname: the test name
    param msgOK: string to be printed if param b==True  ( test condition true)
    param msgFailed: string to be printed if param b==False
    returns b
    """
    if b:
        print("Success: "+ testname + "; " + msgOK)
    else:
        print("Failed: "+ testname + "; " + msgFailed)
    return b

# part b)

# main program:

s = input("Enter string: ")
n = int(input("Enter n: "))
print("Found substring of length {}: '{}'".format(n, find_dup(s, n)))

# more testing:
s1 = "abCDEfCDEghi"
testif(find_dup(s1, 1) == "C", "find 1")
testif(find_dup(s1, 2) == "CD", "find 2")
testif(find_dup(s1, 3) == "CDE", "find 3")
for i in range(4, len(s1)+4):
    testif(find_dup(s1, i) == "", "find " + str(i))

# test boundary case:
testif(find_dup("123456734567", 5) == "34567", "find 5, boundary case")


s2 = "0123456789"
testif(find_dup(s2, 1) == "", "not found 1")
testif(find_dup(s2, 2) == "", "not found 2")
testif(find_dup(s2, 6) == "", "not found 6")

testif(find_dup("", 1) == "", "not found '' 1")
testif(find_dup("", 2) == "", "not found '' 2")
testif(find_dup("", 6) == "", "not found '' 6")


# part c)

# Algorithm for find_max_dup:

# function find_max_dup(s)
# 1.  maxss = ""
# 2.  for n=len(s) / 2; n>=1 and maxss==""; n--
# 2.1   maxss = find_dup(s, n)
# 3.   return maxss


# part d)
def find_max_dup(s):
    n = len(s) // 2
    maxss = ""
    while n >= 1 and maxss == "":
        maxss = find_dup(s, n)
        n = n - 1
    return maxss


s = input("Enter string: ")
maxss = find_max_dup(s)
print("Found maximal duplicated substring '{}' of length {}".format(maxss, len(maxss)))


# more testing:
testif(find_max_dup(s1) == "CDE", "find_max_dup s1")
testif(find_max_dup(s2) == "", "find_max_dup s2")

