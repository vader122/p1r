import random
import numpy as np
n=10
A = np.random.randn(n,n) + 1j*np.random.randn(n,n)
B = np.random.randn(n,n) + 1j*np.random.randn(n,n)
C = np.zeros((n,n))
# for i in range(n):
#     for j in range(n):
C = A+B
D = A@B
E = np.einsum("ij, jk -> ki", A, B)

print(D)
print('======================')
print(E)
print(np.allclose(D,E))