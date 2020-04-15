#faça um programa que leia 5 valores numéricos e guarde numa lista
#no fim mostre o maior e o menor valor digitado e suas respectivas posições na lista

valores = []
max = 0
min = 0

for i in range(0,5):
    valores.append((int(input(f'Insira um valor para a posição {i}: '))))

    if i == 0:
        max = min = valores[i]
    else:
        if valores[i] > max:
            max = valores[i]
        if valores[i] < min:
            min = valores[i]

print('-'*50)
print(f'Você digitou os valores: {valores}')
print(f'O menor valor foi: {min}, nas posições:', end = ' ')

for pos, i in enumerate(valores):
    if i == min:
        print(pos, end = '... ')

print(f'\nO maior valor foi: {max}, nas posições:', end = ' ')

for pos, i in enumerate(valores):
    if i == max:
        print(pos, end = '... ')
