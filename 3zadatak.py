while True:
    x1 = float(input("Unesite x koordinatu prve točke: "))
    if x1 == str:
        print("Ponovite unos.")
    y1 = float(input("Unesite y koordinatu prve točke: "))
    if y1 == str:
        print("Ponovite unos.")
    x2 = float(input("Unesite x koordinatu druge točke: "))
    if x2 == str:
        print("Ponovite unos.")
    y2 = float(input("Unesite y koordinatu druge točke: "))
    if y2 == str:
        print("Ponovite unos.")
    if x1 == x2:
        print("Ponovite unos.")
    else:
        k = (y2-y1)/(x2-x1)
        l = -k*x1 + y1
        print("y = {}x + {}".format(k,l))