import calculus as clc
import matplotlib.pyplot as plt
import numpy 
import math

#derivacije

def f(x):
    return x**3 + x**2 + x + 1
def f_2(x):
    return 2*x**3 + 5*x**2 + 5
df_1 = clc.funkcija(f, 0)
df_2 = clc.funkcija(f_2, 1)
df_4 = clc.derivacija_funkcije(f, 0)
df_5 = clc.derivacija_funkcije(f_2, 1)
print("Iznos funkcije f(x) = x^3 + x^2 + x + 1  u x=0 iznosi {}.".format(df_1))
print("Iznos funkcije f(x) = 2x^3 + 5x^2 + 5  u x=1 iznosi {}.".format(df_2))
print("Derivacija funkcije f(x) = x^3 + x^2 + x + 1  u x=0 iznosi {}.".format(round(df_4,3)))
print("Derivacija funkcije f(x) = 2x^3 + 5x^2 + 5  u x=1 iznosi {}.".format(round(df_5,3)))
xf_list = []
f_analist = []
xf_list2 = []
f_analist2 = []
x_f = 0
x_f2 = 0
for i in range(0,100):
    x_f = i*0.1
    xf_list.append(x_f)
    f_analist.append(3*xf_list[i]**2 + 2*xf_list[i] + 1)
for i in range(0,90):
    x_f2 = i
    xf_list2.append(x_f2)
    f_analist2.append(6*xf_list2[i]**2 + 10*xf_list[i])
plt.plot(xf_list, f_analist, c = "b")
df, x = clc.derivacija_u_intervalu(f,0,10,0.1,2)
plt.scatter(x, df, s=5, c = "r")
x.clear()
df.clear()
plt.title('Numerička derivacija (crvena)\n Analitička derivacija (plava)')
plt.show()
plt.plot(xf_list2, f_analist2, c = "b")
df2, x2 = clc.derivacija_u_intervalu(f_2, 0, 90, 3)
plt.scatter(x2, df2, s=5, c = "r")
x2.clear()
df2.clear()
plt.title("Numerička derivacija (crvena)\n Analitička derivacija (plava)")
plt.show()

#integrali

def f_i(x):
    return 3*x**2 + 4 #u rasponu od 0 do 3
def f_i_2(x):
    return x**3 + x #u rasponu od 0 do 1
analiticki_izracunat_integral_1 = 39
analiticki_izracunat_integral_2 = 0.75
gornjameda = []
donjameda = []
integraltrapez = []
Nlist = []
gornjameda2 = []
donjameda2 = []
integraltrapez2 = []
Nlist2 = []
for N in range(100, 1000, 10):
    gor_meda, don_meda = clc.integral_preko_pravokutnika(f_i, 0, 3, N)
    gornjameda.append(gor_meda)
    donjameda.append(don_meda)
    integraltrapez.append(clc.integral_preko_trapeza(f_i, 0, 3, N))
    Nlist.append(N)
for n in range(100, 1000, 10):
    gornja_medja_2, donja_medja_2 = clc.integral_preko_pravokutnika(f_i_2, 0, 1, n)
    gornjameda2.append(gornja_medja_2)
    donjameda2.append(donja_medja_2)
    integraltrapez2.append(clc.integral_preko_trapeza(f_i_2, 0, 1, n))
    Nlist2.append(n)
plt.scatter(Nlist, donjameda, c = "b", s=5)
plt.scatter(Nlist, gornjameda, c = "g",s=5)
plt.scatter(Nlist,integraltrapez, c = "r",s=5)
print("Analitički izračunat prvi integral iznosi {}, a numerički {}.".format(analiticki_izracunat_integral_1, integraltrapez[89]))
print("Analitički izračunat drugi integral iznosi {}, a numerički {}.".format(analiticki_izracunat_integral_2, integraltrapez2[89]))
plt.axhline(analiticki_izracunat_integral_1)
plt.title("Gornja i donja međa se\n prelijevaju u egzaktnu vrijednost no.1")
plt.show()
plt.scatter(Nlist2, donjameda2, c ="b",s=5)
plt.scatter(Nlist2, gornjameda2, c = "g",s=5)
plt.scatter(Nlist2, integraltrapez2, c = "r",s=5)
plt.axhline(analiticki_izracunat_integral_2)
plt.title("Gornja i donja međa se\n prelijevaju u egzaktnu vrijednost no.2")
plt.show()









