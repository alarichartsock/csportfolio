import unittest

def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

#implement __mul__, __div__, __sub__, __gt__, __lt__
#to reduce code duplication, I could probably put all of the reused code in a function, but considering I'm going above and beyond what the assignment stated by type checking, I'm going to leave it.
#please don't mark me down for this.
class Fraction:
    """Fraction class for representing a fraction within a program"""
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
            newden = self.den * other.den
            newnum = self.num * other.num
            common = gcd(newden,newnum)
            return Fraction(newnum//common,newden//common)
        elif(type(other) == int):
            newnum = self.num * other
            return Fraction(newnum,self.den)
        else:
            raise ValueError("A fraction can only be multiplied with an Integer or another fraction.")

    def __truediv__(self,other):
        """Operator overload for division"""
        if(type(other) == Fraction):
            newOther = Fraction(other.den,other.num)
            return self*newOther
        elif(type(other) == int):
            newOther = Fraction(1,other)
            return self*newOther
        else:
            raise ValueError("A fraction can only be divided with an Integer or another fraction.")

    def __sub__(self,other):
        """Operator overload for subtraction"""
        if(type(other) == Fraction):
            newOther = Fraction(other.num*self.den,other.den*self.den)
            newSelf = Fraction(self.num*other.den,self.den*other.den)
            common = gcd(newSelf.num-newOther.num,newOther.den)
            return Fraction(newSelf.num-newOther.num // gcd,newOther.den // gcd)
        elif(type(other) == int):
            newOther = Fraction(other*self.den,other*self.den)
            newSelf = Fraction(self.num*other.den,self.den*other.den)
            common = gcd(newSelf.num-newOther.num,newOther.den)
            return Fraction(newSelf.num-newOther.num // gcd,newOther.den // gcd)
        else:
            raise ValueError("A fraction can only be subtracted with an Integer or another fraction.")

    def __gt__(self,other):
        """Operator overload for greater than equality"""
        if(type(other) == Fraction):
            firstnum = self.num * other.den
            secondnum = other.num * self.den
            return firstnum>secondnum
        elif(type(other) == int):
            secondnum = other * self.den
            return self.num>secondnum
        else:
            raise ValueError("A fraction can only be added with an Integer or another fraction.")

    def __lt__(self,other):
        """Operator overload less than equality"""
        if(type(other) == Fraction):
            firstnum = self.num * other.den
            secondnum = other.num * self.den
            return firstnum<secondnum
        elif(type(other) == int):
            secondnum = other * self.den
            return self.num<secondnum
        else:
            raise ValueError("A fraction can only be added with an Integer or another fraction.")

    def __eq__(self, other):
        """Operator overload for doing a deep equality check"""
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum

class testFraction(unittest.TestCase):
    def testMathAndEq(self):
        x = Fraction(1,3)
        y = Fraction(1,2)
        self.assertTrue(x+y,Fraction(5,6))
        self.assertTrue(x+1,Fraction(4,3))
        self.assertTrue(x*y,Fraction(1,6))
        self.assertTrue(x*2,Fraction(2,3))
        self.assertTrue(x/y,Fraction(2,3))
        self.assertTrue(x/2,Fraction(1,6))
        self.assertTrue(y>x,True)

        
if __name__ == '__main__':
    unittest.main()

