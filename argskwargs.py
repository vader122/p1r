from matplotlib import pyplot as plt
import numpy as np

lista = [2,3,4,5,3,2,1,345,2,134]
dict = {'ght':45, 'ghe':'dwjof', 'ckel':False, 'slowo':9}

def method(*args, **kwargs):
    print('printing args\n')

    for i in args:
        print(i)
    print('printing kwargs\n')
    for i in kwargs:
        print(i)

# method(lista,lista)
# method(*lista, gh=45, ghe='dwjof', ckel=False, slowo=9)
# method(lista, dict)
# method(dict, lista)

def method_2(a,b,*args, c = None, **kwargs):

    print('printing args\n')

    for i in args:
        print(i)
    print('printing kwargs\n')
    for i in kwargs:
        print(i)

    print(a)
    print(b)
    print(c)

# method_2(1,2,3,4,5,6,7,c=10, k=12, z=4)

def plot_with_params(x,y, **params):
    plt.plot(x,y, **params)
    plt.legend()
    plt.show()
    

wart  = np.linspace(0,100, 10000)
funk = np.sin(wart)

plot_with_params(wart, funk, color='green', linestyle='dashed', label='GHCCFGGGCFCFHJ')

