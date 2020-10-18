a = float(input("Digite a quantidade de maçã que deseja comprar"))

if a < 12 :
    b = a * 1.3
    print("Pagará R$ {} pelas maçãs compradas".format(round(b,2))) 
elif a >= 12 :
    b = a * 1

    print("você escolheu {} Maçãs para comprar")
    print("Pagará R$", b, "pelas maçãs compradas".format(round(a,2))) 