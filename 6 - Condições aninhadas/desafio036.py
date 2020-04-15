#crie um programa para aprovar emprestimo pra compra de uma casa
#leia o valor da casa, o salario do comprador e em quantos anos ele vai pagar
#calculd o valor da prestação mensal, sabendo que não pode exceder 30% do salario
#se exceder, o emprestimo será negado

print('{:=^50}'.format(' FINANCIAMENTO DE CASA '))

val = float(input('Qual o valor da casa? '))
sal = float(input('Qual o seu salário? '))
anos = int(input('Em quantos anos você quer pagar o imóvel? '))

pres = val/(anos*12)

if pres>sal*0.3:
    print('\033[31mInfelizmente você não pode financiar este imóvel. As prestações de R$:{:.2f} excedem os R$:{:.2f} correspondentes a 30% do seu salário.\033[m'.format(pres,sal*0.3))
else:
    print('\033[32mVocê poderá financiar este imóvel com {} prestações de R$:{:.2f}.\033[m'.format(anos*12,pres))
