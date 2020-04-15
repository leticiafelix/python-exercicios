#faça um programa que leia um numero n inteiro e mostre na tela os n
#primeiros elementos de uma seq de fibonacci

print('{:=^50}'.format(' FIBONACCI '))

from emoji import emojize

n = int(input('Quantos termos você deseja visualizar? '))

n1 = 0
n2 = 1
i = 3

if n == 1:
    print(0, emojize(':arrow_right:', use_aliases=True), end = ' ')
elif n == 2:
    print(0, emojize(':arrow_right:', use_aliases = True), 1, end = ' ')
else:
    print(0, emojize(':arrow_right:', use_aliases=True), 1, emojize(':arrow_right:', use_aliases=True), end=' ')
    while i <= n:
        ni = n1 + n2
        print(ni, emojize(':arrow_right:', use_aliases = True), end = ' ')

        n1 = n2
        n2 = ni
        i += 1

print('Fim')
