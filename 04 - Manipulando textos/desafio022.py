#faça um programa que leia o nome completo de uma pessoa e mostre:
#o nome com todas as letras maiusculas
#o nome com todas as letras minusculas
#quantas letras tem (sem considerar os espaços)
#quantas letras tem o primeiro nome

nome = str(input('Insira seu nome completo:'))
nome = nome.strip()
mai = nome.upper()
min = nome.lower()
letras = nome.split()
n = len(letras)
letras = len(nome)-(n-1) #subtraindo o número de espaços
prim = len(nome.split()[0])

print("""Nome: {}
Em maiúsculo: {}
Em minúsculo: {}
Quantidade de letras: {}
Quantidade de letras do primeiro nome: {}""".format(nome,mai,min,letras,prim))
