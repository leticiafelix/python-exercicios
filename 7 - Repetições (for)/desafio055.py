#crie um programa que leia o peso de 5 pessoas e mostre qual foi o maior e o menor peso lido

print('{:=^50}'.format(' MAIOR E MENOR PESO '))

max = 0
min = 0

for i in range(1,6):
    peso = float(input('Qual o peso da {}° pessoa? (kg) '.format(i)))
    if i == 1:
        max = peso
        min = peso
    else:
        if peso > max:
            max = peso
        if peso < min:
            min = peso

print('O menor peso é {}kg e o maior é {}kg.'.format(min,max))
