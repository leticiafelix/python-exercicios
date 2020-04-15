import moeda

num = float(input('Digite um valor: '))
pcta = float(input('Escolha uma porcentagem de aumento: '))

pctd = float(input('Escolha uma porcentagem de redução: '))


dobro = moeda.dobro(num)
metade = moeda.metade(num)
diminuir = moeda.diminuir(num, pctd)
aumentar = moeda.aumentar(num, pcta)

print(f'O dobro de {num} é {dobro:.2f}.')
print(f'A metade de {num} é {metade:.2f}.')
print(f'{num} com um aumento de {pcta}% é {aumentar:.2f}.')
print(f'{num} com uma redução de {pctd}% é {diminuir:.2f}.')