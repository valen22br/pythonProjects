# Python Programming.
# Homework 3, problem 2
# Instructor: Dr. Ionut Cardei
# Do not distribute.

# Pythagorean Numbers

import math
from testif import testif


def get_hyp(a, b, n):
    """Returns [h] if (a,b,h) are Pythagorean numbers and h is an integer and h<=n.
    Returns [] otherwise.
    """
    h2 = a*a + b*b
    h = math.sqrt(h2)
    return [int(h)] if h <= n and h == int(h) else []


def compute_Pythagoreans(n):
    """Returns a list of tuples (a,b,c) of Pythagorean numbers s.t. 0<a,b,c<=n.
    If n<=0 it return the empty list. The complexity class is O(n^2).
    """
    if n<=0:
        return []

    # we make c iterate through a list with one element (a valid integer
    #   hypotenuse) or with no elements [], if (a,b,c) can't be a valid
    #   Pythagorean triple:
    lst = [(a,b,c) for a in range(1, n-2) for b in range(1,n-2)
           for c in get_hyp(a, b, n)]
    # other valid solutions are possible, too.
    
    return lst


# a straightforward version that has O(n^3) complexity -- very slow.
def compute_Pythagoreans_VERY_INEFICIENT(n):
    return [(a,b,c) for a in range(1,n+1) for b in range(1,n+1) for c in range(1,n+1)
            if a*a+b*b==c*c]

## ------------------ testing code:

def reduce_and(bool_iter):
    """Computes AND over a collection (an iterable) of bool values ."""
    val = True
    for b in bool_iter:
        val = val and b
    return val


if __name__ == "__main__":    # in top program ?
    # case good n:
    n = 100
    lst1 = compute_Pythagoreans(n)
    print("for n={} it finds {} tuples:".format(n, len(lst1)))
    print(lst1)

    # check that all tuples are Pythagorean:
    check_lst = [ a*a+b*b==c*c for (a,b,c) in lst1]   # we expect a list of TRUE values
    testif(reduce_and(check_lst), "testing up to {}".format(n))

    # case with empty list:
    n = 4
    testif([] == compute_Pythagoreans(n), "testing empty list for n={}".format(n))


    # failure case:
    n = -4
    testif([] == compute_Pythagoreans(n), "testing empty list for n={}".format(n))

