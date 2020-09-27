numero = 0

while numero < 1:
    numero = int(input("informa um numero ai maluco"))

for i in range(1, numero):
    if numero % i == 0:
        print("O número", i,"é divisor de", numero)