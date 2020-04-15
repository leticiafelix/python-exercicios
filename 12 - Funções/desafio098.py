#faça uma função chamada contador() que receba três parametros
#inicio, fim e passo e realize a contagem
#o programa tem que realizar três contagens através da função criada
# de 1 a 10 de 1 em 1
#de 10 a 0 de 2 em 2
#uma contagem personalizada

import math
from time import sleep

def titulo(txt):
    print('-'*60)
    print(f'{txt:^60}')
    print('-'*60)

def contador(inicio, fim , passo):
    l = 0
    passo = int(math.fabs(passo))
    if passo == 0:
        passo = 1

    titulo(f'CONTAGEM {inicio} A {fim} (PASSO {passo:.0f})')
    if inicio > fim:
        for i in range(inicio, fim - 1, - passo):
            l += 1
            sleep(0.4)
            print(i, end=' -> ')
            if l % 8 == 0:
                print()
        print('FIM')
    else:
        for i in range(inicio, fim + 1, passo):
            l += 1
            sleep(0.4)
            print(i, end=' -> ')
            if l % 8 == 0:
                print()
        print('FIM')
        print('-'*60)


#programa principal
contador(1,10,1)
contador(10,0,2)

print('-'*60)

print('AGORA É A SUA VEZ DE PERSONALIZAR A CONTAGEM!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

contador(i,f,p)
