import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def f(t, x, a, b, c, d):
   
    return [(a-b*x[1])*x[0],(-c+d*x[0])*x[1]]

def solver(t_eval, x0, args):
    sol = solve_ivp(f, (0, t_eval[-1]), x0, t_eval=t_eval, args=args, method='RK45')
    return sol.t, sol.y[0], sol.y[1]



def lv(x_0, y_0, a, b, c, d, t_m, delta):
    t_eval = np.linspace(0, t_m, delta)
    x0 = np.array([x_0, y_0])
    t, x, y = solver(t_eval=t_eval, x0=x0, args=(a, b, c, d))

    

    return t,x,y

t, x, y = lv(10, 10, 2.1, 0.1, 0.5,0.1,100, 1000)

plt.plot(t,x, label='ofiary', color='blue')
plt.plot(t,y, label='drapieżnicy', color='red')
plt.show()


