#crie um programa que leia o ano de nascimento de 7 pessoas, no final mostre quantos atingiram a maioridade (21 anos)
# e quantas ainda não

print('{:=^50}'.format(' MAIORIDADE '))

cont = 0

from datetime import datetime

ano = datetime.today().year

for i in range(1,8):
    n = int(input('Qual o ano de nascimento da {}° pessoa? '.format(i)))
    if (ano - n) >= 21:
        cont += 1

print('{} pessoas já atingiram a maioridade ou vão atingir esse ano ({}).'.format(cont,ano))
