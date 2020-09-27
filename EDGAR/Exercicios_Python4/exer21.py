import random

numero = 4
nota = []
menor = 10
maior = 0
soma = 0
aprovados = 0

for i in range(10):
    n = random.randint(0, 10)
    nota.append(n)
    if n < menor :
        menor = n
    if n > maior :
        maior = n

print("notas: " , nota )
print("menor: " , menor )
print("maior: " , maior )
print("media: " , soma/10 )
print("aprovados: " , aprovados )