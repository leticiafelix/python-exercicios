#o prof quer sortear a ordem de apresentação de trabalho de 4 alunos, faça um prog que leia o nome de 4 alunos
# e mostre a ordem sorteada

a1 = input('Insira o nome do aluno 1:')
a2 = input('Insira o nome do aluno 2:')
a3 = input('Insira o nome do aluno 3:')
a4 = input('Insira o nome do aluno 4:')

import random
ordem = random.sample((a1,a2,a3,a4),4)
print('A ordem de apresentação dos trabalhos é:{}'.format(ordem))
