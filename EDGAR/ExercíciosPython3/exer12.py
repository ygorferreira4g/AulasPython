np1 = float(input('Digite a nota 01:'))
np2 = float(input('Digite a nota 02:'))

md = 2
n1 = 5
n2 = 7

Media = (np1 + np2) / md

if Media >= n2 :
    print('Aluno Aprovado')

elif Media >= 5 and Media < 7  :
    print('Aluno de exame final')

elif Media < 5:
    print('Aluno reprovado')    


