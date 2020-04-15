#crie um programa que leia o sexo de uma pessoa mas só aceite M ou F
#caso esteja errado peça a digitação novamente até obter um sexo valido

print('{:=^50}'.format(' LEITOR DE SEXO '))

sexo = str(input('Insira seu sexo [M/F]: ')).upper().strip()

while sexo != 'M' and sexo != 'F':
    sexo = str(input('\033[31mPor favor, insira um sexo válido. \033[m')).upper().strip()

print('\033[32mSexo [{}] registrado com sucesso. \033[m'.format(sexo))
