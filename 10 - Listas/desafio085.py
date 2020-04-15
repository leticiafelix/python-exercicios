#faça um programa onde o usuario possa digitar 7 valores numericos e cadastre numa lista única
#que mantenha separados os valores pares e ímpares. no final mostre os valores
#pares e ímpares em ordem crescente

valores = [[],[]]

for i in range(0,7):
    n = int(input('Insira um número inteiro: '))

    if n % 2 == 0:
        valores[0].append(n)
    else:
        valores[1].append(n)

valores[0].sort()
valores[1].sort()

print('-'*60)
print(f"""Valores Inseridos: {valores}
Pares: {valores[0]}
Ímpares: {valores[1]}""")
