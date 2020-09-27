peças = float(input('Digite quantas peças fez no mes: '))
base= float(1045.00)
peçasliquidas = peças - 30

salario3por100 = (1045 * 0.03) * peçasliquidas



salario5por100 = (1045 * 0.05) * peçasliquidas



if peçasliquidas > 30 and peçasliquidas < 50 :
    print('Seu salário é :' , salario3por100 , "R$")

elif peçasliquidas >= 50 :
    print('Seu salário é : ' ,salario5por100 , "R$")

else:
    print('Seu salario vira só o base pois voce nao bateu a meta. ')    
 


