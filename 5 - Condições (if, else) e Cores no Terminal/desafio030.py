#crie programa que leia um numero inteiro qualquer e diga se é par ou ímpar

print('{:=^50}'.format(' PAR OU ÍMPAR '))

n = int(input('Digite um número inteiro: '))

if n%2==0:
    print('O número {} é par.'.format(n))
else:
    print('O número {} é ímpar.'.format(n))
