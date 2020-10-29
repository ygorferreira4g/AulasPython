alunoCodigo = []
alunoAltura = []
alunoPeso = []
codigo = 1
indice = 0
maisAlto = 0
maisBaixo = 0
maisGordo = 0
maisMagro = 0

def ordenar(listagem, maior, menor):
    if indice == 0:
        maior = menor = listagem[indice]
    else:
        if listagem[indice] > maior:
            maior = listagem[indice]
        if listagem[indice] < menor:
            menor = listagem[indice]
    return (maior, menor)

while codigo > 0:
    codigo = int(input("Digite seu Código ou Digite 0 para finalizar: "))
    if codigo >= 1:
        alunoCodigo.append(codigo)
        alunoAltura.append(int(input("Digite sua altura: ")))
        maisAlto, maisBaixo = ordenar(alunoAltura, maisAlto, maisBaixo)
        alunoPeso.append(int(input("Digite seu Peso: ")))
        maisGordo, maisMagro = ordenar(alunoPeso, maisGordo, maisMagro)
        indice += 1

def codigoAlunoBusca(listagem, oquebuscar, alunoCodigo):
    for i, v in enumerate(listagem):
        if v == oquebuscar:
            print(f'Código: {alunoCodigo[i]}')
print(f'Altura do mais Baixo: {maisBaixo} Mts', end=' ')
codigoAlunoBusca(alunoAltura, maisBaixo, alunoCodigo)
print(f'Altura mais Alto: {maisAlto} Mts', end=' ')
codigoAlunoBusca(alunoAltura, maisAlto, alunoCodigo)
print(f'Peso do mais Magro: {maisMagro} Kg', end=' ')
codigoAlunoBusca(alunoPeso, maisMagro, alunoCodigo)
print(f'Peso do mais Gordo: {maisGordo} Kg', end=' ')
codigoAlunoBusca(alunoPeso, maisGordo, alunoCodigo)

print(f'Media da altura: {sum(alunoAltura)/len(alunoAltura)} Mts')
print(f'Media da peso: {sum(alunoPeso)/len(alunoPeso)} Mts')