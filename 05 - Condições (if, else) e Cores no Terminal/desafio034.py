#crie um programa que leia o salario de um funcionario e calcule o aumento
#salarios superiores a R$1250,00 recebem um aumento de 10%
#salarios inferiores ou iguais recebem um aumento de 15%

print('{:=^50}'.format(' AUMENTO DE SALÁRIO '))

sal = float(input('Insira o salário: '))

if sal<=1250:
    nsal = sal*1.15
    print('Com um aumento de 15%, o salário vai de R${:.2f} para R$:{:.2f}.'.format(sal, nsal))
else:
    nsal = sal*1.1
    print('Com um aumento de 10%, o salário vai de R${:.2f} para R$:{:.2f}.'.format(sal,nsal))
