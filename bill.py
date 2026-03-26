with open("/dmj/2025/ag479781/Pobrane/in.txt","r") as par:
    dane = par
    s = 0
    for line in dane:
        s = s + float(line.split()[-1])
print(s)
