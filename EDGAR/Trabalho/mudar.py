import random

a1 = int 
b1 = int
a2 = int
b2 = int
a3 = int
b3 = int


c1 = int
d1 = int
c2 = int
d2 = int
c3 = int
d3 = int
x8 = int




while a1 or b1 or a2 or b2 or a3 or b3 or c1 or d1 or c2 or d2 or c3 or d3 != "sair"  :
    
 x1_y1 = (random.randint(0, 9)) , (random.randint(0, 9))

 x2_y2= (random.randint(0, 9)) ,  (random.randint(0, 9)) 

 x3_y3 = (random.randint(0, 9)),  (random.randint(0, 9))
 


 

 a1 = (int(input("Digite a latitude X1: ")))
 b1 = (int(input("Digite a longitude Y1: ")))

 a2 = (int(input("Digite a latitude X2: ")))
 b2 = (int(input("Digite a longitude Y2: ")))

 a3 = (int(input("Digite a latitude X3: ")))
 b3 = (int(input("Digite a longitude Y3: ")))



 


 if a1 == x1_y1[0] and b1 ==  x1_y1[1] and a2 == x2_y2[0] and b2 == x2_y2[1]and a3 == x3_y3[0] and b3 == x3_y3[1]   :
    print("Parabens Você Ganhou! ")
    print("JODO ENCERRADO !!!")  
    break

 else : 
     print("Você Errou agora é a vez da máquina! ")    
     print("\n")



             # SEGUNDA PARTE
 

 c1 = (int(input("Digite sua latitude W1: ")))
 d1 = (int(input("Digite sua longitude Q1: ")))

 c2 = (int(input("Digite sua latitude W2: ")))
 d2 = (int(input("Digite sua longitude Q2: ")))

 c3 = (int(input("Digite sua latitude W3: ")))
 d3 = (int(input("Digite sua longitude Q3: ")))
 
 
 w1 = (random.randint(0, 9))
 q1 = (random.randint(0, 9))

 w2 = (random.randint(0, 9))  
 q2 = (random.randint(0, 9))

 w3 = (random.randint(0, 9))
 q3 = (random.randint(0, 9))
 print("\n")
 
 


 if w1 == c1 and d1 == q1 and w2 == c2 and d2 == q2 and w3 == c3 and d3 == q3 :
    print("A Máquina ganhou Ganhou\n Você perdeu. ")
    print("JODO ENCERRADO !!!")  
    break 
 
  
 else :  
    print("Para sair digite 'sair' a qualquer momento! ")
     
    print("\n") 

    print("A máquina errou agora é sua vez novamente! ") 
   
    
