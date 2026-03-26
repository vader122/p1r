dane = 0

with open("/dmj/2025/ag479781/Pobrane/in.txt","r") as pin:
    dane = pin
    with open("/dmj/2025/ag479781/Pobrane/out.txt","a") as pout:
        for line in dane:
            if line.strip()[0] == "?":
                continue
            else:
                pout.write(line)





