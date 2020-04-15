#faça um programa que leia 4 valores pelo teclado e guarde numa tupla
#no final mostre quantas vezes apareceu o 9, em q posição esta o primeiro 3 e quais foram os numeros pares

n = (int(input('Insira um número: ')), int(input('Insira um número: ')), int(input('Insira um número: ')), int(input('Insira um número: ')))

print(f"""Você digitou os valores: {n}
O número 9 apareceu {n.count(9)} vez(es).""")
if 3 in n:
    print(f'O primeiro 3 está na {n.index(3)+1}° posição.')
else:
    print('O número 3 não aparece.')

print('Os números pares são:', end = ' ')

for i in n:
    if i % 2 == 0:
        print(f'{i}', end = ' ')
