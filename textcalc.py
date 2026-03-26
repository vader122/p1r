def obl(k):
    dane = k.split()
    dane = {index: value for index, value in enumerate(dane)}
    for key in dane.keys():
        try:
            dane[key] = float(dane[key])
        except ValueError:
            continue


    zlicz = {
'+': lambda a, b: a + b,
'-': lambda a, b: a - b,
'*': lambda a, b: a * b,
'/': lambda a, b: a / b,
'%': lambda a, b: a % b,
'**': lambda a, b: a ** b,

}
    return print(zlicz[dane[1]](dane[0], dane[2]))

obl("3 ** 23")
