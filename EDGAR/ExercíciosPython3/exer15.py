p1 = float(input('Qts dedos tem a mão do Mickey ? '))
p2 = float(input('Em que ano nasceu Albert Einsten ? '))
p3 = float(input('Qual e o resultado de 2x(3+2)-1 ? '))

 # acertou as 3

if  p1 == 4 and  p2 == 1879 and p3 == 9:
    print('Voçê é levemente burro')

    # acertou 2

elif p1 != 4 and p2 == 1879 and p3 == 9:
    print('Você é moderadamente burro!')

elif p1 == 4 and p2 != 1879 and p3 == 9:
    print('Você é moderadamente burro!')

elif p1 == 4 and p2 == 1879 and p3 != 9:
    print('Você é moderadamente burro!') 

# acertou 1

elif p1 !=4 and p2 != 1879 and p3 == 9:
    print('Você é extremamente burro!') 

elif p1 !=4 and p2 == 1879 and p3 != 9:
    print('Você é extremamente burro!') 

elif p1 == 4 and p2 != 1879 and p3 != 9:
    print('Você é extremamente burro!') 

    # errou todas

else:
    print('Você tem o QI de uma porta!')

    
   