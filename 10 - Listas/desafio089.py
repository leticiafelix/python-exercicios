#faça um programa que leia o nome e duas notas de vários alunos e guarde tudo em uma lista composta
#no final mostre um boletim contendo a média de cada um e permita que o usuario
#possa ver as notas de cada aluno individualmente

boletim = []

while True:
    print('-' * 60)
    print(f'{"CADASTRO":^60}')
    print('-' * 60)

    while True:
        nome = str(input('Nome: ')).title().strip()
        n1 = float(input('Nota 1: '))

        while n1<0 or n1>10:
            n1 = float(input('\033[31mA nota deve ser entre 0 e 10. \033[m'))

        n2 = float(input('Nota 2: '))
        while n2<0 or n1>10:
            n1 = float(input('\033[31mA nota deve ser entre 0 e 10. \033[m'))

        boletim.append([nome, [n1,n2], (n1+n2)/2])

        print('\033[32mCadastro efetuado com sucesso!\033[m')

        rpt = str(input('Deseja continuar a cadastrar alunos? [S/N] ')).strip().upper()

        while not rpt in 'NS':
            rpt = str(input('\033[31mInsira uma resposta válida.\033[m')).strip().upper()

        if rpt == 'N':
            break

    print('-' * 60)
    print(f'{"BOLETIM":^60}')
    print('-' * 60)

    print(f'{"N°":^10}{"ALUNO(A)":^35}{"MÉDIA":^15}')
    for i in range(0,len(boletim)):
            print(f'{i:^10}{boletim[i][0]:^35}{boletim[i][2]:^15.2f}')

    menu = 0
    encerrar = 0

    while True:
        print('-' * 60)
        print(f'{"MENU":^60}')
        print('-' * 60)

        menu = int(input("""[1] VER NOTAS DE UM ALUNO
[2] CADASTRAR NOVOS ALUNOS
[3] SAIR
"""))

        while not menu in range(1,4):
            menu = int(input('\033[31mEscolha uma opção válida. \033[m'))

        if menu == 3:
            encerrar = True
            print('-' * 60)
            print('Programa encerrado. Volte sempre! :)')
            break
        elif menu == 1:
            aluno = int(input('Insira o número do aluno para ver suas notas: '))

            while not aluno in range(0,len(boletim)):
                aluno = int(input('\033[31mEscolha um aluno que esteja cadastrado.\033[m'))

            print('-' * 60)
            print(f'{boletim[aluno][0].upper():^60}')
            print('-' * 60)
            print(f'{"NOTA 1":^30}{"NOTA 2":^30}')
            print(f'{boletim[aluno][1][0]:^30.2f}{boletim[aluno][1][1]:^30.2f}')
            print('\n')
            menu = int(input("""[1] MENU
[2] SAIR
"""))
            while not menu in range(1, 3):
                menu = int(input('\033[31mEscolha uma opção válida. \033[m'))

            if menu == 2:
                encerrar = True
                print('-' * 60)
                print('Programa encerrado, volte sempre! :)')
                break

    if encerrar:
        break
