#faça um programa que leia o nome de uma cidade e diga se começa ou não com "santo"

print('{:=^50}'.format(' CIDADES COM SANTO '))
cidade = str(input('Insira o nome da cidade: '))
cidade = cidade.split()[0]

print(cidade.upper().count('SANTO')!=0)
