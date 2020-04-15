#faça um programa onde 4 jogadores joguem um dado e tenham resultados aleatorios
#guarde os resultados em um dicionário, no final coloque o dicionario em ordem sabendo que o vencedor
# tirou o maior número no dado

from random import randint
from time import sleep
from operator import itemgetter

jogadores = {}

for i in range(1,5):
    jogadores[f'Jogador {i}'] = randint(1,6)

ranking = {}
ranking = sorted(jogadores.items(), key = itemgetter(1), reverse = True) #a partir daqui raking é uma lista

print('-'*30)
print(f'{"JOGANDO OS DADOS...":^30}')
print('-'*30)

for k, v in jogadores.items():
    sleep(1)
    print(f'{f"{k} tirou {v} no dado.":^30}')

sleep(1)
print('-'*30)
print(f'{"RANKING":^30}')
print('-'*30)

for k, v in enumerate(ranking):
    sleep(1)
    print(f'{f"{k+1}° posição: {v[0]} com {v[1]}":^30}')
