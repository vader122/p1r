import json
from matplotlib import pyplot as plt


plik = open("/dmj/2025/ag479781/Pobrane/ludnosc.json")
dane = json.load(plik)
plik.close()

a = input('Podaj województwo lub wpisz "Polska":')
b = input('Podaj pożądana statystykę:')

x = []
y = []
gen = []

if a != "Polska":

    if b != 'gestosc':
        for i in range(2013,2026):
            x.append(dane[str(i)][a][b])

        plt.plot(range(2013,2026), x)
        plt.show()
    else:
        for i in range(2013,2026):
            x = [dane[str(i)][key]['ludność'] for key in dane[str(i)].keys()]
            sumx = sum(x)
            y = [dane[str(i)][key]['powierzchnia km2'] for key in dane[str(i)].keys()]
            sumy = sum(y)
            gen.append(sumx/sumy)
        plt.plot(range(2013,2026), gen)
        plt.show()



else:
    if b!='gestosc':
        c = []
        for i in range(2013,2026):
            x = []
            x = [dane[str(i)][key][b] for key in dane[str(i)].keys()]
            x = sum(x)
            c.append(x)
            #x.append(dane[str(i)][a][b])
        plt.plot(range(2013,2026), c)
        plt.show()
    else:
        c = []
        for i in range(2013,2026):
            x = []
            x = [dane[str(i)][key]['ludność'] for key in dane[str(i)].keys()]
            x = sum(x)
            y =[]
            y = [dane[str(i)][key]['powierzchnia km2'] for key in dane[str(i)].keys()]
            y = sum(y)
            c.append(x/y)
        plt.plot(range(2013,2026), c)
        plt.show()
    
