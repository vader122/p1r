import numpy as np

class Rational:
    def __init__(self, p=0, q=1):
        self.p = int(p)
        self.q = int(q)
        lista = []
        if self.q < 0:
            self.q = -self.q
            self.p = -self.p
        
        for i in range(2,min(abs(int(self.p+1)), abs(int(self.q+1)))):
            if self.p%i == 0 and self.q%i == 0:
                lista.append(i)
        if lista:
            for i in lista:
                self.p = self.p/i
                self.q = self.q/i


        self.p = int(self.p)
        self.q = int(self.q)

        
    def __str__(self):
        return f'Ułamek wynosi {self.p}/{self.q}.'
    
    def __repr__(self):
        return f'{self.p}/{self.q}'
    
    def __add__(self, other: "Rational"):
        new_p = self.p*other.q+other.p*self.q
        new_q = self.q*other.q
        return Rational(new_p, new_q)
   
    
    def __iadd__(self, other):
        self.p = self.p*other.q+other.p*self.q
        self.q = self.q*other.q
        self = Rational(self.p, self.q)
        return self
    

     
    def __isub__(self, other):
        self.p = self.p*other.q-other.p*self.q
        self.q = self.q*other.q
        self = Rational(self.p, self.q)
        return self
    
    def __sub__(self, other: "Rational"):
        new_p = self.p*other.q-other.p*self.q
        new_q = self.q*other.q
        return Rational(new_p, new_q)
    
    def __mul__(self, other: "Rational"):
        new_p = self.p*other.p
        new_q = self.q*other.q
        return Rational(new_p, new_q)
   
    
    def __imull__(self, other):
        new_p = self.p*other.p
        new_q = self.q*other.q
        self = Rational(new_p, new_q)
        return self
    
    def __truediv__(self, other: "Rational"):
        self * Rational(other.q, other.p)
        return self * Rational(other.q, other.p)
   
    
    def __itruediv__(self, other):
        self = self * Rational(other.q, other.p)
        return self


    
    def numerator(self):
        return self.p
    
    def denominator(self):
        return self.q
    
    def __float__(self):
        return float(self.p/self.q)
    
    def __neg__(self):
        new_p = -self.p
        q = self.q
        return Rational(new_p, q)
    
    def __lt__(self, other):
        if self.p*other.q<self.q*other.p:
            return True
        else:
            return False
        
def rational(a = Rational(),b = Rational()):
    print(f' liczba 1 to {float(a)}, liczba 2 to {float(b)}')
    print(f'liczby przeciwne to: {-a}, {-b}')
    lista = [a,b]
    lista = sorted(lista)
    print(f'w kolejności niemalejącej: {lista[0]}, {lista[1]}')
    print(f'suma: {a+b}, iloczyn {a*b}')

rational(Rational(1,7), Rational(3,9))
    


    


    