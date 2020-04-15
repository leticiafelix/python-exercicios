#crie um programa que leia o comprimento de três retas e diga se elas podem ou nao formar um triangulo

print('{:=^50}'.format(' ANALISADOR DE TRIÂNGULOS I '))

import math

r1 = float(input('Insira a medida da primeira reta: '))
r2 = float(input('Insira a medida da segunda reta: '))
r3 = float(input('Insira a medida da terceira reta: '))

if (math.fabs(r1-r2)<r3 and (r1+r2)>r3 and math.fabs(r2-r3)<r1 and r1<(r2+r3) and math.fabs(r1-r3)<r2 and r2<(r1+r3)):
    print('As retas de medidas: {}, {} e {} podem formar um triângulo.'.format(r1,r2,r3))
else:
    print('As retas de medidas {}, {} e {} não podem formar um triângulo.'.format(r1,r2,r3))
