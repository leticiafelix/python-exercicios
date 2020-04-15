#crie um programa que pergunte a distancia de uma viagem em km
#calcule o preço da passagem cobrando R$0,50 por km para viagens até 200km e R$0,45 para viagens mais longas

print('{:=^50}'.format(' PREÇO DE PASSAGEM '))

d = float(input('Qual a distância da viagem? '))

if d<=200:
    p = d*0.5
else:
    p = d*0.45

print('A passagem custa R${:.2f}.'.format(p))
