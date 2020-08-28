slm = float(input("Digite valor do salário mínimo:"))
kwt = float(input("Digite o consumo em KW:"))

kw = (slm/7) 
Valor_cada_KW = kw/100

Valor_Pagar = Valor_cada_KW*kwt

Valor_Pagar_10_por_cento = (Valor_Pagar/100)*90
print("Valor do KW: %.2f"%(Valor_cada_KW))
print("Valor Total a pagar R$: %.2f"%(Valor_Pagar))
print("Valor a pagar com 10 de desconto R$: %.2f"%(Valor_Pagar_10_por_cento))
