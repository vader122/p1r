import json
from matplotlib import pyplot as plt

plik = open("/dmj/2025/ag479781/Pobrane/D-42.json")
slownik = json.load(plik)

dane = slownik["dane"]
granice = slownik["granice"]

plik.close()

def przygotuj_histogram(granice, wartosci):
    słow = {}
    for i in range(len(granice)):
        słow[granice[i]] = 0
        if i != len(granice)-1:
            for j in range(len(wartosci)):
                if wartosci[j]<granice[i+1] and wartosci[j]>=granice[i]:

                    słow[granice[i]] = słow[granice[i]]+ 1
        słow["gmax"] = 0
        for k in range(len(wartosci)):
            if wartosci[k]>=granice[-1]:
                słow[gmax] = słow[gmax] + 1
        słow["gmin"] = 0
        for l in range(len(wartosci)):
            if wartosci[k]< granice[0]:
                słow[gmin] = słow[min] + 1

    return słow
przyg = przygotuj_histogram(granice,dane)

print(przyg)


