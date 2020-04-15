#crie um programa que leia dois valores e mostre um menu na tela
#[1] somar [2] mult [3] maior [4] novos numeros [5] sair do programa

print('{:=^50}'.format(' MENU DE OPERAÇÕES '))

from time import sleep

menu = 0
op = 0
n1 = float(input('Insira o primeiro número: '))
n2 = float(input('Insira o segundo número: '))

while not menu == 5:
    menu = float(input(
"""    
   :: MENU ::
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR
    """))

    while not menu in range(1,6):
        menu = float(input('\033[31mEscolha uma opção válida.\033[m'))

    if menu == 1:
        op = n1 + n2
        print('SOMA :: {} + {} = {:.2f}'.format(n1,n2,op))
        sleep(2)
    elif menu == 2:
        op = n1 * n2
        print('MULTIPLICAÇÃO :: {} x {} = {:.2f}'.format(n1,n2,op))
        sleep(2)
    elif menu == 3:
        op = max(n1,n2)
        print( 'MAIOR :: O maior entre {} e {} é {:.2f}.'.format(n1,n2,op))
        sleep(2)
    elif menu == 4:
        n1 = float(input('Insira o primeiro número: '))
        n2 = float(input('Insira o segundo número: '))

print('Fim do programa. Volte sempre!')
