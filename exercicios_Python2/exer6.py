SalarioH = 50.00
horaT = 220
desINSS = 8

salarioBruto = SalarioH * horaT
salarioDesconto = ((salarioBruto * 8) / 100)
SalarioLiquido = salarioBruto - salarioDesconto
porcentagem_de_desconto = 100 - (SalarioLiquido*100/salarioBruto) 


print("Seu salario bruto é R$: %.2f"  % (salarioBruto))
print("Seu salario Liquido é R$: %.2f"%(SalarioLiquido))

print("Seu Desconto é de:" , porcentagem_de_desconto , "%")