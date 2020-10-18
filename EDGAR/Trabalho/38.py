
print("CANDIDATOS\n 1- JOÃO\n 2- PEDRO\n 3- LUCAS\n 4- JOSÉ\n 5- NULO\n 6- BRANCO")
print("\n")

escolha = []
joao = 0
pedro = 0
lucas = 0
jose = 0
nulo = 0
branco = 0
i = 0


while escolha != 0 :
        escolha = int(input("DIGITE O NÚMERO CORRESPONDENTE AO SEU CANDIDATO: "))
        print("\n")
        if escolha == 1:
               joao = joao + 1
               print(" VOTOU NO JOÃO")

        elif escolha == 2 :
             pedro = pedro + 1   
             print(" VOTOU NO PEDRO")

        elif escolha  == 3 :
             lucas = lucas + 1
             print(" VOTOU NO LUCAS")

        elif escolha == 4 :
             jose = jose + 1
             print(" VOTOU NO JOSÉ") 

        elif escolha == 5 :
             nulo = nulo + 1
             print(" VOTOU NULO") 

        elif escolha == 6 : 
             branco = branco + 1  
             print(" VOTOU RM BRANCO")  

        elif escolha > 6 :   
             print("NÚMERO DO CANDIDATO NÃO EXISTE")
else :
    print ("VOTAÇÃO ENCERRADA!")       



print("QUANTIDADE DE VOTOS PARA JOÃO: ",joao)
print("QUANTIDADE DE VOTOS PARA PEDRO: ",pedro)
print("QUANTIDADE DE VOTOS PARA LUCAS: ",lucas)
print("QUANTIDADE DE VOTOS PARA JOSÉ: ",jose)
print("TOTAL DE VOTOS:" , joao + pedro  +  lucas + jose + nulo + branco)
print("VOTOS NULOS: ", nulo)
print("TOTAL DE VOTOS EM BRANCOS: ", branco)
print("PORCENTAGEM DE VOTOS NULOS: " ,( joao + pedro  +  lucas + jose + nulo + branco / 6 ) * nulo)
print("PORCENTAGEM DE VOTOS EM BRANCO: " ,( joao + pedro  +  lucas + jose + nulo + branco / 6 ) * branco)




