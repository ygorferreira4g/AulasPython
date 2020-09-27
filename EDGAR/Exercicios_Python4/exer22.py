somafem = somamasc = idade = mediah = mediatotal = media30 = 0
horastrabalho = 220
salariohr30 = 40
salriohr = 60

for i in range(4):
    sexo = int(input("Digite seu sexo ( 1 se mulher , 2 se homem):"))
    idade = int(input("Digite sua idade:"))
    if sexo == 1 :
        somafem +=1
    madiam = salriohr * horastrabalho

    if idade < 30:
        media30 = salariohr30 * horastrabalho
    mediatotal = (mediah + media30) / 2
    if sexo ==2 :
        somamasc += 1
        mediah + salariohr30 * horastrabalho
mediatotal = (mediah + madiam) / 2

print("A quantidade de homens é: {}. A quantidade de mulher é: {} .".format(somamasc, somafem))
print("A media salarial total da empresa é de: `R${}. A media total das mulheres é: R${}.".format(somamasc,somafem))
print("A media das mulheres com mednos de 30 anos é de:R${}. A media total das mulheres é: R${}.".format(media30, mediatotal))