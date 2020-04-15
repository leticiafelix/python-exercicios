#faça um programa que ajude alguem a criar palpites da megasena
#o programa pergunta quantos jogos serão gerados e sorteia 6 numeros entre 1 e 60 para cada jogo.
#cadastrando tudo em uma lista composta (jogos em ordem crescente)

from random import sample

print('-'*40)
print(f'{"MEGA SENA":^40}')
print('-'*40)

n = int(input('Quantos jogos você deseja gerar? '))
jogos = []

for i in range(0,n):
    jogos.append(sample(range(1,61),6))
    jogos[i].sort()

print('-'*40)
print(f'{"SORTEANDO...":^40}')
print('-'*40)

from time import sleep

for i in range(0,len(jogos)):
    sleep(0.7)
    print(f'Jogo {i+1}: {jogos[i]}')

print('-'*40)
print(f'{"BOA SORTE!":^40}')
print('-'*40)
