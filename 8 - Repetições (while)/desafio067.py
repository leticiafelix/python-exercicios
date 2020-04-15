#faça um programa que mostre a tabuada de varios numeros, um de cada vez, para cada valor digitado pelo usuario
#o programa sera interrompido quando o numero solicitado for negativo


while True:
    print('{:=^50}'.format(' TABUADA '))
    n = int(input('De qual número você deseja ver a tabuada? '))
    if n < 0:
        break

    for i in range(1,11):
        print(f'{n} x {i:2} = {(n*i):2}')


print('Programa TABUADA encerrado. Volte sempre!')
