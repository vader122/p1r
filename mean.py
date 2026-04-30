from abc import ABC, abstractmethod
import math
import argparse
import sys


class Mean(ABC):

    def __init__(self, x = []):
        self.x = x

    @property
    def N(self):
        return len(self.x)
    
    @abstractmethod
    def __call__(self):
        pass

class ArithmeticMean(Mean):
# tu jest też jaka s opcja z @override czy coś
    
    def __call__(self):
        avg = sum([x for x in self.x])/len(self.x)
        return avg
    


class GeometricMean(Mean):

    def __call__(self):
        avg = math.prod(([x for x in self.x]))**(1/len(self.x))
        return avg


class HarmonicMean(Mean):

    def __call__(self):
        avg = len(self.x)/(sum([1/x for x in self.x]))
        return avg
    
def mean():


    # sys std in wczytywanie

    list = []
    for line in sys.stdin:
    


        if 'q' == line.strip().lower():
            break
        list.append(float(line))


    a = ArithmeticMean(list)
    b = GeometricMean(list)
    c = HarmonicMean(list)

    print(a())
    print(b())
    print(c())

    return 0

mean()
#[12,3,43,1,6,21]

    

    

