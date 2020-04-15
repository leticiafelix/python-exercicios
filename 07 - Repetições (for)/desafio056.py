#crie um programa que leia nome idade e sexo de 4 pessoas e mostre
#a média de idade do grupo, nome do homem mais velho, quantas mulheres tem menos de 20 anos

print('{:=^50}'.format(' LEITOR DE DADOS '))

somaidade = 0
maxm = 0
nomem = ''
contf = 0

for i in range(1,5):
    print('Pessoa {}:'.format(i))
    nome = str(input('Nome:')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M para masculino, F para feminino): ')).strip().upper()

    somaidade = somaidade + idade

    if sexo == 'M':
        if i==1:
            maxm = idade
            nomem = nome
        else:
            if idade > maxm:
                maxm = idade
                nomem = nome
    elif sexo == 'F':
        if idade < 20:
            contf += 1

media = somaidade/4

print("""A média das idades é: {}.
O homem mais velho é o {}, que tem {} anos.
Há {} mulheres com menos de 20 anos.""".format(media,nomem,maxm,contf))
