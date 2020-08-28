Lista = [1, 2, 3]
Copia = Lista
Lista.append(4)
print(Copia)

# Porque o APPEND Adiciona qualquer valor completo, por exemplo, se enviarmos um objeto, ele adiciona 
# o objeto, se enviarmos uma lista, ele adiciona a lista inteira ao invés de seus itens e nesse caso
#  ele adicionou o numero 4 no print.