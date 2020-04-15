#crie um programa que leia 6 numeros inteiros e mostre a soma apenas dos que forem pares
#se o número for impar, desconsidere-o

print('{:=^50}'.format(' SOMA DOS ÍMPARES '))

s = 0
cont = 0

for i in range(1,7):
    n = int(input('Insira o {}° número inteiro: '.format(i)))
    if n%2==0:
        s += n
        cont += 1

print('Você informou {} números pares e a soma deles é {}.'.format(cont,s))
