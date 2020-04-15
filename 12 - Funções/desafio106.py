#crie um mini sistema que utilize o interactive help do python.
#o usuario vai digitar o comando e o manual vai aparecer. quando o usuario digitar a palavra "fim" o programa encerrará
#obs: use cores

def titulo(txt, color = '42'):
    print(f'\033[;{color}m{"-"*len(txt):^70}')
    print(f'{txt:^70}')
    print(f'{"-"*len(txt):^70}')
    print('\033[m', end = '')

def ajuda(c):
    from time import sleep
    titulo(f'ACESSANDO O MANUAL DO COMANDO \'{c}\'...', color = 46)
    sleep(2)
    print('\033[7;30m')
    help(c.lower())
    print('\033[m', end = '')


#programa principal
while True:
    titulo('SISTEMA DE AJUDA')
    c = str(input('Função ou Biblioteca ("fim" para sair): ')).strip().upper()

    if c == 'FIM':
        titulo('ATÉ LOGO!', color='41')
        break
    else:
        ajuda(c)
