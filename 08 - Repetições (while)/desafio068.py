#crie um programa que jogue par ou ímpar com o usuário
#o jogo será interrompido quando o jogador perder, mostrando o total de vitorias consecutivas que ele conquistou

from random import randint
from time import sleep

while True:
    vit = 0

    while True:
        print(':::: Par ou Ímpar ::::')
        n = float(input('Escolha um número inteiro de 1 a 10: '))

        while not n in range(1,11):
            n = float(input('\033[31mPor favor, insira um inteiro de 1 a 10.\033[m'))

        user = str(input("""Par ou Ímpar? [P/I]: """)).strip().upper()

        while user != 'P' and user != 'I':
            user = str(input('\033[31mPor favor, insira uma resposta válida.\033[m')).strip().upper()

        computador = randint(1,10)
        soma = n + computador

        if soma % 2 == 0:
            if user == 'P':
                vit += 1
                print('\033[32mParabéns, você venceu! Você escolheu {:.0f} e eu {}. {:.0f} é par.\033[m'.format(n, computador, soma))
                print('Vamos jogar novamente...')
            else:
                print('\033[31mVocê perdeu! Você escolheu {:.0f} e eu {}. {:.0f} é par.\033[m'.format(n, computador, soma))
                break
        else:
            if user == 'I':
                vit += 1
                print('\033[32mParabéns, você venceu! Você escolheu {:.0f} e eu {}. {:.0f} é ímpar.\033[m'.format(n,computador,soma))
                print('Vamos jogar novamente...')
            else:
                print('\033[31mVocê perdeu! Você escolheu {:.0f} e eu {}. {:.0f} é par.\033[m'.format(n, computador, soma))
                break

    print('Fim, você venceu {} vezes consecutivas.'.format(vit))

    sleep(2)

    jogar = str(input('Deseja reiniciar? [S/N]: ')).strip().upper()

    while jogar != 'S' and jogar != 'N':
        jogar = str(input('\033[31mPor favor, insira uma resposta válida. \033[m')).strip().upper()

    if jogar == 'N':
        break

print('Jogo encerrado. Volte sempre!')
