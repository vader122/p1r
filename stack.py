class Stack:
    def __init__(self, lista = []):
        self.S = lista
    def __str__(self):
        return f'stos S'
    
    def pusty(self):
        if self.S == []:
            return "false"

    
    def stosowanie(self, a):
        self.S.append(a)
    def odstosowanie(self):
        self.S.pop()
    def zczyt(self):
        return self.S[-1]


S = Stack()

b = [2.54, 45.6, 7.12, 9.1, 991.5]

def zwrot(pod):
    S1 = Stack(pod)
    while not S1.pusty():
        print(S1.zczyt())
        S1.odstosowanie()
    return 0
    
zwrot(b)





