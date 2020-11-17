import sys 
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
ROT = 13

entrada = input("ENCRYPT OR DECRYPT ?  ")
comando = entrada.upper()


def base(message, dir):   
     m = ""
     for c in message:
          if c in ALPHABET:
              c_index = ALPHABET.index(c)
              m += ALPHABET[(c_index + ( dir * ROT)) % len(ALPHABET) ]
          else: 
              m += c
     return m


     
def encrypt(message):
  return base(message, 1)

def decrypt(message):
  return base(message, -1)


if comando == "ENCRYPT" :
    palavra = input("DIGITE A FRASE QUE DESEJA ENCRIPTAR : ")
    print(encrypt(palavra))
        
elif comando == "DECRYPT" :
    palavra = input("DIGITE A FRASE QUE DESEJA DECRIPTAR : ")
   
    print(decrypt(palavra))
else : 
    print(comando +  " -> COMANDO NÃO ACEITO")     


