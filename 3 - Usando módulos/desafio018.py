#leia um angulo e mostre o sen cos e tg

ang = float(input('Insira um ângulo:'))

import math

sen = math.sin(ang)
cos = math.cos(ang)

print('O seno do ângulo {}° é igual a {} e o cosseno é igual a {}'.format(ang,sen,cos))
