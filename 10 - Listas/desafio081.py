#faça um programa que leia varios numeros e coloque numa lista, depois mostre
#quantos numeros foram digitados, a lista ordenada de forma decrescente
#se o valor 5 foi digitado e está ou não na lista

valores = []

while True:
    valores.append(int(input('Insira um número: ')))

    rpt = str(input('Deseja continuar a inserir números? [S/N] ')).strip().upper()

    while not rpt in 'NS':
        rpt = str(input('\033[31mInsira uma resposta válida.\033[m')).strip().upper()
    if rpt == 'N':
        break

valores.sort(reverse = True)

print('-'*60)
print(f"""Você inseriu {len(valores)} números.
Seus números em ordem decrescente: {valores}""")

if 5 in valores:
    print('O número 5 está na lista!')
else:
    print('O número 5 não está na lista!')
