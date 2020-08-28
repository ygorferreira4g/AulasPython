sl1 = float(250)
sl2 = float(130)
sl3 = float(540)

tsl = (sl1 + sl2 + sl3)
print ("total", tsl)

msl  = int( tsl/3)
print("media", msl)

psl1 =  sl1*100/tsl
print("Porcentagem 1: %.2f" % (psl1))

psl2 = sl2*100/tsl
print("Porcentagem 2: %.2f" % (psl2))

psl3 = sl3*100/tsl
print("Porcentagem 3: %.2f" % (psl3))