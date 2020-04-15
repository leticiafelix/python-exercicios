#leia um numero real e mostre na tela sua porção inteira
import math

num = float(input('Digite um número real:'))
print('A porção inteira de {} é {}'.format(num,math.trunc(num)))
