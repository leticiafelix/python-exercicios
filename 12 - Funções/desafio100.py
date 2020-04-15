#faça um programa que tenha uma lista chamada numeros e duas funções
#uma função sorteia() e outra somapar(). a primeira sorteia
# 5 numeros e coloca dentro de uma lista. a segunda mostra a
#soma entre todos os pares sorteados pela função anterior

from random import randint
from time import sleep

def sorteia(n):
    print('-'*40)
    print(f'{"SORTEIA":^40}')
    print('-'*40)
    print('Sorteando 5 números...')
    for i in range(0,5):
        sleep(1)
        n.append(randint(0,10))
        print(f'[{n[i]}]', end = ' ')
    print()


def somapar(n):
    print('-'*40)
    print(f'{"SOMA PAR":^40}')
    print('-'*40)
    soma = 0
    print('NÚMEROS: ', end = '')
    for i in range(0,len(n)):
        print(f'[{n[i]}]', end = ' ')
        if n[i] % 2 == 0:
            soma += n[i]
    print(f'\nSOMA DOS PARES: {soma}')


#programa principal
numeros = []
sorteia(numeros)
somapar(numeros)
