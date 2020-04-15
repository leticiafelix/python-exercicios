#crie um programa que leia um numero inteiro e peça para o usuário escolher a base de conversão
#(1 para binario 2 para octal 3 para hexadecimal) e converta o valor

print('{:=^50}'.format(' CONVERSÃO DE BASES '))

n = int(input('Insira um número inteiro: '))
base = int(input('Escolha a base de conversão: \033[32m[1]\033[m para \033[32mbinária\033[m \033[36m[2]\033[m para \033[36moctal\033[m e \033[35m[3]\033[m para \033[35mhexadecimal\033[m: '))

if base == 1:
    binario = bin(n)[2:]
    print('O número {} na base binária é igual a {}.'.format(n,binario))
elif base == 3:
    hexadecimal = hex(n)[2:]
    print('O número {} na base hexadecimal é igual a {}.'.format(n,hexadecimal))
elif base == 2:
    octal = oct(n)[2:]
    print('O número {} na base octal é igual a {}.'.format(n,octal))
else:
    print('Opção inválida. Tente novamente.')
