md5 = input('qtd md 5:')
md10 = input('qtd md 10:')

def calk(): 
    clc = (float(md5)*(0.05))
    clc2 = (float(md10)*(0.010))
    nt2 = clc+clc2
    

    print ("qtd nt 2: {0:.0f} \ncentavos que sobraram {1:.2f}".format(nt2, nt2 - (int(nt2))) )

calk()
    



