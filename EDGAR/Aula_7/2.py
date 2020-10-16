file = open("texto", "r")
text = file.read().lower()
lines = text.count("\n")
count_os = text.count(" os ") + text.count("\nos") + (1 if text.startswith("os ") else 0)
count_o = text.count(" o ") + text.count("\no") + (1 if text.startswith("o ") else 0)
count_as = text.count(" as ") + text.count("\nas") + (1 if text.startswith("as ") else 0)
count_a = text.count(" a ") + text.count("\na") + (1 if text.startswith("a ") else 0)
#media = (count_os+count_o+count_as+count_a)/lines
linha = 0
n_line_menor = 0
n_line_maior = 0
menor = 1000
maior = 0
for frase in text.split("\n"):
    linha += 1
    count = frase.count(" os ") + frase.count("\nos") + frase.count(" o ") + frase.count("\no") + \
            frase.count(" as ") + frase.count("\nas") + frase.count(" a ") + frase.count("\na") + \
            (1 if text.startswith("a ") else 0) + (1 if text.startswith("as ") else 0) + \
            (1 if text.startswith("o ") else 0) + (1 if text.startswith("os ") else 0)
    if count < menor:
        menor = count
   n_line_menor = linha
    if count > maior:
        if linha == 67:
            print("veja o que muda do galaxy note 9 para a geraã§ã£o anterior, o galaxy note 8, e se vale a pena trocar")
        maior = count
        n_line_maior = linha
print("os", count_os, "o", count_o, "as", count_as, "a", count_a)
#print("media", media)
print("linha com menos", n_line_menor, "com {} ocorrências".format(menor))
print("linha com mais", n_line_maior, "com {} ocorrências".format(maior))
