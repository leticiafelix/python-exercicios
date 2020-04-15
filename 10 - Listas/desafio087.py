#aprimore o desafio086, mostrando no final a soma dos valores pares
#a soma dos valo res da terceira coluna e omaior valor da segunda linha

v = [[],[],[]]
soma = [[0],[0]]
max = 0

for i in range(0,3):
    for j in range(0,3):
        v[i].append(int(input(f'Insira um número para a posição [{i+1},{j+1}]: ')))


print('-'*40)
print('Sua matriz: ')
for i in range(0,3):
    for j in range(0,3):
        if i == 1:
            if j == 0:
                max = v[i][j]
            elif v[i][j] > max:
                max = v[i][j]
        if j == 2:
            soma[1][0] += v[i][j]
        if v[i][j] % 2 == 0:
            soma[0][0] += v[i][j]
        print(f'[ {v[i][j]:^4} ]', end='')
    print()

print('-'*40)
print(f"""Soma dos pares: {soma[0][0]}
Soma da 3° coluna: {soma[1][0]}
Maior valor da 2° linha: {max}""")
