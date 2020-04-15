#faça um programa que leia varios numeros inteiros pelo teclado
#no fim mostre a media entre todos os valores
#mostre o maior e menor
#o programa pergunta ao usuario se ele quer continuar ou nao a digitar valores

print('{:=^50}'.format(' MEDIA, MAIOR E MENOR '))

soma = 0
cont = 0

while True:
    cont += 1
    n = int(input('Insira um número: '))
    soma += n
    media = soma/cont

    if cont == 1:
        max = n
        min = n
    else:
        if n > max:
            max = n
        if n < min:
            min = n

    v = str(input('Deseja continuar a digitar valores? [S/N] ')).upper()
    while v != 'S' and v != 'N':
        v = str(input('\033[31mInsira uma resposta válida.\033[m')).upper()

    if v =='N':
        break

print("""MÉDIA: {:.2f}
MAIOR: {:.2f}
MENOR: {:.2f}""".format(media,max,min))
