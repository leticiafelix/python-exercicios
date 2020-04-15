#le um numero real e mostra na tela sua porção inteira
import math
print('{:=^50}'.format('Porção Inteira'))
num = float(input('Digite um número real:'))
print('A porção inteira de {} é {}'.format(num,math.trunc(num)))

#le o comprimento do cat op e do cat adj de um triangulo retangulo e calcule a hip
print('{:#^50}'.format('Hipotenusa'))
catop = float(input('Insira o comprimento do cateto oposto:'))
catadj = float(input('Insira o comprimento do cateto adjacente:'))
hip = math.sqrt(catop**2 + catadj**2)
print('A hipotenusa de um triângulo retângulo com cateto oposto de {}cm e cateto adjacente {}cm é igual a {}cm'.format(catop,catadj,hip))

#le um angulo e mostre o sen cos e tg
ang = float(input('Insira um ângulo:'))
sen = math.sin(ang)
cos = math.cos(ang)
print('O seno do ângulo {}° é igual a {} e o cosseno é igual a {}'.format(ang,sen,cos))

#um prof quer sortear um de 4 alunos pra apagar o quadro, faça um programa q ajude ele lendo o nome de 4 alunos e sorteando os escolhidos
print('{:~^50}'.format('Sorteio Para Apagar o Quadro'))
a1 = input('Insira o nome do aluno 1:')
a2 = input('Insira o nome do aluno 2:')
a3 = input('Insira o nome do aluno 3:')
a4 = input('Insira o nome do aluno 4:')

import random
sort = random.choice((a1,a2,a3,a4))
print('O(A) aluno(a) sorteado(a) foi: {}'.format(sort))

#o prof quer sortear a ordem de apresentação de trabalho de 4 alunos, faça um prog que leia o nome de 4 alunos e mostre a ordem sorteada
print('{:#^50}'.format('Ordem de apresentação do trabalho'))
a1 = input('Insira o nome do aluno 1:')
a2 = input('Insira o nome do aluno 2:')
a3 = input('Insira o nome do aluno 3:')
a4 = input('Insira o nome do aluno 4:')
ordem = random.sample((a1,a2,a3,a4),4)
print('A ordem de apresentação dos trabalhos é:{}'.format(ordem))

#prog q abra e reproduza um audio de arquivo mp3
print('{:=^20}'.format("MP3 Player"))

