#aprimore o desafio 093 para que ele funcione com varios
#jogadores, incluindo um sistema de visualização de detalhes do aproveitamento
#de cada jogador

from time import sleep

menu = 2
lista = []
n = 0

while True:
    print('-'*60)
    print(f'{"CADASTRO":^60}')
    print('-'*60)

    while True:
        total = 0
        lista.append({})
        lista[n]['nome'] = str(input('Nome: ')).strip().title()
        lista[n]['partidas'] = int(input('Nº de Partidas Jogadas: '))
        lista[n]['gols'] = []
        for i in range(0, lista[n]['partidas']):
            lista[n]['gols'].append(int(input(f'Nº de Gols na Partida {i + 1}: ')))
            total += lista[n]['gols'][i]
        lista[n]['total'] = total
        n += 1
        print('\033[32mCadastro efetuado com sucesso!\033[m')

        rpt = str(input('Deseja continuar a cadastrar? [S/N] ')).strip().upper()

        while rpt != 'S' and rpt != 'N':
            rpt = str(input('\033[31mInsira uma resposta válida.\033[m')).strip().upper()

        if rpt == 'N':
            break

    print('-' * 60)
    print(f'{"RESULTADO":^60}')
    print('-' * 60)

    print(f'{"Nº":^10}{"NOME":^30}{"PARTIDAS":^10}{"GOLS":^10}')

    for i in range(0,len(lista)):
        print(f'{i+1:^10}{lista[i]["nome"]:^30}{lista[i]["partidas"]:^10}{lista[i]["total"]:^10}')
    sleep(5)

    menu = 0
    encerrar = False

    while True:
        print('-' * 60)
        print(f'{"MENU":^60}')
        print('-' * 60)
        menu = int(input("""[1] VER DETALHES DE UM JOGADOR
[2] CADASTRAR NOVOS JOGADORES
[3] SAIR
"""))
        while not menu in range(1,4):
            menu = int(input('\033[31mEscolha uma opção válida. \033[m'))

        if menu == 2:
            break
        elif menu == 3:
            encerrar = True
            break
        elif menu == 1:
            jogador = int(input('Insira o número do jogador: '))-1
            while not jogador in range(0,len(lista)):
                jogador = int(input('\033[31mEscolha um jogador cadastrado. \033[m'))-1
            print('-' * 60)
            print(f'{f"""GOLS DE {lista[jogador]["nome"].upper()}""":^60}')
            print('-' * 60)
            for i in range(0,lista[jogador]['partidas']):
                print(f'{f"PARTIDA {i+1} ":.<55}{lista[jogador]["gols"][i]:^5}')

            print('-' * 60)
            menu = int(input("""[1] MENU
[2] SAIR
"""))
            while not menu in range(1, 3):
                menu = int(input('\033[31mEscolha uma opção válida. \033[m'))
            if menu == 2:
                encerrar = True
                break
    if encerrar:
        break

print('-' * 60)
print(f'{"PROGRAMA ENCERRADO. VOLTE SEMPRE! :)":^60}')
print('-' * 60)
