#faça um programa que tenha uma tupla com várias palavras (não use acentos)
#depois disso mostre pra cada palavra quais são suas vogais

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
            'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for i in range(0, len(palavras)):
    print(f'\nNa palavra {palavras[i].upper()} temos', end=' ')
    for j in range(0, len(palavras[i])):
        if palavras[i][j] in 'aeiou':
            print(palavras[i][j], end = ' ')
