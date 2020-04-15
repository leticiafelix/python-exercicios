#leia o nome de uma pessoa e diga se ela tem "silva" no nome

print('{:=^50}'.format(' NOMES COM SILVA '))

nome = str(input('Insira seu nome:'))
print(nome.upper().find('SILVA')!=-1)
