import matplotlib.pyplot as plt
import numpy as np
def kruznica(r,x,y,x1,y1):
     x = float(input("Unesite x koordinatu središta kružnice: "))
    y = float(input("Unesite y koordinatu središta kružnice: "))
    r = float(input("Unesite radijus kružnice: "))
    if r < 0:
        print("Ponovite unos.")
    else:
        x1 = float(input("Unesite x koordinatu točke: "))
        y1 = float(input("Unesite y koordinatu točke: "))
        X = x1 - x
        Y = y1 - y
        d = math.sqrt(math.pow(X, 2)+math.pow(Y, 2))
        if d < r:
            s = round(r-d,3)
            print("Točka se nalazi unutar kružnice i daleko je od nje za {}.".format(s))
            break
        elif d == r:
            print("Točka se nalazi na kružnici")
            break
        elif d > r:
            s = d-r
            print("Točka se nalazi izvan kružnice i udaljena je od nje za {}".format(s))
fi = np.linspace(0,2*np.pi,100)
eks = x + r*np.cos(fi)
epsilon = y + r*np.sin(fi)
fig, ax = plt.subplots(1)
ax.plot(eks, epsilon)
ax.set_aspect(1)
xpoints = np.array([x1])
ypoints = np.array([y1])
plt.plot(xpoints, ypoints, 'o')
plt.show()
