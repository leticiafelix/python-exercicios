#refaça o desafio009 utilizando o laço for

n = int(input('Insira um número inteiro: '))
print(':::: Tabuada de {} ::::'.format(n))

for i in range(1,11):
    print('{} x {:2}  =  {}'.format(n,i,n*i))
