#faça um programa que leia o nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionario
#se por acaso a CTPS for diferente de ZERO, o dicionario receberá também o ano de contratação e o salário
#calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar
#supondo que se aposenta apos 35 anos de colaboração

from datetime import datetime

print('-'*60)
print(f'{"CADASTRO":^60}')
print('-'*60)

cadastro = {}

cadastro['Nome: '] = str(input('Nome: ')).strip().title()
cadastro['ano'] = int(input('Ano de nascimento: '))
cadastro['mês'] = int(input('Mês de nascimento: '))
cadastro['dia'] = int((input('Dia de nascimento: ')))
cadastro['Carteira: '] = int(input('Número da Carteira de Trabalho (0 se não tiver): '))

ano = datetime.now().year
mes = datetime.now().month
dia = datetime.now().day

if cadastro['mês'] < mes:
    if dia < cadastro['dia']:
        cadastro['Idade: '] = ano - cadastro['ano']
else:
    cadastro['Idade: '] = ano - cadastro['ano'] - 1

if cadastro['Carteira: '] != 0:
    cadastro['Contratação: '] = int(input('Ano de contratação: '))
    cadastro['Salário: R$'] = float(input('Salário: R$'))

    cadastro['Idade de aposentadoria: '] = (cadastro['Contratação: '] - cadastro['ano'] + 35)


print('-'*60)
print(f'{"CADASTRO":^60}')
print('-'*60)

for k, v in cadastro.items():
    if k != 'ano' and k != 'mês' and k != 'dia':
        print(f'{k}{v}')

print('-'*60)
