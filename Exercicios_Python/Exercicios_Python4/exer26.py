divisor = 1
valor = 0
sinal = 1

while 4/divisor > 0.0001:
    print(4, divisor*sinal)
    valor += 4/divisor*sinal
    divisor += 2
    sinal *= -1
print(valor)