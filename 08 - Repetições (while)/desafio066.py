#faça um programa que leia varios numeros inteiros, o programa só para quando o usuario digitar 999 (usando o break)
#no final mostre quantos numeros foram digitados e qual foi a soma entre eles (desconsiderando o flag 999)

soma = 0
i = 0

while True:
    n = int(input('Insira um número inteiro (999 para parar): '))
    if n == 999:
        break
    soma += n
    i += 1

print(f'A soma dos {i} números que você inseriu é igual a {soma}.')
