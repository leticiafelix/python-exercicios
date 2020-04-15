#crie um programa que leia um numero qualquer e mostre o seu fatorial

print('{:=^50}'.format(' FATORIAL! '))

n = int(input('Insira um número inteiro: '))
fat = n

while not n == 1:
    fat = fat*(n-1)
    n -= 1

print(fat)
