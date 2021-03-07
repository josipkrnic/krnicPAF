import matplotlib.pyplot as plt 
import numpy as np
def pravac(x1,y1,x2,y2):
    k = round((y2-y1)/(x2-x1),3)
    l = -k*x1 + y1
    print("y = {}x + l".format(k,l))
while True:
    x1 = float(input("Unesite x koordinatu prve točke: "))
    y1 = float(input("Unesite y koordinatu prve točke: "))
    x2 = float(input("Unesite x koordinatu druge točke: "))
    y2 = float(input("Unesite y koordinatu druge točke: "))
    if x1 == x2:
        print("Ponovite unos.")
    else:
        print(pravac(x1,y1,x2,y2))
        break
xpoints = np.array([x1,x2])
ypoints = np.array([y1,y2])
plt.plot(xpoints,ypoints)
plt.show()