#crie um programa que leia duas notas de um aluno, calcule a media e retorne o resultado
#media abaixo de 5 - reprovado
#media entre 5 e 6.9 - recuperação
#media 7 ou superior - aprovado

print('{:=^50}'.format(' RESULTADO AVALIAÇÃO '))

n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))
m = (n1+n2)/2

if m >= 7:
    print('\033[32mSua média foi {:.2f}. Parabéns! Você foi aprovado.\033[m'.format(m))
elif m<5:
    print('\033[31mSua média foi {:.2f}. Você foi reprovado.\033[m'.format(m))
else:
    print('\033[33mSua média foi {:.2f}. Você está de recuperação.\033[m'.format(m))
