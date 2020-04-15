#crie um programa que calcule a soma de todos os numeros impares que são múltiplos de 3 e que se encontram entre 1 e 500

print('{:=^50}'.format(' TERMOS DE UMA PA '))

cont = 0
soma = 0

for i in range(1,501):
    if i%2!=0 and i%3==0:
        soma += i
        cont += 1

print('A soma de todos os {} valores solicitados é igual a {}.'.format(cont,soma))

#solução mais compacta proposta no video: for i in range(1,501,2) sem a parte par do if
