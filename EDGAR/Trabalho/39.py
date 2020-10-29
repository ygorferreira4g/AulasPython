import math



num = float(input("Digite um número:"))
print("\n")

raiz = int ((num) ** 0.5)
raiz2 = float((num) ** 0.5)

print("O numero inteiro que mais se aproxima da raiz quadrada de", num,"é", raiz  + 1)
print("A raiz quadrada de", num, "é {} ".format(round(raiz2 , 2)))