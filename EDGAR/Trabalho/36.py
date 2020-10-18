codigo = 1
altura = 1
peso = 1
i = 0
c1 = 0 ; a1 = 0 ; p1 = 0 ; c2 = 0 ; a2 = 0 ; p2 = 0; c3 = 0 ;a3 = 0 ; p3 = 0 ; c4 = 0 ; a4 = 0 ; p4 = 0


def maisBaixo() :

    
                               # DEFINIÇÃO CALCULO PARA MAIS BAIXO

                     #       EQUAÇÃO PRA SABER O MAIS BAIXO 1

    if  a1 != 0 and a1  <=  a2 and a3 and a4  :
        print(" CLIENTE MAIS BAIXO : \n CÓDIGO :" , c1,"ALTURA :" , a1, "PESO :" , p1)    
        print("\n")    
      


                     #       EQUAÇÃO PRA SABER O MAIS BAIXO 2

    elif a2 != 0 and a2 <= a1 and a3 and a4 :
        print(" CLIENTE MAIS BAIXO : \n CÓDIGO :" , c2,"ALTURA :" , a2, "PESO :" , c2) 
        print("\n") 
      

                    #       EQUAÇÃO PRA SABER O MAIS BAIXO 3

    elif a3 != 0 and a3 <= a1 and a2 and a4 :
         print( " CLIENTE MAIS BAIXO :\n CÓDIGO :" , c3 ,  "ALTURA :" , a3, "PESO :" , p3)
         print("\n") 
       

                    #       EQUAÇÃO PRA SABER O MAIS BAIXO  4

    elif a4 != 0 and a4 <= a1 and a2 and a3 :
        print(" CLIENTE MAIS BAIXO : \n CÓDIGO :" , c4 , "ALTURA :" , a4, "PESO :" , p4)  
        print("\n") 
       





                               # DEFINIÇÃO CALCULO PARA MAIS ALTO


def maisAlto():                 
    
                      #       EQUAÇÃO PRA SABER O MAIS ALTO 1

    if a1 == a1 and a1  > a2 and a1 > a3 and a1 > a4 :
        print("CLIENTE MAIS ALTO: \n  CÓDIGO :" , c1 ,"ALTURA :" , a1 , "PESO :" , p1) 
        print("\n")       
        print("ALTURA MÉDIA: " , ( a1+a2+a3+a4 ) / i )
        print("\n")
        
     
       
      
   


                    #       EQUAÇÃO PRA SABER O MAIS ALTO 2

    elif a2 == a2 and  a2 > a1 and a2 > a3 and a2 > a4 :  
        print(" CLIENTE MAIS ALTO: \n  CÓDIGO :" , c2 , "ALTURA :" , a2, "PESO :" , p2)  
        print("\n") 
        print("ALTURA MÉDIA 3: " , (a1+a2+a3+a4 ) / i )
        print("\n") 
        

        


                              #       EQUAÇÃO PRA SABER O MAIS ALTO 3

    elif a3 == a3 and a3 > a1 and a3 > a2 and a3 > a4 :
       print(" CLIENTE MAIS ALTO: \n  CÓDIGO :" , c3 , "ALTURA :" , a3, "PESO :" , p3)  
       print("\n") 
       print("ALTURA MÉDIA: " , (a1+a2+a3+a4 ) / i )
       print("\n")
      
       

                        


                        #       EQUAÇÃO PRA SABER O MAIS ALTO  4

    elif a4 == a4 and a4  > a1 and a4 > a2 and a4 > a3 :  
       print(" CLIENTE MAIS ALTO : \n   CÓDIGO :" , c4 , "ALTURA :" , a4, "PESO :" , p4)  
       print("\n") 
       print("ALTURA MÉDIA: " , (a1+a2+a3+a4 ) / i )
       print("\n") 
       maisBaixo()



def Magro() :   
      
                                # DEFINIÇÃO PARA SABER MAIS GORDO 

    if p1 != 0 and p1 <= p2 and p3  and p4 :
        print("Cliente Mais Magro:\n" ,"PESO :" , p1 ,"CÓDIGO :" , c1, "ALTURA :" , a1) 
        print("\n") 

    if p2 != 0 and p2 <= p1 and p3  and p4 :
        print("Cliente Mais Magro:\n" ,"PESO :" , p2 ,"CÓDIGO :" , c2, "ALTURA :" , a2) 
        print("\n") 

    if p3 != 0 and p3 <= p1 and p2 and p4 :
        print("Cliente Mais Magro:\n" ,"PESO :" , p3 ,"CÓDIGO :" , c3, "ALTURA :" , a3)   
        print("\n")  

    if p4 != 0 and p4 <= p2 and p2  and p3s :
        print("Cliente Mais Magro:\n" ,"PESO :" , p4 ,"CÓDIGO :" , c4, "ALTURA :" , a4)   
        print("\n")  
           





                                                       

                          # DEFINIÇÃO PARA SABER MAIS GORDO 

def Gordo():

    if p1 == p1  and p1  > p2  and p1 > p3 and p1 > p4 :
        print("Cliente Mais Gordo:\n" ,"PESO :" , p1 ,"CÓDIGO :" , c1, "ALTURA :" , a1) 
        print("\n") 
        print("Média de peso:",(p1 +p2 + p3 + p4 ) / i)
        print("\n")
    

    if p2 == p2 and p2 > p1 and p2 > p3 and p2 > p4 :
        print("Cliente Mais Gordo:\n" ,"PESO :" , p2 ,"CÓDIGO :" , c2, "ALTURA :" , a2) 
        print("\n") 
        print("Média de peso:",(p1 +p2 + p3 + p4 ) / i)
        print("\n")


    if p3 == p3 and p3 > p1 and p3 > p2 and p3 > p4 :
        print("Cliente Mais Gordo:\n" ,"PESO :" , p3 ,"CÓDIGO :" , c3, "ALTURA :" , a3)   
        print("\n") 
        print("Média de peso:",(p1 +p2 + p3 + p4 ) / i)
        print("\n") 
    

    if p4 == p4 and p4 > p1 and p4 > p2 and p4 > p3 :
        print("Cliente Mais Gordo:\n" ,"PESO :" , p4 ,"CÓDIGO :" , c4, "ALTURA :" , a4)   
        print("\n") 
        print("Média de peso:",(p1 +p2 + p3 + p4 ) / i)
        print("\n") 
         



while codigo != 0 :
    
        codigo = int(input("Digite seu Código ou 0 para finalizar: "))
        print("\n")
        if codigo != 0 :
         altura = int(input("Digite sua altura: "))
         print("\n")
         peso = int(input("Digite seu Peso: "))
         print("\n")  



        else :
         print("PROCESSO FINALIZADO " ) 
         print("\n")      
         maisAlto()
         print("\n") 
         Gordo()
         print("\n")          
         maisBaixo()
         print("\n") 
         Magro()
         print("\n") 
        
        # PRIMEIRO CLIENTE

        if i == 0 :
         c1 = codigo
         a1 = altura
         p1 = peso  
        
            

       #   SEGUNDO CLIENTE

        if i == 1  :
         c2 = codigo
         a2 = altura
         p2 = peso
        
 
        # TERCEIRO CLIENTE

        if i == 2  :
         c3 = codigo
         a3 = altura
         p3 = peso
        


        # QUARTO CLIENTE

        if i == 3  :
         c4 = codigo
         a4 = altura
         p4 = peso
        

        i = i + 1






                      







    

