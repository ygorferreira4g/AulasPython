#  Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento 
#  de pesca do estado de Goiás (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa 
#  que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável
#   excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
#   Imprima os dados do programa com as mensagens adequadas.

peso = int(input("digite quantos quilos de peixe pescou:"))

exceço = peso - 50

multa = exceço * 4


if peso > 50 :  
    print("Você excedeu" , exceço , "Kg de peixes do limite permitido" )
    print("Você pagará R$", multa," de multa ")
else :
     print("Pode ficar tranquilo que você ainda está na média só pescou", peso, "Kg de Peixes")

