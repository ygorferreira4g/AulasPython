codigo = 1
altura = 1
peso = 1
i = 1
c1 = 0 ; a1 = 0 ; p1 = 0 ; c2 = 0 ; a2 = 0 ; p2 = 0; c3 = 0 ;a3 = 0 ; p3 = 0 ; c4 = 0 ; a4 = 0 ; p4 = 0



                               # DEFINIÇÃO CALCULO PARA MAIS ALTO


def maisAlto():                 
    
                      #       EQUAÇÃO PRA SABER O MAIS ALTO 1

    if a1 > a2 and a1 > a3 and a1 > a4 :
        print("CLIENTE MAIS ALTO : \n  CÓDIGO :" , c1 ,"ALTURA :" , a1 , "PESO :" , p1) 
        print("\n")       
        print("ALTURA MÉDIA: " , ( a1+a2+a3+a4 ) / 4 )
        print("\n")
   


                    #       EQUAÇÃO PRA SABER O MAIS ALTO 2

    elif a2 > a1 and a2 > a3 and a2 > a4 :
        print(" CLIENTE MAIS ALTO 2: \n  CÓDIGO :" , c2 , "ALTURA :" , a2, "PESO :" , p2)  
        print("\n") 
        print("ALTURA MÉDIA 3: " , (a1+a2+a3+a4 ) / 4 )
        print("\n") 


                              #       EQUAÇÃO PRA SABER O MAIS ALTO 3

    elif a3 > a1 and a3 > a2 and a3 > a4 :
       print(" CLIENTE MAIS ALTO 4 : \n  CÓDIGO :" , c3 , "ALTURA :" , a3, "PESO :" , p3)  
       print("\n") 
       print("ALTURA MÉDIA: " , (a1+a2+a3+a4 ) / 4 )
       print("\n") 

                    


                        #       EQUAÇÃO PRA SABER O MAIS ALTO  4

    elif a4 > a1 and a4 > a2 and a4 > a3 :
       print(" CLIENTE MAIS ALTO : \n   CÓDIGO :" , c4 , "ALTURA :" , a4, "PESO :" , p4)  
       print("\n") 
       print("ALTURA MÉDIA: " , (a1+a2+a3+a4 ) / 4 )
       print("\n") 

                   


def maisBaixo() :

    
                               # DEFINIÇÃO CALCULO PARA MAIS BAIXO

                     #       EQUAÇÃO PRA SABER O MAIS BAIXO 1

    if a1 < a2 and a1 < a3 and a1 < a4 :
        print(" CLIENTE MAIS BAIXO : \n CÓDIGO :" , c1,"ALTURA :" , a1, "PESO :" , p1)    
        print("\n")    
        print("ALTURA MÉDIA: " , ( a1+a2+a3+a4 ) / 4 )
        print("\n")


                     #       EQUAÇÃO PRA SABER O MAIS BAIXO 2

    if a2 < a1 and a2 < a3 and a2 < a4 :
        print(" CLIENTE MAIS BAIXO : \n CÓDIGO :" , c2,"ALTURA :" , a2, "PESO :" , c2) 
        print("\n") 
        print("ALTURA MÉDIA2: " , (a1+a2+a3+a4 ) / 4 )
        print("\n")
                   

                    #       EQUAÇÃO PRA SABER O MAIS BAIXO 3

    if a3 < a1 and a3 < a2 and a3 < a4 :
         print( " CLIENTE MAIS BAIXO :\n CÓDIGO :" , c3 ,  "ALTURA :" , a3, "PESO :" , p3)
         print("\n") 
         print("ALTURA MÉDIA3: " , (a1+a2+a3+a4 ) / 4 ) 
         print("\n")


                    #       EQUAÇÃO PRA SABER O MAIS BAIXO  4

    if a4 < a1 and a4 < a2 and a4 < a3 :
        print(" CLIENTE MAIS BAIXO : \n CÓDIGO :" , c4 , "ALTURA :" , a4, "PESO :" , p4)  
        print("\n") 
        print("ALTURA MÉDIA 4: " , (a1+a2+a3+a4 ) / 4 )
        print("\n")







                                # DEFINIÇÃO PARA DENTRO DO MAIS ALTO  
          # Essa definição foi feita para ser usada apenas dentro da definição calculo

# def textoAlto()  :
#     print(" CLIENTE MAIS ALTO :  CÓDIGO" , c4 , "ALTURA" , a4, "PESO" , p4)  
#     print("ALTURA MÉDIA: " , (a1+a2+a3+a4 ) / 4 )
#     print("\n")                             

                          # DEFINIÇÃO PARA SABER MAIS GORDO 

