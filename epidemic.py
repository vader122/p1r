import random
import math
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

import matplotlib.animation as animation



class Person:
    def __init__(self, x, y, stat=0):
        self.x = x
        self.y = y
        self.status = stat #0-zdorwy, 1-chory, 2-nosiciel
        self.__MaxDistance = 1
        self.__MaxIllDistance = 0.1
    
    def Move(self):
        if self.status == 0 or self.status == 2:
            dx = random.random()
            self.x = self.x + dx*random.choice([1,-1])
            self.y = self.y + math.sqrt(1-dx**2)*random.choice([1,-1])

        if self.status == 1:
            dx = random.uniform(0,0.1)
            self.x = self.x + dx*random.choice([1,-1])
            self.y = self.y + math.sqrt(0.1-dx**2)*random.choice([1,-1])

    

    def Info(self):
        return print(f"położenie (w,y) = {self.x},{self.y}, stan storwia: {self.status}")

    def __str__(self):
        return f"położenie (w,y) = {self.x},{self.y}, stan storwia: {self.status}"

    

class Population:
    
    def __init__(self, w=100, h=100, infectionprob=0.2, infectiondist =1, liczeb = 100):
        def rand():
            if random.random() <= infectionprob:
                return 1
            else:
                return 0
            
        
        self.w = w
        self.h = h
        self.people = [Person(random.uniform(0,w), random.uniform(0,h), rand()+random.choice([0,1])) for x in range(liczeb)]
        self.__InfectionProbability = infectionprob
        self.__InfectionDistance = infectiondist 
        
    
    def Move(self):

        self.people = [p.Move() for p in self.people]
        self.people = [p.x = p.x % self.w for p in self.people]
        self.people = [p.y = p.y % self.h for p in self.people]

        for p in self.people:
            if p.status() == 1 or p.status() == 2:
                pass
            else:
                for p1 in self.people:
                    if math.sqrt((p.x-p1.x)**2+(p.y-p1.y)**2) <= 1 and (p1.status() = 1 or p1.status() = 2):
                        pro = random.random()
                        if pro <= 0.25:
                            p.status = 1
                        if pro>0.25 and pro <=0.5:
                            p.status = 2
                        if p.status == 1 or p.status == 2:
                            break
                        


        return 0


    

    def Paint(self):
        fig, wyk = plt.subplots()
        for p in self.people:
            if p.status() == 0:
                scat1 = wyk.scatter(self.w, self.h, c='b')
            if p.status() == 0:
                scat1 = wyk.scatter(self.w, self.h, c='b')
            if p.status() == 0:
                scat1 = wyk.scatter(self.w, self.h, c='b')
        
        def update(frame):

        ani = animation.FuncAnimation(fig=fig, func=update, frames=40, interval=30)
        plt.show()
        

    
