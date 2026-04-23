import numpy as np

class Velocity:
    def __init__(self, beta=0):
        self.beta = beta
    def __str__(self):
        return f'Ułamek prędkości wynosi {self.beta}.'
    def __repr__(self):
        return f'Velocity: {self.beta}.'
    def __add__(self, other: "Velocity"):
        new_beta = (self.beta+other.beta)/(1+self.beta*other.beta)
        return Velocity(new_beta)
    def __iadd__(self, other: "Velocity"):
        self.beta = (self.beta+other.beta)/(1+self.beta*other.beta)
        return self
    def gamma(self):
        return 1/np.sqrt(1-self.beta**2)
    
    
def velocity(v1=0, v2=0):
    V1 = Velocity(v1)
    V2 = Velocity(v2)
    V = V1+V2
    return V, V.gamma()


print(velocity(0.5,0.7))
V3 = Velocity(0.5)
V3 += Velocity(0.7)
print(V3)
    
    
    
