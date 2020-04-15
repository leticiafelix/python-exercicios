#crie um programa que calcule o valor a ser pago por um produto considerando seu preço normal e a condição de pagamento
#a vista no dinheiro/cheque: 10% de desconto
#a vista no cartão: 5% de desconto
#em até 2x no cartão: preço normal
#3x ou mais no cartão: 20% de juros

print('{:=^50}'.format(' PAGAMENTO '))

preco = float(input('Valor: '))
pag = int(input("""Forma de pagamento: 
\033[32m[1]\033[m \033[32mDINHEIRO\033[m 
\033[36m[2]\033[m \033[36mCARTÃO (à vista)\033[m 
\033[35m[3]\033[m \033[35mCARTÃO (parcelado)\033[m """))

if pag == 3:
    parc = int(input('Em quantas parcelas você deseja pagar? (sem juros até 2x, acima com 30% de juros): '))
    if parc <= 2:
        print('Valor a pagar: R$:{:.2f} em {} parcela(s) de R$:{:.2f}'.format(preco,parc,preco/parc))
    else:
        print('Valor a pagar: R$:{:.2f} em {} parcelas de R$:{:.2f}'.format(preco*1.2,parc,(preco*1.2)/parc))
elif pag == 2:
    print('Valor a pagar: R$:{:.2f} (5% de desconto)'.format(preco*0.95))
else:
    print('Valor a pagar: R$:{:.2f} (10% de desconto)'.format(preco*0.9))