def Gordo():

    if p1 > p2  and p1 > p3 and p1 > p4 :
        print("Cliente Mais Gordo:\n" ,"PESO : " , p1 ,"CÓDIGO : " , c1, "ALTURA : " , a1) 
        print("\n") 

    if p2 > p1 and p2 > p3 and p2 > p4 :
        print("Cliente Mais Gordo:\n" ,"PESO : " , p2 ,"CÓDIGO : " , c2, "ALTURA : " , a2) 
        print("\n") 

    if p3 > p1 and p3 > p2 and p3 > p4 :
        print("Cliente Mais Gordo:\n" ,"PESO : " , p3 ,"CÓDIGO : " , c3, "ALTURA : " , a3)   
        print("\n")  

    if p4 > p1 and p4 > p2 and p4 > p3 :
        print("Cliente Mais Gordo:\n" ,"PESO : " , p4 ,"CÓDIGO : " , c4, "ALTURA : " , a4)   
        print("\n")   


def Magro() :   
      
                                # DEFINIÇÃO PARA SABER MAIS GORDO 

    if p1 < p2  and p1 < p3 and p1 < p4 :
        print("Cliente Mais Magro:\n" ,"PESO : " , p1 ,"CÓDIGO : " , c1, "ALTURA : " , a1) 
        print("\n") 

    if p2 < p1 and p2 < p3 and p2 < p4 :
        print("Cliente Mais Magro:\n" ,"PESO : " , p2 ,"CÓDIGO : " , c2, "ALTURA : " , a2) 
        print("\n") 

    if p3 < p1 and p3 < p2 and p3 < p4 :
        print("Cliente Mais Magro:\n" ,"PESO : " , p3 ,"CÓDIGO : " , c3, "ALTURA : " , a3)   
        print("\n")  

    if p4 < p1 and p4 < p2 and p4 < p3 :
        print("Cliente Mais Magro:\n" ,"PESO : " , p4 ,"CÓDIGO : " , c4, "ALTURA : " , a4)   
        print("\n")  



while i <  5 :
    
        codigo = int(input("Digite seu Código ou 0 para finalizar: "))
        print("\n")
        altura = int(input("Digite sua altura: "))
        print("\n")
        peso = int(input("Digite seu Peso: "))
        print("\n")
        
        # PRIMEIRO CLIENTE

        if i == 1 :
         c1 = codigo
         a1 = altura
         p1 = peso  
        
        elif codigo == 0 :
            print("PROCESSO FINALIZADO " ) ; i = 6
            print("\n")
            print("Seu codigo :",c1 ,"   Sua altura:", a1 , "  Seu peso :", p1 )
            print("\n") 
            maisAlto()
            print("\n") 
            maisBaixo()
            print("\n") 
            Gordo()
            print("\n") 
            Magro()
            print("\n")

         



       #   SEGUNDO CLIENTE

        elif i == 2  :
         c2 = codigo
         a2 = altura
         p2 = peso
        elif codigo == 0 :
            print("PROCESSO FINALIZADO " ) ; i = 6
            print("\n")
            print("Seu codigo :",c2 ,"   Sua altura:", a2 , "  Seu peso :", p2 )
            print("\n") 
            maisAlto()
            print("\n") 
            maisBaixo()
            print("\n") 
            Gordo()
            print("\n") 
            Magro()
            print("\n")


 
        # TERCEIRO CLIENTE

        elif i == 3  :
         c3 = codigo
         a3 = altura
         p3 = peso
        elif codigo == 0 :
            print("PROCESSO FINALIZADO " ) ; i = 6
            print("\n")
            print("Seu codigo :",c3 ,"   Sua altura:", a3 , "  Seu peso :", p3 )
            print("\n") 
            maisAlto()
            print("\n") 
            maisBaixo()
            print("\n") 
            Gordo()
            print("\n") 
            Magro()
            print("\n")



        # QUARTO CLIENTE

        elif i == 4  :
         c4 = codigo
         a4 = altura
         p4 = peso
        elif codigo == 0 :
            print("PROCESSO FINALIZADO " ) ; i = 6
            print("\n")
            print("Seu codigo :",c4 ,"   Sua altura:", a4 , "  Seu peso :", p4 )
            print("\n") 
            maisAlto()
            print("\n") 
            maisAlto()
            print("\n") 
            Gordo()
            print("\n") 
            Magro()
            print("\n")

        i = i + 1






                      







    

