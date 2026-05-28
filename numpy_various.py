import numpy as np
from abc import ABC, abstractmethod
from matplotlib import pyplot as plt

class Shape(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, a):
        super().__init__(a,a)
    
    def function(self):
        return lambda i,j : ((i == self.x) & (np.abs(j) <= self.x)) | (((j == self.x) & (np.abs(i) <= self.x)))

    def area(self):
        return self.x**2

class Rectangle(Shape):
    def __init__(self, a, b):
        super().__init__(a,b)

    def area(self):
        return self.x*self.y

class Ellipse(Shape):
    def __init__(self, a, b):
        super().__init__(a,b)
    
    def area(self):
        return np.pi*self.x*self.y
    
    
square = Square(10)

mat = np.fromfunction(square.function(), (100,100))

def color_shape(shape_matrix, n, color = (50,50,50)):
    matrix = np.empty((n,n), dtype=object)
    for i in range(n):
        for j in range(n):
            if shape_matrix[i][j] == True:
                matrix[i][j] = color

    return matrix


mat_2 = color_shape(mat, n=100)
plt.imshow(mat_2)



    