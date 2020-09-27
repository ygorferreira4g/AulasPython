sexo = str(input('Digite se é Homem ou  Mulher: '))
salario = float(input('Digite quanto voçê ganha: '))


if sexo == "Mulher"  and salario > 10000.00 :
    print(' Casa comigo?')

elif sexo == "Mulher" and salario <=  10000.00 :
    print('Sai comigo ?')

elif sexo == "Homem" and salario >= 10000.00:
    print(' Me empresta dinheiro ?')

else:
    print(' Até mais')



