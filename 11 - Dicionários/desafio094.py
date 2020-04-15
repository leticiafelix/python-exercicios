#faça um programa que leia nome, sexo e idade de várias pessoas guardando os dados de cada pessoa em um dicionário
#guarde todos os dicionarios em uma lista. no final, mostre
#a) quantas pessoas foram cadastradas
#b) média de idade do grupo
#c)lista com todas as mulheres
#d)lista com todas as pessoas com idade acima da média

lista = []

print('-'*60)
print(f'{"CADASTRO":^60}')
print('-'*60)

n = 0
while True:
    lista.append({})
    lista[n]['nome'] = str(input('Nome: ')).strip().title()
    lista[n]['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()

    while not lista[n]['sexo'] in 'MF' or lista[n]['sexo'] == '':
        lista[n]['sexo'] = str(input('\033[31mInsira uma resposta válida. \033[m')).strip().upper()

    lista[n]['idade'] = int((input('Idade: ')))
    print('\033[32mCadastro efetuado com sucesso!\033[m')
    n += 1

    rpt = str(input('Deseja continuar a cadastrar? [S/N] ')).strip().upper()

    while not rpt in 'SN' or rpt == '':
        rpt = str(input('\033[31mInsira uma resposta válida. \033[m')).strip().upper()

    if rpt == 'N':
        break

soma = 0
mulheres = []
for i in range(0,len(lista)):
    soma += lista[i]['idade']
    if lista[i]['sexo'] == 'F':
        mulheres.append(lista[i]['nome'])

media = soma/n

acimamed = []
for i in range(0,len(lista)):
    if lista[i]['idade'] > media:
        acimamed.append(lista[i]['nome'])

print('-'*60)
print(f'{"RESULTADO":^60}')
print('-'*60)

print(f"""Pessoas cadastradas: {n}
Média de idade: {media:.2f}
Mulheres cadastradas: """, end = '')

for i in range(0,len(mulheres)):
    print(f'[{mulheres[i]}]', end = ' ')
print()

print('Pessoas com idade acima da média: ', end = '')
for i in range(0,len(acimamed)):
    print(f'[{acimamed[i]}]', end = ' ')
print()
print('-'*60)
