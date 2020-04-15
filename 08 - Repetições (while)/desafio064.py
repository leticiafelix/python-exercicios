#faça um programa que leia varios numeros inteiros pelo teclado
#ele só para quando o usuario digitar 999, que é a condição de parada
#mostre quantos numeros foram digitados e a soma entre eles (desconsiderando o flag 999)

print('{:=^50}'.format(' SOMA DE N NÚMEROS '))
soma = 0
n = 0
i = 0
cont = 0

while not n == 999:
    n = int(input('Insira um número inteiro [999 para sair]: '))
    if n != 999:
        soma += n
    i += 1

print('A soma dos {} números que você inseriu é igual a {}.'.format(i-1,soma))
