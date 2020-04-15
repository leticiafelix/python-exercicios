#faça um programa que gerencie o aproveitamento de um jogador de futebol
#o programa vai ler o nome e quantas partidas ele jogou
#depois vai ler a quantidade de gols feitos em cada partida
#no final, tudo ser'á guardado em um dicionário incluindo o total de gols feitos durante o campeonato

print('-'*50)
print(f'{"CADASTRO":^50}')
print('-'*50)

jogador = {}

jogador['Nome: '] = str(input('Nome: ')).strip().title()
jogador['Partidas: '] = int(input('Partidas Jogadas: '))
jogador['Gols: '] = []

soma = 0
for i in range(0,jogador['Partidas: ']):
    jogador['Gols: '].append(int(input(f'Gols na partida {i+1}: ')))
    soma += jogador['Gols: '][i]

jogador['Total de Gols: '] = soma

print('-'*50)
print(f'{jogador["Nome: "].upper():^50}')
print('-'*50)

for k, v in jogador.items():
    print(f'{k}{v}')

print('-' * 50)
