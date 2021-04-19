import vertikalnihitac as vert
obj3 = vert.VertikalniHitac()
obj3.init_otpor(10,10,5,Dt=0.01,masa=1)
print("Za početnu visinu {} i početnu brzinu {} uz otpor zraka, vrijeme hica jest {}.".format(H0,V0,obj3.vrijeme_hica_otpor()))
obj3.reset()