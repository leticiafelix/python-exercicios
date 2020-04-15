#refaça o desafio051 lendo o primeiro termo e a razao de uma PA
#mostrando os 10 primeiros termos dda PA utilizando o while

print('{:=^50}'.format(' 10 PRIMEIROS TERMOS DE UMA PA '))
from emoji import emojize

a1 = int(input('Primeiro Termo: '))
r = int(input('Razão: '))

i = 0
while not i == 10:
    print(a1,emojize(':arrow_right:',use_aliases= True),end=' ')
    a1 = a1 + r
    i = i + 1
print('FIM')
