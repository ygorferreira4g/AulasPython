pp = float(input('Qual o Valor em R$ do que quer comprar ? '))

md1 = 1
md5 = 5
md25 = 25
md10 = 10
md50 = 50
md100 = 100

mdt = float( ((md1 + md5 + md10 + md25 + md50 + md100) * 700) / 100 )
print("O Valor que voce tem no cofre é R$" , mdt)

if pp > mdt:
    print('Precisa Juntar mais dinheiro')

elif pp <= mdt:
    print("Oba, vamos comprar... ")    
