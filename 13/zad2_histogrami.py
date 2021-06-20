import universe13
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import random
import math
au = 1.496e11
day = 60*60*24
year = 365.242*day
Dsun = []
Dmer = []
Dven = []
Dzem = []
Dmars = []
D_sun = []
D_zem = []
D_ven = []
D_mer = []
D_mars = []
for i in range(1000):
    sun = universe13.Planet("Sun","yellow", 1.989e30, np.array((0.,0.)), np.array((0.,0.)))
    mercury = universe13.Planet("Mercury","green", 3.3e24, np.array((0.,-0.387 * au)), np.array((47362.,0.)))
    venus = universe13.Planet("Venus","gold", 4.8685e24, np.array((0.723 * au,0.)), np.array((0.,35020.)))
    earth = universe13.Planet("Earth","blue", 5.9742e24, np.array((-1*au,0.)), np.array((0.,-29783.)))
    mars = universe13.Planet("Mars", "red", 6.417e23, np.array((0.,-1.52 * au)), np.array((24007.,0.)))
    ss = universe13.Universe()
    ss.add_planet(sun)
    ss.add_planet(mercury)
    ss.add_planet(venus)
    ss.add_planet(earth)
    ss.add_planet(mars)
    masa = random.uniform(1e13,9.9e13)
    rx = random.uniform(2*au,3*au)
    ry = random.uniform(2*au,2.5*au)
    vx = random.uniform(-35000,-15000)
    vy = random.uniform(-35000,-15000)
    komet = universe13.Planet("komet","brown",masa,np.array((rx,ry)),np.array((vx,vy)))
    ss.add_planet(komet)
    ss.evolve(2*year)
    x_pol = komet.x
    y_pol = komet.y
    x_sun = sun.x
    y_sun = sun.y
    x_zem = earth.x
    y_zem = earth.y
    x_ven = venus.x
    y_ven = venus.y
    x_mars = mars.x
    y_mars = mars.y
    x_mer = mercury.x
    y_mer = mercury.y
    t = len(x_sun)
    t1 = len(x_zem)
    t2 = len(x_ven)
    t3 = len(x_mer)
    t4 = len(x_mars)
    for k in range(t):
        d = math.sqrt((x_sun[k]-x_pol[k])**2+(y_sun[k]-y_pol[k])**2)
        Dsun.append(d)
    D = min(Dsun)
    D_sun.append(D)
    print("{}. komet Sunce.".format(i+1))
    for k in range(t3):
        d = math.sqrt((x_mer[k]-x_pol[k])**2+(y_mer[k]-y_pol[k])**2)
        Dmer.append(d)
    D = min(Dmer)
    D_mer.append(D)
    print("{}. komet Merkur.".format(i+1))
    for k in range(t2):
        d = math.sqrt((x_ven[k]-x_pol[k])**2+(y_ven[k]-y_pol[k])**2)
        Dven.append(d)
    D = min(Dven)
    D_ven.append(D)
    print("{}. komet Venera.".format(i+1))
    for k in range(t1):
        d = math.sqrt((x_zem[k]-x_pol[k])**2+(y_zem[k]-y_pol[k])**2)
        Dzem.append(d)
    D = min(Dzem)
    D_zem.append(D)
    print("{}. komet Zemlja.".format(i+1))
    for k in range(t4):
        d = math.sqrt((x_mars[k]-x_pol[k])**2+(y_mars[k]-y_pol[k])**2)
        Dmars.append(d)
    D = min(Dmars)
    D_mars.append(D)
    print("{}. komet Mars.".format(i+1))
plt.subplot(1,5,1)
plt.hist(D_sun)
plt.xlabel("Udaljenost [m]")
plt.ylabel("Frekvencija")
plt.title("Sunce")
plt.subplot(1,5,2)
plt.hist(D_mer)
plt.xlabel("Udaljenost [m]")
plt.ylabel("Frekvencija")
plt.title("Merkur")
plt.subplot(1,5,3)
plt.hist(D_ven)
plt.xlabel("Udaljenost [m]")
plt.ylabel("Frekvencija")
plt.title("Venera")
plt.subplot(1,5,4)
plt.xlabel("Udaljenost [m]")
plt.ylabel("Frekvencija")
plt.title("Zemlja")
plt.hist(D_zem)
plt.subplot(1,5,5)
plt.hist(D_mars)
plt.xlabel("Udaljenost [m]")
plt.ylabel("Frekvencija")
plt.title("Mars")
plt.savefig("primjer_za_sto_kometa.pdf")
plt.show()

            
