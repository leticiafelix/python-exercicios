#crie um código que faça o computador pensar em um número inteiro entre 0 e 5
#peça para o usuario tentar descobrir qual numero o pc escolheu
#diga se o usuario perdeu ou venceu

print('{:=^50}'.format('Advivinhação'))
print('Vou pensar em um número de 0 a 5 e você tenta adivinhar, ok?')

from random import randint
n = randint(0,5)

from time import sleep
print('Pensando em um número...')
sleep(3)

print('Pronto! Escolhi um número entre 0 e 5.')
n1 = int(input('Tente adivinhar: '))

if n==n1:
    print("Uau! Você acertou!")
else:
    print('Você perdeu! O número que eu escolhi foi {}.'.format(n))
