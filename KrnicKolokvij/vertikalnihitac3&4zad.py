import vertikalnihitac as vert
obj1 = vert.VertikalniHitac()
obj1.init(10,10,0.01)
print("Za početnu visinu {} i početnu brzinu {}, maksimalna je visina {}.".format(10,10,obj1.h_maks()))
obj1.reset()
obj2 = vert.VertikalniHitac()
obj2.init(10,10,0.05)
print("Za početnu visinu {} i početnu brzinu {}, vrijeme hica jest {}.".format(10,10,obj2.vrijeme_hica()))
obj2.reset()
