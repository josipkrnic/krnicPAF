while True:
    x1 = float(input("Unesite x koordinatu prve točke: "))
    y1 = float(input("Unesite y koordinatu prve točke: "))
    x2 = float(input("Unesite x koordinatu druge točke: "))
    y2 = float(input("Unesite y koordinatu druge točke: "))
    if x1 == x2:
        print("Ponovite unos.")
    else:
        k = round((y2-y1)/(x2-x1),3)
        l = -k*x1 + y1
        print("y = {}x + {}".format(k,l))