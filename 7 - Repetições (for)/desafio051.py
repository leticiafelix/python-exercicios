#crie um programa que leia o primeiro termo e a razão de uma PA, no final mostre os 10 primeiros termos dessa PA

print('{:=^50}'.format(' 10 PRIMEIROS TERMOS DE UMA PA '))

n = int(input('Insira o primeiro termo da PA: '))
r = int(input('Insira a razão da PA: '))

from emoji import emojize

for i in range(n,n+((11-1)*r),r):
    print('{}'.format(i),emojize(':arrow_right: ',use_aliases=True), end='')
print('FIM')
