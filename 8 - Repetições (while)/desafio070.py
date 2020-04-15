#crie um programa que leia o nome e preço de varios produtos, entre cada produto pergunta se o usuario quer continuar.
#no final mostre:
#a) qual o total gasto na compra, b) quantos produtos custam mais de R$1000,00 e c) qual o nome do produto mais barato

rpt = ''
cont = 0
total = 0
mais_1000 = 0
barato = ''
barato_valor = 0

print('      ::: LOJAS CEV :::      ')

while True:
    cont += 1
    print('----- PRODUTO {} -----'.format(cont))
    prod = str(input('Nome: ')).strip().title()
    valor = float(input('Valor: R$'))
    print('\033[32mProduto cadastrado com sucesso!\033[m')
    total += valor

    if valor > 1000:
        mais_1000 += 1

    if cont == 1:
        barato = prod
        barato_valor = valor
    elif valor < barato_valor:
        barato = prod
        barato_valor = valor

    rpt = str(input('Cadastrar novo produto? [S/N] ')).strip().upper()

    while rpt != 'S' and rpt != 'N':
        rpt = str(input('\033[31mInsira uma resposta válida.\033[m')).strip().upper()

    if rpt == 'N':
        break

print('----------------------------------------------')
print(f"""Produtos: {cont}
Total: R${total:.2f}
Produtos acima de R$1000,00: {mais_1000}
Produto mais barato: {barato}""")
print('----------------------------------------------')
