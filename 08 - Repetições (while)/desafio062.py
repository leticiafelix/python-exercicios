#melhore o desafio062 mas ao inves de acabar ele pergunta se quer mostrar mais
#quantos termos, o prog só para quando a pessoa quiser mostrar
#mais 0 termos

print('{:=^50}'.format(' TERMOS DE UMA PA '))
from emoji import emojize

a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))

termos = 10
i = 0
cont = 0

while termos != 0:

    while i < termos:
        print(a1, emojize(':arrow_right:', use_aliases= True), end = ' ')
        a1 += r
        i += 1
        cont += 1

    print('Pausa...')
    i = 0

    termos = int(input('Quantos termos a mais você deseja visualizar? '))

print('Fim. Você visualizou {} termos.'.format(cont))
