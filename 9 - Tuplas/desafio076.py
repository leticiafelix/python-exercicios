#faça um programa que tenha uma tupla unica com nomes de produtos e seus preços na sequencia
#no final mostre uma listagem de preços organizando os dados de forma tabular

print('-'*50)
print(f'{"LISTAGEM DE PREÇOS":^50}')
print('-'*50)

produtos = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro',34.9)

for i, pos in enumerate(produtos):
    if i % 2 == 0:
        print("""{:.<40}""".format(produtos[i]), end = '')
    else:
        print('R$ {:7.2f}'.format(produtos[i]))
print('-'*50)
