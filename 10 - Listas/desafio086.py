#faça um programa que crie uma matriz 3x3 e preencha com valores lidos pelo teclado
#no final mostre a matriz na tela com a formatação correta

v = [[],[],[]]

for i in range(0,3):
    for j in range(0,3):
        v[i].append(int(input(f'Insira um número para a posição [{i+1},{j+1}]: ')))


print('-'*40)
print('Sua matriz: ')

for i in range(0,3):
    for j in range(0,3):
        print(f'[ {v[i][j]:^5} ]', end = '')
    print()
