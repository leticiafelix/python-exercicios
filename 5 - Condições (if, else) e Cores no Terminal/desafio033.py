#crie um programa que leia 3 numeros e mostre qual o maior e qual o menor

print('{:=^50}'.format(' MAIOR E MENOR '))

n1 = float(input('Digite um número: '))
n2 = float(input('Digite mais um número: '))
n3 = float(input('Digite mais um número: '))

min = n1
if n2<min:
    min = n2
if n3<min:
    min = n3

max = n1
if n2>max:
    max = n2
if n3>max:
    max = n3

print('O menor número é {}, o maior é {}.'.format(min,max))
