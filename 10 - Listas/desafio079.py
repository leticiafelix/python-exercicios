#faça um programa onde o usuario pode digitar varios valores numericos e cadastre numa lista.
#caso o número ja exista na lista ele não será adicionado novamente. no final serão exibidos todos
#os valores unicos digitados, em ordem crescente

valores = []
cont = 0

while True:
    valores.append(int(input('Insira um número inteiro: ')))

    if valores.count(valores[cont]) > 1:
        del valores[cont]
        print('\033[31mEste número já está na lista. Ele não será adicionado novamente.\033[m')
    else:
        cont += 1
        print('\033[32mNúmero adicionado com sucesso.\033[m')

    rpt = str(input('Deseja continuar adicionando valores? [S/N] ')).strip().upper()
    while not rpt in 'SN':
        rpt = str(input('\033[31mInsira uma resposta válida. \033[m')).strip().upper()

    if rpt == 'N':
        break

print('-'*85)
print(f'Os números que você inseriu (em ordem crescente) são: {sorted(valores)}.')
