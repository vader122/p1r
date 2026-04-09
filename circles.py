import math

class circle:
    def __init__(self, wspx,wspy,prom: float):
        self.x = wspx
        self.y = wspy
        self.r = prom


    def __str__(self):
        return "kwadrat"

    def circumference(self):
        return 3.14159265358*2*self.r

    def intersection(self, circle2):
        odl = math.sqrt((self.y-circle2.y)**2+(self.x-circle2.x)**2)

        if odl > self.r+circle2.r:
            return 0
        if odl == self.r+circle2.r:
            return 1
        if odl < self.r+circle2.r and odl > abs(self.r-circle2.r):
            return 2
        if odl == abs(self.r-circle2.r):
            return 1
        if odl < abs(self.r-circle2.r):
            return 0

c1 = circle(0,0,2)
c2 = circle(0,1,3)

print(c1.intersection(c2))