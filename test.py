import json
plik = open("/dmj/2025/ag479781/Pobrane/ludnosc.json")
dane = json.load(plik)
plik.close()

print(dane['2013'].keys())