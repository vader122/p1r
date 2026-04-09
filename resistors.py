class Resistor:
    def __init__(self, opor=0):
        self.__R = opor
    def __str__(self):
        return f'opornik o oporze {self.__R}'

    
    def get_resistance(self):
        return self.__R
    def set_resistance(self, res):
        self.__R = res

def series(a: Resistor, b: Resistor, rodz: str) -> Resistor:
    r1 = a.get_resistance()
    r2 = b.get_resistance()
    if rodz != "+" and rodz !="=":
            return print('zły rodzaj')
    if rodz == "+":
        return Resistor(r1 + r2)
    if rodz =="=":
        return Resistor(1/((1/r1)+(1/r2)))


def series1(a: Resistor, b: Resistor) -> Resistor:
    r1 = a.get_resistance()
    r2 = b.get_resistance()
    return Resistor(r1 + r2)


def series2():

    

