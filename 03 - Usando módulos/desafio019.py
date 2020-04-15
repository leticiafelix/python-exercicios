#um prof quer sortear um de 4 alunos pra apagar o quadro, faça um programa q ajude ele lendo o nome de 4 alunos
# e sorteando os escolhidos

a1 = input('Insira o nome do aluno 1:')
a2 = input('Insira o nome do aluno 2:')
a3 = input('Insira o nome do aluno 3:')
a4 = input('Insira o nome do aluno 4:')

import random
sort = random.choice((a1,a2,a3,a4))
print('O(A) aluno(a) sorteado(a) foi: {}'.format(sort))
