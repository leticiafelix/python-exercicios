#faça um programa que tenha função chamada escreva() que receba um texto qualquer como parâmetro
#e mostre uma mensagem com tamanho adaptavel. (as linhas em cima e embaixo vão ser do tamanho do texto)

def escreva(txt):
    l = len(txt)
    print('-' * l)
    print(f'{txt:^{l}}')
    print('-' * l)

#programa principal
escreva('lalala')
escreva('     LETÍCIA FELIX      ')
escreva('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
