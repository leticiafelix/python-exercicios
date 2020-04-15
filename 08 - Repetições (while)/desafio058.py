#melhore o jogo do desafio028 onde o pc vai pensar em um numero
#entre 0 e 10, mas agora o jogador tenta até acertar
#no final mostra quantos palpites foram necessários para vencer

from time import sleep
from random import randint

print('\033[35m{:=^50}\033[m'.format(' :: Jogo da Adivinhação :: '))
inicio = 1

while inicio == 1:
    sleep(1)
    print('Vou pensar em um número entre 0 e 10, você deve tentar adivinhar.')
    sleep(2)
    print('Pensando em um número...')
    computador = randint(0,10)
    sleep(3)
    print('Pronto!')

    cont = 0
    user = 100

    while not user == computador:
        cont += 1

        while not user in range(0,11):
            user = float(input('Em que número eu pensei? '))
            if not user in range(0,11):
                print('\033[31mO número deve ser um inteiro entre 0 e 10.\033[m')

        if user != computador:
            if user < computador:
                print('\033[31mMais... tente novamente.\033[m')
                user = ''
            else:
                print('\033[31mMenos... tente novamente.\033[m')
                user = ''
        else:
            print('\033[32mParabéns! Você acertou em {} tentativas. Eu tinha pensado no {}.\033[m'.format(cont,computador))

    inicio = 0
    sleep(2)

    print('\033[35m{:=^50}\033[m'.format(' :: Jogo da Adivinhação :: '))
    inicio = float(input("""[1] JOGAR NOVAMENTE
[2] SAIR """))

    while not inicio in range(1,3):
        inicio = float(input('Por favor, insira uma opção válida.'))
