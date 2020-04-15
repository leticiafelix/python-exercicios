#crie um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio indo de 10 a 0
#com uma pausa de 1 seg entre eles

print('{:=^50}'.format(' CONTAGEM REGRESSIVA '))

from time import sleep
import emoji

for i in range(10,-1,-1):
    sleep(1)
    print('{}...'.format(i))
print('FELIZ ANO NOVO!!! {}'.format(emoji.emojize(':boom:',use_aliases=True)))
