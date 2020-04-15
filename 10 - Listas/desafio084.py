#faça um programa que leia o nome e peso de varias pessoas e guarde numa lista no final mostre
#a) quantas pessoas foram cadastradas
#b) uma lista com as pessoas mais pesadas e outra com as pessoas mais leves

pessoas = []

while True:
    ind = [str(input('Nome: ')).strip().capitalize(), float(input('Peso: '))]
    pessoas.append(ind[:])
    print('\033[32mCadastro efetuado com sucesso!\033[m')

    rpt = str(input('Deseja continuar a cadastrar pessoas? [S/N] ')).strip().upper()
    while not rpt in 'NS':
        rpt = str(input('\033[31mInsira uma resposta válida.\033[m')).strip().upper()
    if rpt == 'N':
        break

for pos, pessoa in enumerate(pessoas):
    if pos == 0:
        max = pessoa[1]
        min = pessoa[1]
    else:
        if pessoa[1] > max:
            max = pessoa[1]
        elif pessoa[1] < min:
            min = pessoa[1]

pesados = []
leves = []

for pessoa in pessoas:
    if pessoa[1] == max:
        pesados.append(pessoa[0])
    if pessoa[1] == min:
        leves.append(pessoa[0])

print('-'*60)
print(f"""Você cadastrou {len(pessoas)} pessoas.
O maior peso foi de: {max}kg. Peso de {pesados}
O menor peso foi de: {min}kg. Peso de {leves}""")
