#adapte o codigo do desafio 107, criando uma função adicional
#chamada moeda() que consiga mostrar os valores como um valor monetario formatado

import moeda

num = float(input('Digite um valor: '))
pcta = float(input('Escolha uma porcentagem de aumento: '))

pctd = float(input('Escolha uma porcentagem de redução: '))


dobro = moeda.dobro(num)
metade = moeda.metade(num)
diminuir = moeda.diminuir(num, pctd)
aumentar = moeda.aumentar(num, pcta)

print(f'O dobro de {moeda.moeda(num)} é {moeda.moeda(dobro)}.')
print(f'A metade de {moeda.moeda(num)} é {moeda.moeda(metade)}.')
print(f'{moeda.moeda(num)} com um aumento de {pcta}% é {moeda.moeda(aumentar)}.')
print(f'{moeda.moeda(num)} com uma redução de {pctd}% é {moeda.moeda(diminuir)}.')