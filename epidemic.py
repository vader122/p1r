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
            return Person(self.x,self.y, self.status)

        if self.status == 1:
            dx = random.uniform(0,0.1)
            self.x = self.x + dx*random.choice([1,-1])
            self.y = self.y + math.sqrt(0.1-dx**2)*random.choice([1,-1])
            return Person(self.x,self.y, self.status)

    

    def Info(self):
        return print(f"położenie (w,y) = {self.x},{self.y}, stan storwia: {self.status}")

    def __str__(self):
        return f"położenie (w,y) = {self.x},{self.y}, stan storwia: {self.status}"

    

class Population:
    
    def __init__(self, w=100, h=100, infectionprob=0.2, infectiondist =1, liczeb = 100):
        def randinfect():
            if random.random() <= infectionprob:
                return 1 +random.choice([0,1])
            else:
                return 0
            
        
        self.w = w
        self.h = h
        self.people = [Person(random.uniform(0,w), random.uniform(0,h), randinfect()) for x in range(liczeb)]
        self.__InfectionProbability = infectionprob
        self.__InfectionDistance = infectiondist 
        
    
    def Move(self):

        # self.people = [p.Move() for p in self.people]
        # self.people = [Person(p.x % self.w, p.y % self.h, p.status) for p in self.people]

        for p in self.people:
            p.Move()
            p.x = p.x % self.w
            p.y = p.y % self.h




        for p in self.people:
            if p.status == 1 or p.status == 2:
                pass
            else:
                for p1 in self.people:
                    if math.sqrt((p.x-p1.x)**2+(p.y-p1.y)**2) <= 1 and (p1.status == 1 or p1.status == 2):
                        pro = random.random()
                        if pro <= 0.25:
                            p.status = 1
                        if pro>0.25 and pro <=0.5:
                            p.status = 2
                        if p.status == 1 or p.status == 2:
                            break
                        


        return self.people


    

    def Paint(self):
        fig, wyk = plt.subplots()
        zdr = [x for x in self.people if x.status == 0]
        cho = [x for x in self.people if x.status == 1]
        nos = [x for x in self.people if x.status == 2]

        scat1 = wyk.scatter([p.x for p in zdr], [p.y for p in zdr], c ='b')
        scat2 = wyk.scatter([p.x for p in cho], [p.y for p in cho], c ='r')
        scat3 = wyk.scatter([p.x for p in nos], [p.y for p in nos], c ='y')

        wyk.set(xlim=[0, self.w], ylim=[0, self.h], xlabel='szerekość', ylabel='wysokość')
        # for p in self.people:
        #     if p.status == 0:
        #         scat1 = wyk.scatter(p.w, self.h, c='b')
        #     if p.status == 1:
        #         scat2 = wyk.scatter(self.w, self.h, c='r')
        #     if p.statu3 == 2:
        #         scat1 = wyk.scatter(self.w, self.h, c='y')
        
        def update(frame):
            self.Move()

            zdr = [x for x in self.people if x.status == 0]
            cho = [x for x in self.people if x.status == 1]
            nos = [x for x in self.people if x.status == 2]
            
            data1 =np.stack([[p.x for p in zdr], [p.y for p in zdr]]).T
            scat1.set_offsets(data1)

            data2 =np.stack([[p.x for p in cho], [p.y for p in cho]]).T
            scat2.set_offsets(data2)

            data3 =np.stack([[p.x for p in nos], [p.y for p in nos]]).T
            scat3.set_offsets(data3)

            return (scat1,scat2,scat3)
        
            

        ani = animation.FuncAnimation(fig=fig, func=update, frames=40, interval=30)
        plt.show()


PoP = Population(liczeb=1000, infectionprob=0.001)
PoP.Paint()
        

    
