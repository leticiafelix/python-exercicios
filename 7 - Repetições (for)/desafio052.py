#crie um programa que leia um numero inteiro e diga se ele é ou não um número primo (só é divisível por 1 e por ele msm)

print('{:=^50}'.format(' NÚMEROS PRIMOS '))

n = int(input('Insira um número inteiro: '))
cont = 0

for i in range(1,n+1):
    if n%i == 0:
        cont += 1
        print('\033[32m{}\033[m'.format(i), end=' ')
    else:
        print('\033[31m{}\033[m'.format(i), end=' ')

if cont != 2:
    print('\n O número {} foi divisível {} vezes, então ele não é primo.'.format(n,cont))
else:
    print('\n O número {} foi divisível apenas por 1 e {}, logo ele é primo.'.format(n,n))
