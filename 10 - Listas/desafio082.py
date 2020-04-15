#faça um programa que leia varios numeros e coloque numa lista
#depois disso crie duas listas extras, que conterão apenas os valores pares e os valores impares, respectivamente
#ao final mostre o conteúdo das três listas geradas

numeros = []

while True:
    numeros.append(int(input('Insira um número inteiro: ')))

    rpt = str(input('Deseja continuar a inserir números? [S/N] ')).strip().upper()
    while not rpt in 'NS':
        rpt = str(input('\033[31mInsira uma resposta válida.\033[m')).strip().upper()
    if rpt == 'N':
        break

pares = []
ímpares = []

for i in range(0,len(numeros)):
    if numeros[i] % 2 == 0:
        pares.append(numeros[i])
    else:
        ímpares.append(numeros[i])

print('-'*60)
print(f"""Você inseriu os números: {numeros}
Os pares são: {pares}
Os ímpares são: {ímpares}""")
