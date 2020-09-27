valor = 0
valorinicial = 1000

for periodo in range(1, 11):
    valor = valorinicial * (1+0.02)**periodo
    print("o valor do mês {} é: {}".format(periodo, round(valor, 2)))