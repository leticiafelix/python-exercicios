#crie um programa que leia a velocidade de um carro
#se ultrapassar 80km/h diga que ele foi multado
#a multa vai custar R$7,00 por cada km acima do limite

print('{:=^50}'.format(' ALUGUEL DE CARROS '))

vel = float(input('Velocidade: '))

if vel>80:
    multa = 7*(vel-80)
    print('{}km/h. Multado! Você estava acima de 80km/h e recebeu uma multa de R$:{:.2f}'.format(vel,multa))
else:
    print('{}km/h. Tenha um bom dia, dirija com segurança!'.format(vel))
