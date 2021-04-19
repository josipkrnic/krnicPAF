import vertikalnihitac as vert 
o1 = vert.VertikalniHitac()
o2 = vert.VertikalniHitac()
q = input("Unesite P ili p za promjenu početnih parametara, a N ili n za nastavak: ")
if q == "N" or q == "n":
    o1.init(10,10,0.01)
    o2.init(60,35,0.01)
    print("Početna visina prvog objekta jest {} m, a početna brzina {} m/s".format(30, 40))
    print("Početna visina drugog objekta jest {} m, a početna brzina {} m/s".format(60, 35))
elif q == "P" or q == "p":
    o1.reset()
    o2.reset()
    h_0 = float(input("Unesite novu početnu visinu prvog objekta: "))
    v_0 = float(input("Unesite novu početnu brzinu prvog objekta: "))
    h_o = float(input("Unesite novu početnu visinu drugog objekta: "))
    v_o = float(input("Unesite novu početnu brzinu drugog objekta: "))
    print("Nova početna visina prvog objekta jest {} m, a početna brzina {} m/s.".format(h_0, v_0))
    print("Nova početna visina drugog objekta jest {} m, a početna brzina {} m/s.".format(h_o,v_o))


