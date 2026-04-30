from sympy import hermite , Poly , Symbol, legendre

class Polynomial:
    def __init__(self, list = []):
        while True:
            if list[::-1] == 0:
                list.pop()
            else:
                break
        
        self.c = list

    def __str__(self):
        return str(self.c)
        

    @property
    def deg(self):
        return len(self.c)-1
    
    def __getitem__(self, key):
        return self.c.get(key)
    
    def __setitem__(self, key, value):
        self.c[key] = value
        return self.c.get(key)
    
    def __delitem__(self, key):
        del self.c[key]
        
    def __call__(self, real):
        w = 0
        for i in range(len(self.c)):
            w = w + (real**(i))*self.c[i]
        return w

    def __add__(self, other):
        new_c = [x+y for x,y in zip(self.c, other.c)]
        return Polynomial(new_c)
    
    def __mul__(self, real):
        new_c = [real*x for x in self.c]
        return Polynomial(new_c)
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def D(self):
        new_c = [i*self.c[i] for i in range(len(self.c))]
        new_c = new_c[1::]
        return Polynomial(new_c)
    
def HermiteCoefficients ( n ) :

    x = Symbol ('x')
    return Poly(hermite(n , x ) , x ).coeffs()

def LegendreCoefficients ( n ) :
    x = Symbol ('x')
    return Poly(legendre(n , x ),x).coeffs()
    
a = Polynomial([12,1,3,8])
b = a.D()



def polynomial(nat, real):
    PolL = Polynomial(LegendreCoefficients(nat))
    PolH = Polynomial(HermiteCoefficients (nat))
    Pol = Polynomial(LegendreCoefficients(nat)).D() + Polynomial(HermiteCoefficients(nat)).D() + 3*(Polynomial(LegendreCoefficients(nat))+Polynomial(HermiteCoefficients(nat)))
    print(PolL(real))
    print(PolH(real))
    print(Pol(real))
    return 0 

polynomial(5, 57)
    

    



