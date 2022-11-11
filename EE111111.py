import numpy as np
import math
from random import random
from random import gauss
from matplotlib import pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

def f(x1,x2,x3):
    f = x1 + 2*x2 +x2*x3 -x1**2 -x2**2 -x3**2
    return f

def evol(u,v,w):
    plt.figure(1)
    plt.plot(u)
    plt.plot(v)
    plt.plot(w)
    plt.legend(('x1','x2','x2'))
    plt.ylim([-2, 2])
    
    plt.show()

def mutation(x1,s):
    xn = x1+s*gauss(0,1)
    while xn < -2 or xn > 2:
        xn = x1+s*gauss(0,1)
    return xn

def sigma(s,g,m):
    ps = m/g
    c = 0.817
    if g%20 == 0:
    #if True:
        if ps > 0.2:
            s = s/c
        elif ps < 0.2:
            s = s*c
        else:
            s = s
    else:
        s = s
    return s
    
def main():
  
    xmin, xmax, ymin, ymax, zmin, zmax = [-2, 2, -2, 2, -2, 2]
    gmax = 500;           #máximo número de iteraciones
    m = 0;                 #número de mutaciones exitosas
    c = 0.817;
    x1 = 4*random()+xmin
    x2 = 4*random()+ymin
    x3 = 4*random()+zmin
    x0y0z0 = [round(x1,6), round(x2,6), round(x3,6)]
    print("x0,y0,z0: ",x0y0z0)
    padre = f(x1,x2,x3)
    s = 1
    u = [x1]
    v = [x2]
    w = [x3]
    
    for g in range(1,gmax):
        xn = mutation(x1,s)
        yn = mutation(x2,s)
        zn = mutation(x3,s)
        hijo = f(xn,yn,zn)
        if hijo > padre:
            x1 = xn
            x2 = yn
            x3 = zn
            m += 1               #mutación exitosa
            padre = f(x1,x2,x3)
        else:
            x1 = x1
            x2 = x2
            x3 = x3
            m = m
        s = sigma(s,g,m)
        u.append(x1)
        v.append(x2)
        w.append(x3)
        
    xfyfzf = [round(x1,6), round(x2,6), round(x3,6)]
    print("xf,yf,zf: ",xfyfzf)
    evol(u,v,w)
    
main()