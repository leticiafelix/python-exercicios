#refaça o desafio 035 dos triângulos acrescentando o recurso de mostrar que tipo de triângulo será formado
#equilatero - todos os lados iguais
#isósceles - dois lados iguais
#escaleno - todos os lados diferentes

print('{:=^50}'.format(' ANALISADOR DE TRIÂNGULOS II '))

import math

r1 = float(input('Insira a medida da primeira reta: '))
r2 = float(input('Insira a medida da segunda reta: '))
r3 = float(input('Insira a medida da terceira reta: '))

if (math.fabs(r1-r2)<r3 and (r1+r2)>r3 and math.fabs(r2-r3)<r1 and r1<(r2+r3) and math.fabs(r1-r3)<r2 and r2<(r1+r3)):
    conf = 'sim'
    print('As retas de medidas: {}, {} e {} podem formar um triângulo.'.format(r1,r2,r3))
else:
    conf = 'não'
    print('As retas de medidas {}, {} e {} não podem formar um triângulo.'.format(r1,r2,r3))

if conf == 'sim':
    if r1 == r2 and r1 == r3:
      print('O triângulo será equilátero.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('O triângulo será isósceles.')
    else:
     print('O triângulo será escaleno.')
