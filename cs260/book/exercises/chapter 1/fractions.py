import unittest

def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

#implement __mul__, __div__, __sub__, __gt__, __lt__
class Fraction:
    def __init__(self,top,bottom):
        """Assign numerator and denominator values"""
        self.num = top
        self.den = bottom

    def __str__(self):
        """Return stringified value of the fraction"""
        return str(self.num)+"/"+str(self.den)

    def show(self):
        """Print current value of fraction"""
        print(self.num,"/",self.den)

    def __add__(self,other):
        """Operator overload for adding to another fraction"""
        if(type(other) == Fraction):
            newnum = self.num*other.den + \
            self.den*other.num
            newden = self.den * other.den
            common = gcd(newnum,newden)
            return Fraction(newnum//common,newden//common)
        elif(type(other) == int):
            newnum = self.den * other + self.num
            return Fraction(newnum,self.den)
        else:
            raise ValueError("A fraction can only be added with an Integer or another fraction.")

    def __mul__(self,other):
        """Operator overload for multiplication"""
        if(type(other) == Fraction):
            #multiply fractions
        elif(type(other) == int):
            #multiply fraction with int
        else:
            raise ValueError("A fraction can only be added with an Integer or another fraction.")

    def __div__(self,other):
        """Operator overload for division"""
        if(type(other) == Fraction):
            #multiply fractions
        elif(type(other) == int):
            #multiply fraction with int
        else:
            raise ValueError("A fraction can only be added with an Integer or another fraction.")

    def __sub__(self,other):
        """Operator overload for subtraction"""
        if(type(other) == Fraction):
            #multiply fractions
        elif(type(other) == int):
            #multiply fraction with int
        else:
            raise ValueError("A fraction can only be added with an Integer or another fraction.")

    def __gt__(self,other):
        """Operator overload for greater than equality"""
        if(type(other) == Fraction):
            #multiply fractions
        elif(type(other) == int):
            #multiply fraction with int
        else:
            raise ValueError("A fraction can only be added with an Integer or another fraction.")

    def __lt__(self,other):
        """Operator overload less than equality"""
        if(type(other) == Fraction):
            #multiply fractions
        elif(type(other) == int):
            #multiply fraction with int
        else:
            raise ValueError("A fraction can only be added with an Integer or another fraction.")

    def __eq__(self, other):
        """Operator overload for doing a deep equality check"""
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum


class testFraction(unittest.TestCase):
    def testMath(self):
        self.assertTrue()

if __name__ == '__main__':
    unittest.main()
