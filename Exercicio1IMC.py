nome = input('Qual seu nome:')
altura = input('Qual sua altura em metros:')
peso = input('Qual o seu peso em KG:')

def calkIMC():
    imc = float(peso)/(float(altura)*float(altura))

    print("Ola", nome, "o seu IMC e ", imc)

calkIMC()