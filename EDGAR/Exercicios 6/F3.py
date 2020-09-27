populacao = 50000000
m = 60000000

pulacao_por_ano = populacao * 0.02

def A (x):
    return  (populacao * 0.02) + populacao

def B (y):
    return ( populacao * 0.02 ) / 10000

def C (z):
    return populacao * 0.02 / 100



print("A população em 1992 sera de " , A(2), "de pessoas")

print("A população terá ultrapassado 60 milhões em ", B(1) , " Anos")

print("A população terá dobrado em  " , C(1) , "Anos")

