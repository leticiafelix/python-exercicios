#faça um programa que tenha uma função chamada área() que receba as dimensões de um terreno retangular
#(largura e comprimento) e mostre a area do terreno

def area(l,c):
    a = l * c
    print(f'A área de um terreno {l:.2f}x{c:.2f} é de {a:.2f}m².')


#programa principal

print('-'*30)
print(f'{"CONTROLE DE TERRENOS":^30}')
print('-'*30)

a = float(input('Largura (m): '))
b = float(input('Altura (m): '))

area(a,b)
