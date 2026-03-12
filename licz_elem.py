from collections import Counter
b = [1, 1, a, a, c, c ,c]
def licz(a):
    x = Counter(a)
    return x

print(licz(b))