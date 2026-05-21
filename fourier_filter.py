import numpy as np
import matplotlib.pyplot as plt


def input(func, dt, t, szer):
    def funkcja(t):
        return eval(func)

    time = np.linspace(0,t, int(t/dt))
    dane = funkcja(time)
    szum = 0.1* np.array([np.random.normal(scale = szer) for x in time])
    zaszumione = dane + szum
    result = np.fft.fft(zaszumione)
    czest = np.fft.fftfreq(len(zaszumione), d=time[1]-time[0])
    czest_odciecia = 1
    plt.plot(time,dane)
    #plt.plot(time, zaszumione)
    #plt.scatter(czest, abs(result))
    

    w_result = result[np.argsort(abs(result))[-6:]]
    do_odwrotu = czest[np.argsort(abs(result))[-6:]]
    w_recov = np.fft.ifft(w_result)
    #print(w_recov)

    #bet_result = [result[x] if x in np.argsort(abs(result))[-52:] else 0 for x in np.argsort(abs(result))]
    bet_result = result * (abs(czest) <= czest_odciecia)
    bet_recov = np.fft.ifft(np.array(bet_result))
    # odwrot = np.fft.ifft(do_odwrotu)
    print(czest)

    # recov = np.fft.ifft(zaszumione)
    

    #plt.scatter(do_odwrotu, w_result)
    plt.plot(time, bet_recov)


    
    plt.show()


input('np.sin(t)+0.5*np.cos(2*t)+0.25*np.sin(3*t)', 0.01, 100, 10)
