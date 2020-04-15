#crie um programa que faça o computador jogar Jokenpô

print('\033[35m{:-^20}\033[m'.format(':: JOKENPÔ! ::'))

user = int(input('Insira sua jogada \033[37m([1] pedra, [2] papel ou [3] tesoura)\033[m:'))

if user == 1:
    user = 'pedra'
elif user == 2:
    user = 'papel'
elif user == 3:
    user = 'tesoura'

from time import sleep

print('PEDRA, PAPEL OU TESOOOURA?!')
sleep(1)

from random import choice

computer = ('pedra','papel','tesoura')
computer = choice(computer)

if user == computer:
    print('\033[33mEMPATE! Nós dois escolhemos {}.\033[m'.format(user))
elif user == 'tesoura':
    if computer == 'pedra':
        print('\033[31mVOCÊ PERDEU! Eu escolhi {} e você {}.\033[m'.format(computer,user))
    else:
        print('\033[32mVOCÊ VENCEU! Eu escolhi {} e você {}.\033[m'.format(computer,user))
elif user == 'pedra':
    if computer == 'papel':
        print('\033[31mVOCÊ PERDEU! Eu escolhi {} e você {}.\033[m'.format(computer, user))
    else:
        print('\033[32mVOCÊ VENCEU! Eu escolhi {} e você {}.\033[m'.format(computer, user))
elif user == 'papel':
    if computer == 'pedra':
        print('\033[32mVOCÊ VENCEU! Eu escolhi {} e você {}\033[m.'.format(computer, user))
    else:
        print('\033[31mVOCÊ PERDEU! Eu escolhi {} e você {}.\033[m'.format(computer, user))
