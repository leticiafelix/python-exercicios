#crie um programa que leia a idade e o sexo de varias pessoas
#a cada pessoa cadastrada o programa deve perguntar se o usuario quer continuar
#no final mostre:
#a) quantas pessoas tem mais de 18 anos, b) quantos homens foram cadastrados, c) quantas mulheres tem menos de 20 anos

dezoito = 0
homens = 0
mulher_20 = 0
cont = 0

while True:
    cont +=1
    print(':::: CADASTRO {} ::::'.format(cont))
    idade = float(input('Idade: '))
    while not idade in range(0,150):
        idade = float(input('\033[31mPor favor, insira uma idade válida.\033[m'))

    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('\033[31mPor favor, insira um sexo válido.\033[m')).strip().upper()

    print('\033[32mCadastro realizado com sucesso!\033[m')

    if idade > 18:
        dezoito += 1
    if sexo == 'M':
        homens += 1
    elif idade < 20:
        mulher_20 += 1

    rpt = str(input('Deseja continuar a cadastrar? [S/N] ')).strip().upper()

    while rpt != 'S' and rpt != 'N':
        rpt = str(input('\033[31mPor favor, insira uma resposta válida.\033[m')).strip().upper()

    if rpt == 'N':
        break

print('------------------------------------------------')
print(f"""Pessoas cadastradas: {cont}
Maiores de 18: {dezoito}
Homens: {homens}
Mulheres com menos de 20 anos: {mulher_20} """)
print('------------------------------------------------')
