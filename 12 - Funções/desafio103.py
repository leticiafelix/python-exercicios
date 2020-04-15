#faça um programa que tenha uma função chamada ficha() que receba dois parametros
#opcionais: o nome de um jogador e quantos gols ele marcou o prog deverá ser capaz de mostrar a ficha do jogador
#mesmo que algum dado nao tenha sido informado corretamente

def ficha(nome = '<desconhecido>', gols = 0):
    """
    -> Mostra a ficha do jogador.
    :param nome: nome do jogador
    :param gols: gols feitos
    """
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


#PROGRAMA PRINCIPAL
nome = str(input('Nome do jogador: ')).strip().title()
gols = str(input('Número de gols: '))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome == '':
    nome = '<desconhecido>'

ficha(nome,gols)
