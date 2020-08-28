import datetime

Km =  float(input("Digite e distancia em KM até seu destino:"))
km_l = 12
velocidade_Média = 80

qtd_L = Km/km_l

tempo_Gasto = Km/velocidade_Média

horasGastas = int(tempo_Gasto)
minutosGastos = int((tempo_Gasto - int(tempo_Gasto))*60)

reais = qtd_L * 4.60



print("Combustível: %.2f"  % (qtd_L ),"Litros")
print("Duração de viagem" ,horasGastas,"Horas e",minutosGastos,"Minutos")
print("Valor gasto com Combustível: R$ %.2f" %  (reais))

