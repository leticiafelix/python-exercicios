#crie um programa que mostre todos os numeros pares entre 1 e 50

print('Pares entre 1 e 50:')

for i in range(1,51):
    if i%2==0:
        print(i,end=' ')
print('\nAcabou')

#solução mais compacta: for i in range(2,51,2) sem o if
