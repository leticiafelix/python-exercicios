from time import sleep

def titulo(txt, color = 0):
    print(f'\033[3{color}m:\033[m' * 60)
    print(f'\033[3{color}m{txt:^60}\033[m')
    print(f'\033[3{color}m:\033[m'*60)


def menu(opcoes = ['OPÇÃO 1','OPÇÃO 2', 'OPÇÃO 3']):
    select = 0
    valido = False
    while True:
        try:
            titulo('MENU', 6)
            for i, j in enumerate(opcoes):
                print(f'\033[36m[{i+1}]\033[m - {j.upper().strip()}')
            select = int(input('SELECIONE UMA OPÇÃO: ')) - 1
        except:
            print('\033[31mOpção Inválida.\033[m')
        else:
            if select not in range(0, len(opcoes)):
                print('\033[31mOpção Inválida.\033[m')
            else:
                titulo(f'{opcoes[select]}')
                valido = True
        if valido:
            break
    return select


def cadastroexiste():
    try:
        cadastro = open('cadastro', mode = 'r')
        cadastro.close()
    except:
        print('Ainda não há cadastro. Criando novo arquivo...')
        sleep(2)
        cadastro = open('cadastro', mode = 'a')
        cadastro.write(f'{"Nome":^30}{"Idade":^30}')
        cadastro.close()
        print('\033[32mO arquivo \'cadastro\' foi criado com sucesso.\033[m')


def cadastrar():
    cadastro = open('cadastro', mode='a')
    while True:
        nome = input('Nome: ').strip().title()
        if nome.isspace() or nome.isnumeric():
            print('\033[31mEntrada Inválida.\033[m')
        else:
            print('\033[32mNome cadastrado com sucesso.\033[m')
            break
    while True:
        try:
            idade = int(input('Idade: '))
        except:
            print('\033[31mEntrada Inválida.\033[m')
        else:
            print('\033[32mIdade cadastrada com sucesso.\033[m')
            break

    cadastro.write(f'\n{nome:^30}{idade:^30}')
    cadastro.close()


def vercadastro():
    cadastro = open('cadastro', mode='r')
    print(cadastro.read())
    cadastro.close()
