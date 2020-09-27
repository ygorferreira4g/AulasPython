periodo = 0
juros = valor = 0.0
valorinicial = 1000

for periodo in range(1, 4):
    valor = valorinicial * (1 + 0.1)**periodo
    print("O valor do mês {} é: {}".format(periodo, round(valor, 2)))