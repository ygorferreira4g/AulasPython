nome = "Jessie"
saldo = 1000
print("Olá , ", nome)

lançamento = int(input("Digite 1 para colocar dinheiro, 2 para sacar 3 para sair: "))
Deposito = 1
Saque = 2
finalizar = 3

if lançamento == Deposito:
    c = int(input("Digite quanto quer colocar na conta: "))
    
    print("Deposito feito com sucesso.")    



elif lançamento == Saque :
    d = int(input("Digite o valor da compra : "))
    saldo -= d
    print("Pagamento efetuado com sucesso.")

elif lançamento == finalizar :
        print("Agradecemos seu acesso")

print("O seu saldo é de: R${} .".format(saldo))
print("Muito obrigado por utilizar nossos serviços!")

