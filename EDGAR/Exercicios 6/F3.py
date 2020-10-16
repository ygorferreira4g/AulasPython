populacao = 50000000
m = 60000000

pulacao_por_ano = populacao * 0.02

def A (x):
    return  (x * 0.02) + populacao

def B (y):
    return ( y * 0.02 ) / 100000

def C (z):
    return z * 0.02 / 100



print("A população em 1992 sera de " , A(populacao), "de pessoas")

print("A população terá ultrapassado 60 milhões em ", B(populacao) , " Anos")

print("A população terá dobrado em  " , C(populacao) , "Anos")

