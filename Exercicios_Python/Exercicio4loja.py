area = input('Informe  tamanho da area em M²:') 
vlt = 80
def Calk():

    clc = float(area)/(3)/(18)
    print ("quantidade de tinta em Latas {0:.2f}".format(clc))

    clc2 = float(clc)*(80)
    print ("Total R$: {0:.2f}".format(clc2))
    print("Preço unitário da lata: R$", vlt)

    

Calk()