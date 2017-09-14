import numpy as np
import matplotlib.pyplot as plt

def oceanfunc(x):
    freq0 = wavefunc(x, 0.5, 0.5, 1.3)
    freq1 = wavefunc(x, 1.3, 0.12, 2.1)
    freq2 = wavefunc(x, 2.3, 0.03, 3.1)
    freq3 = wavefunc(x, 4.7, 0.015, 1)
#    freq4 = wavefunc(x, 7.1, 0.0025, 2)
    return freq0+freq1+freq2+freq3

def wavefunc(x, freq=1, amp=1, offset=0):
    return amp*(-np.abs(np.sin(freq*x+offset)))

def plotfunction(t):
    plt.figure(figsize=(10,3), facecolor='#252525', edgecolor='#e8e8e8')
    plt.subplot(111, facecolor='#252525')
    plt.ylim(-3, 3)
    plt.plot(t, oceanfunc(t), color='#1E90FF')
    plt.show()

def plotsingle(t):
    plt.figure(figsize=(10,3), facecolor='#252525', edgecolor='#e8e8e8')
    plt.subplot(111, facecolor='#252525')
    plt.ylim(-3, 3)
    plt.plot(t, wavefunc(t), color='#1E90FF')
    plt.show()
