#crie um programa que leia um ano qualquer e mostre se ele é bissexto

print('{:=^50}'.format(' ANOS BISSEXTOS '))

ano = int(input('Insira um ano (para analisar o ano atual, digite 0): '))

from datetime import date

if ano == 0:
    ano = date.today().year

if ano%4==0 and ano%100!=0 or ano%400==0:
    print('O ano de {} é bissexto.'.format(ano))
else:
    print('O ano de {} não é bissexto.'.format(ano))
