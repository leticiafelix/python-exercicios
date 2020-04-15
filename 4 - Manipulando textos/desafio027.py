#leia o nome completo de uma pessoa, em seguida mostre
#o primeiro e o ultimo nome separadamente

print('{:=^50}'.format(' PRIMEIRO E ÚLTIMO NOME '))

nome = str(input('Insira seu nome:')).strip
prim = nome.split()[0]
ult = nome.split()[len(nome.split())-1]

print('Seu primeiro nome é {}, seu último nome é {}'.format(prim,ult))
