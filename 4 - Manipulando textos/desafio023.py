#faça um programa que leia um numero de 0 a 9999 e mostre cada digito separado
#unidade, dezena, centena, milhar
#como  string e matematicamente

print('{:=^50}'.format('Analise de Número'))

#como string
n_aux = str(input('Digite um inteiro de 0 a 9999: '))
n = '000{}'.format(n_aux)
uni = n[len(n)-1]
dez = n[len(n)-2]
cen = n[len(n)-3]
mil = n[len(n)-4]
print('O número {} tem {} milhares, {} centenas, {} dezenas e {} unidades'.format(n_aux,mil,cen,dez,uni))

#matematicamente

n = int(input('Digite um inteiro de 0 a 9999:'))

import math
mil = math.trunc(n/1000)
cen = math.trunc((n-mil*1000)/100)
dez = math.trunc((n-mil*1000-cen*100)/10)
uni = math.trunc(n-mil*1000-cen*100-dez*10)

print('O número {} tem {} milhares, {} centenas, {} dezenas e {} unidades'.format(n,mil,cen,dez,uni))

#resolução proposta no video
#un = n // 1 % 10
#dez = n // 10 % 10
#cen = n // 100 % 10
#mil = n // 1000 % 10
