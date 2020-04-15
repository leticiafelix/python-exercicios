#faça um programa que leia por quantos dias o carro foi alugado, quantos km foram rodados e retorne o valor a pagar
#o carro custa R$60,00 por dia e R$0,15 por km rodado

dias = int(input('Por quantos dias o carro foi alugado?'))
km = float(input('Quantos km foram rodados?'))
total = dias*60 + km*0.15

print('O total a pagar é de R${:.2f}'.format(total))
