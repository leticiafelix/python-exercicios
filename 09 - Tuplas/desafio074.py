#faça um programa que gere 5 numeros aleatórios e coloque numa tupla, depois disso mostre a listagem dos números gerados
#e indique o menor e o maior valor da tupla

from random import randint

n = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))

print(f'Os valores sorteados foram: {n}'
      f'\nO menor valor é: {min(n)}'
      f'\nO maior valor é: {max(n)}')
