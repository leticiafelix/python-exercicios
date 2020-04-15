#leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo e calcule a hipotenusa

catop = float(input('Insira o comprimento do cateto oposto:'))
catadj = float(input('Insira o comprimento do cateto adjacente:'))

import math

hip = math.sqrt(catop**2 + catadj**2)

print('A hipotenusa de um triângulo retângulo com cateto oposto de {}cm e cateto adjacente {}cm é igual a {}cm'.format(catop,catadj,hip))
