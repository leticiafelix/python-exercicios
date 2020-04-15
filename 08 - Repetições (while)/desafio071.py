#faça um programa que simula o funcionamento de um caixa eletrônico
#no inicio pergunte ao usuario qual o valor a ser sacado (inteiro)
#o programa informa quantas cédulas de cada valor serão entregues
#considere que o caixa possui cédulas de 20, 50, 10 e 1 real


print('--------------------------------')
print('           BANCO CEV            ')
print('--------------------------------')

cedulas = 0
ced = 50
total = float(input('Valor do saque: R$'))

while True:

    if total >= ced:
        cedulas = total // ced #este operador é o floor division, retorna apenas a parte inteira da divisão
        total -= cedulas*ced
    else:
        if cedulas > 0:
            print(f'{cedulas:.0f} cédulas de R${ced:.2f}.')

        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1

        cedulas = 0

        if total == 0:
            break

print('Volte sempre ao Banco CEV! Tenha um bom dia!')
