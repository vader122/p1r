import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def f(t, x, g, l):
    """A = [[0, 1]], [-1, 0]], czyli odpowiada rownaniu
    dx/dt = v
    dv/dt = -x
    czyli w jednej linijce jest to: d^2x/dt^2 = -x
    """
    
    
    return [x[1], -(g/l)*np.sin(x[0])]

def solver(t_eval, x0):
    sol = solve_ivp(f, (0, t_eval[-1]), x0, t_eval=t_eval, args = (1,1))
    return sol.t, sol.y[0], sol.y[1]

t_max = 10
t_eval = np.linspace(0, t_max, 100)
x0 = np.array([1, 1.2])
t, x, y = solver(t_eval, x0)




plt.plot(t, x, label='x(t)')
#plt.plot(t, np.cos(t))
plt.show()