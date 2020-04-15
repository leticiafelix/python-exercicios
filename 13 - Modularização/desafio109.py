#modifique as funcoes que foram criadas no desafio 107 para que elas aceitem
#um parametro a mais informando se o valor retornado por elas vai ser
#ou nao formatado pela funcao moeda() do desafio 108

import moeda

num = float(input('Digite um valor: '))
pcta = float(input('Escolha uma porcentagem de aumento: '))

pctd = float(input('Escolha uma porcentagem de redução: '))


dobro = moeda.dobro(num, f = True)
metade = moeda.metade(num, f = True)
diminuir = moeda.diminuir(num, pctd, f = True)
aumentar = moeda.aumentar(num, pcta, f = False)

print(f'O dobro de {num} é {dobro}.')
print(f'A metade de {num} é {metade}.')
print(f'{num} com um aumento de {pcta}% é {aumentar}.')
print(f'{num} com uma redução de {pctd}% é {diminuir}.')