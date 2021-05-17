import matplotlib.pyplot as plt
import math
import numpy 
def funkcija(f, x):
    return f(x)
def derivacija_funkcije(f, x, h = 0.01, opcija = 3):
    if opcija == 2:
        df = (f(x+h) - f(x))/h
        return df
    elif opcija == 3:
        df_ = (f(x+h) - f(x-h))/(2*h)
        return df_
def derivacija_u_intervalu(f, donja_meda, gornja_meda, h = 0.01, opcija = 3):
    df = []
    x = []
    x_ = 0
    for x_ in numpy.linspace(donja_meda, gornja_meda, 100):
        x.append(x_)
        df.append(derivacija_funkcije(f, x_, h, opcija))
    return df,x
def integral_preko_pravokutnika(f, donja_meda, gornja_meda, N):
    gore = 0
    dole = 0
    dx = (gornja_meda-donja_meda)/N
    for i in range(0, N):
        dole += f(i*dx)*dx
        gore += f((i+1)*dx)*dx
    return dole,gore
def integral_preko_trapeza(f, donja_meda, gornja_meda, N):
    dx = (gornja_meda-donja_meda)/N
    s = 0
    for i in range(0, N):
        s += f(i*dx) + f((i+1)*dx)
    return (s*dx)/2












