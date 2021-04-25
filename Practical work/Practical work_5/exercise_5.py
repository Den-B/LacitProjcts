import math
class Drop():
    def __init__(self,numerator,denominator,):
        self.numerator=int(numerator)
        self.denominator=int(denominator)
        self.number=0
    
    def normalize(self):
        if(self.denominator<=self.numerator):
            self.number=int(self.numerator/self.denominator)
            self.numerator=(self.numerator-self.denominator*self.number)
        divider = math.gcd(self.numerator,self.denominator)

        if(self.numerator==0):
            self.denominator=0

        else:
            self.numerator=int(self.numerator/divider)
            self.denominator=int(self.denominator/divider)
        print(self.numerator,self.denominator)

    def __str__(self):#?
        buff=str(self.number)+" "+str(self.numerator)+"/"+str(self.denominator)
        print(buff) 


    def NOK(one,two):
        nok=one*two/math.gcd(one,two)
        return nok


    def __add__(self,other):
        nok=Drop.NOK(self.denominator,other.denominator)
        return Drop((self.numerator+self.denominator*self.number)*(nok/self.denominator)+(other.numerator+other.number*other.denominator)*(nok/other.denominator),nok)

    def __sub__(self,other):
        nok=Drop.NOK(self.denominator,other.denominator)
        return Drop((self.numerator+self.denominator*self.number)*(self.denominator/nok)-(other.numerator+other.number*other.denominator)*(other.denominator/nok),nok)

    def __mul__(self,other):
        return Drop((self.numerator+self.number*self.denominator)*(other.numerator+other.number*other.denominator),self.denominator*other.denominator)

    def __truediv__(self,other):
        nok=Drop.NOK(self.denominator,other.denominator)
        return Drop((self.numerator+self.number*self.denominator)*other.denominator,((other.numerator+other.number*other.denominator)*self.denominator))

    def __lt__(self,other):
        nok=Drop.NOK(self.denominator,other.denominator)
        return (self.numerator+self.denominator*self.number)*(nok/self.denominator)<(other.numerator+other.number*other.denominator)*(nok/other.denominator)

    def __le__(self,other):
        nok=Drop.NOK(self.denominator,other.denominator)
        return (self.numerator+self.denominator*self.number)*(nok/self.denominator)<=(other.numerator+other.number*other.denominator)*(nok/other.denominator)

    def __eq__(self,other):
        nok=Drop.NOK(self.denominator,other.denominator)
        return (self.numerator+self.denominator*self.number)*(nok/self.denominator)==(other.numerator+other.number*other.denominator)*(nok/other.denominator)


    def __gt__(self,other):
        nok=Drop.NOK(self.denominator,other.denominator)
        return (self.numerator+self.denominator*self.number)*(nok/self.denominator)>(other.numerator+other.number*other.denominator)*(nok/other.denominator)


    def __ge__(self,other):
        nok=Drop.NOK(self.denominator,other.denominator)
        return (self.numerator+self.denominator*self.number)*(nok/self.denominator)>=(other.numerator+other.number*other.denominator)*(nok/other.denominator)

