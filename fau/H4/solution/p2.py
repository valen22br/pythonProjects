# Python Programming.
# Homework 4, problem 2
# Instructor: Dr. Ionut Cardei
# Do not distribute.

from testif import testif
import pylab

class Poly:
    def __init__(self, coeffs):
        """Constructor. Saves the coeffs to a list. It cuts coefficients==0 above the polynomial degree.
        May throw ValueError if list is empty or conversion to float fails.
        precondition: coeffs is nonempty list of int/floats
        """
        if len(coeffs) == 0:
            raise ValueError("Poly.__init__ error: empty list of coefficients.")
        self.__coeffs = [float(c) for c in coeffs]
        # not required: remove coefficients==0 above the polynomial degree. Saves space.
        i = len(self.__coeffs) - 1
        while (i > 0 and self.__coeffs[i] == 0):
            del self.__coeffs[i]
            i -= 1


    def degree(self):
        return len(self.__coeffs) - 1

    def __str__(self):
        """Generate string with coefficients. May throw IndexError"""
        # !!! For grading, simply printing the list with coefficients is enough.
        
        c0 = str(self.__coeffs[0])    # may throw INdexError
        coeffs_lst = [c0]
        for i in range(1, len(self.__coeffs)):
            expo = "" if i == 1 else "^{}".format(i)
            if self.__coeffs[i] == 1:
                c = "+X{}".format(expo)
            elif self.__coeffs[i] == -1:
                c = "-X{}".format(expo)
            elif self.__coeffs[i] !=0:
                c = "{:+f}X{}".format(self.__coeffs[i], expo)
            if self.__coeffs[i] !=0:
                coeffs_lst.append(c)
        return "".join(coeffs_lst)

    def __repr__(self):
        """Representation."""
        return str(self)

    def __getitem__(self, k):
        """Returns the coefficient a_k. Throws IndexError if not 0<=k<=self.degree()"""
        if not 0 <= k <= self.degree():
            raise IndexError("Poly.__getitem__: error, invalid coefficient degree {}.".format(k))
            # !!! For grading, it is OK to raise ValueError instead of IndexError.
        return self.__coeffs[k]

    def __add__(self, q):
        """Addition with polynomial q. Although not required, we show how to add with a number.
           precondition: q is a Poly or int or float"""
        if type(q) == Poly:
            if len(self.__coeffs) > len(q.__coeffs):
                long = self
                short = q
            else:
                long = q
                short = self
            sum_coeffs = long.__coeffs[:]     # we need a copy !
            for i in range(len(short.__coeffs)):
                sum_coeffs[i] += short.__coeffs[i]
            return Poly(sum_coeffs)
        elif type(q) == int or type(q) == float:
            return self + Poly([q])  # recursive call, will add with polynomial (first case)
        else:
            raise TypeError("Poly.__add__ error: parameter {} not a Poly or a number.".format(q))
        

    
    def __radd__(self, q):
        """Addition.
        precondition: q is a Poly or int or float"""
        return self + q

        
    def __mul__(self, q):
        """Multiplication with polynomial q. 
           precondition: q is a Poly or int or float"""
        if type(q) == Poly:
            prod_coeffs = [0] * (self.degree() + 1) * (q.degree() + 1)   # list with product coefficients
            for i in range(self.degree() + 1):
                for j in range(q.degree() + 1):
                    prod_coeffs[i+j] += self[i] * q[j]
            return Poly(prod_coeffs)
        elif type(q) == int or type(q) == float:
            return self * Poly([q])  # recursive call, will multiply with polynomial (first case)
        else:
            raise TypeError("Poly.__mul__ error: parameter {} not a Poly or a number.".format(q))


    def __rmul__(self, q):
        """Multiplication with polynomial q, with reversed param order.
           precondition: q is a Poly or int or float"""
        return self * q


    def __eq__(self, q):
        """Equality operator."""
        return (type(q) == type(self)) and (self.degree() == q.degree()) and (self.__coeffs == q.__coeffs)


    def eval(self, x):
        """Evaluates the polynomial P(x) for parameter x.
           precondition: x is a number or an iterable collection of numbers.
        """
        if type(x) == int  or type(x) == float:
            n = self.degree()
            y = self[n]
            for i in range(n-1, -1, -1):
                y = y * x + self[i]
            return y
        else:            # assume it's an iterable, such as a tuple or list, or a generator
            return [self.eval(elem) for elem in x]    # we return a list

    def graphit(self, xseq):
        """Displays the chart of the polynomial using domain given by iterable number collection xseq.
        precondition: xseq is iterable collection of numbers.
        """
        yseq = self.eval(xseq)
        pylab.plot(xseq, yseq, "r-", label=str(self))
        pylab.legend()
        pylab.show()
        
    
def run_tests():
    l1 = [-1, 2, 1]
    p1 = Poly(l1)
    l11 = [-1, 2, 1]
    p11 = Poly(l11)

    l2 = [3, 0, -1, 2]
    p2 = Poly(l2)
    
    a = 3.0
    p1a = Poly( [a + l1[0]] + l1[1:])

    p2a = Poly( [a*c for c in l2] )   # a * p2
    
    ps = Poly([2, 2, 0, 2])
    pp = Poly([-3, 6, 4, -4, 3, 2])

    x = 2.0
    y1 = 7.0
    y2 = 15.0

    xs = [-1, 0, 1, 2]
    y1s = [-2, -1, 2, 7]

    testif(p1 == p11, "eq")
    testif(p1 != p2, "ne")
    testif(p1 + p2 == ps, "add")
    testif(p1 + a == p1a, "add + {}".format(a))
    testif(a + p1 == p1a, "{} + add".format(a))

    testif(p1 * p2 == pp, "mul")
    testif(p2 * a == p2a, "mul * {}".format(a))
    testif(a * p2 == p2a, "{} * mul".format(a))

    testif(p1.eval(x) == y1, "eval p1")
    testif(p2.eval(x) == y2, "eval p2")

    testif(p1.eval(xs) == y1s, "eval p1 with list")


def test_graphit():
    l1 = [-1, 2, 1]
    p1 = Poly(l1)
    l2 = [3, 0, -1, 2]
    p2 = Poly(l2)

    xs = [-4 + 0.1 * i for i in range(0,100)]
    p1.graphit(xs)
    p2.graphit(xs)
    (p1 * p2).graphit(xs)
        
def main():
    run_tests()
    test_graphit()

if __name__ == "__main__":
    main()

