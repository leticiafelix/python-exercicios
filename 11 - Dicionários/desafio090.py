# faça um programa que leia o nome, a média de um aluno
# e escreva a situação dele em um dicionario
# no fim mostre o conteúdo da estrutura na tela
# obs: media 7 para aprovação

boletim = {'nome': str(input('Nome: ')).strip().title(), 'media': float(input('Média: '))}

if boletim['media'] >= 7:
    boletim['Situação'] = 'aprovado'
else:
    boletim['Situação'] = 'recuperação'

print('-'*30)
for k, v in boletim.items():
    print(f'{k} é igual a {v}')
