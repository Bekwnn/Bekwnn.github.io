import numpy as np
import matplotlib.pyplot as plt

def beziercurve(p0, p1, p2, p3, t):
    return ((1-t)**3)*p0 + 3*((1-t)**2)*t*p1 + 3*(1-t)*(t**2)*p2 + (t**3)*p3

def plotbezier(p0, p1, p2, p3, t):
    x = beziercurve(p0[0], p1[0], p2[0], p3[0], t)
    y = beziercurve(p0[1], p1[1], p2[1], p3[1], t)
    plt.figure(figsize=(5,5), facecolor='#252525', edgecolor='#e8e8e8')
    plt.xlim(0,1)
    plt.ylim(0,1)
    plt.subplot(111, facecolor='#252525')
    plt.plot(x, y, color='#1E90FF')
    xps = [p0[0], p1[0], p2[0], p3[0]]
    yps = [p0[1], p1[1], p2[1], p3[1]]
    plt.plot(xps, yps, 'x--')
    plt.show()
