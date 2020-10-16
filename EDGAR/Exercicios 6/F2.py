

def PA(NC1):
    return NC1 * 20 + 140

def PB(NC2):
    return  NC2 * 25 + 110


a = (int(input("Digite  Consultas: ")))

print("Valor que gastará com o plano A R$: " , PA(a))

print("Valor que gastará com o plano B R$: " , PB(a))

if PA(a) < PB(a) :
    print("Compensa plano B: ", PB(a))
else : 
    print("compensa plano A:  ", PA(a))

# if (PA < PB) :
#     print(PA)

# if (PB < PA ):
#     print(PB)    