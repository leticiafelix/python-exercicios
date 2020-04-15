#crie um programa que leia dois numeros inteiros e compare-os
#responda 'o primeiro valor é maior' ou 'o segundo valor é maior' ou 'os dois são iguais'

print('{:=^50}'.format(' COMPARAÇÃO DE NÚMEROS '))

n1 = int(input('Insira um número inteiro: '))
n2 = int(input('Insira outro número inteiro: '))

if n1 == n2:
    print('Os números são iguais.')
elif n2<n1:
    print('O primeiro número é maior.')
else:
    print('O segundo número é maior.')
