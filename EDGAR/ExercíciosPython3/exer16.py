peso = float(input('Digite seu peso em KG: '))
altura = float(input('Digite sua altura em METROS: '))

imc = peso/(altura*altura )
print('Seu IMC é : ' , imc)

if imc < 18.5:
    print('Voce esta abaixo do peso ideal.')

elif imc >= 18.5 and imc <= 24.9:
    print('Parabens voce esta no peso normal')


if imc >= 25.0  and imc <= 29.9:
    print('Voce esta acima do seu peso (sobre peso)')

elif imc >= 30.0  and imc <= 34.9:
    print('Voce esta com obesidade grau 1')   
 

if imc >= 35.0  and imc <= 39.9:
    print('Voce esta com obesidade grau 2')   

elif imc  > 40:     
    print('Voce esta com obesidade grau 3')
