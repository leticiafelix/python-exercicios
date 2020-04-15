#faça um programa que tenha uma função chamada fatorial() que receba dois parametros
#o primeiro que indique o numero a calcular e o outro chamado show
#que sera um valor logico opcional indicando se sera mostrado na tela
#ou nao o processo de calculo do fatorial (fazer a funcao com docstring)

def fatorial(n = 1, show = False):
    """
    -> Calcula o fatorial de um número.
    :param n: Número cujo fatorial será calculado.
    :param show: (opcional) Se True, mostra o processo de cálculo do fatorial.
    :return: O fatorial do n inserido como parâmetro.
    Função criada por Letícia Felix.
    """
    fat = 1
    if show:
        print('-'*40)
        print(f'{f"FATORIAL DE {n}":^40}')
        print('-'*40)

    for i in range(n , 0, -1):
        fat *= i
        if show and i !=1:
            print(i, end = ' x ')
        elif show and i == 1:
            print(i, end = ' = ')
    return fat

#PROGRAMA PRINCIPAL
num = int(input('Insira um número inteiro: '))
print(fatorial(num, show = True))
print(fatorial(num))
help(fatorial)
