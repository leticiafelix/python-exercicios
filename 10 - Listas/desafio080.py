#faça um programa onde o usuario possa digitar 5 valores numericos e cadastre-os
#em uma lista, ja na posição correta de ordem crescente (sem usar o sort())
#no final mostre a lista ordenada na tela. enquanto vai adicionando vai falando a posição que adicionou o valor na lista

valores = []

for i in range(1,6):
    n = int(input(f'Insira o {i}° número: '))

    if i == 1:
        valores.append(n)
        print('\033[32mNúmero adicionado na 1° posição.\033[m')
    else:
        if n > max(valores):
            valores.append(n)
            print(f'\033[32mNúmero adicionado na {len(valores)}° (última) posição.\033[m')
        else:
            for j in range(0,len(valores)):
                if n <= valores[j]:
                    valores.insert(j,n)
                    print(f'\033[32mNúmero adicionado na {j+1}° posição.\033[m')
                    break

print('-'*70)
print(f'Os números que você inseriu (em ordem crescente): {valores}')
