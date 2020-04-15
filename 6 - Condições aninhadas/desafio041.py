#crie um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade
#ate 9 - mirim, ate 14 - infantil, ate 19 - junior, ate 20 - sênior, acima - master

print('{:=^50}'.format(' CATEGORIA ATLETA '))

ano = int(input('Em que ano você nasceu? '))
mes = int(input('Em que mês você nasceu? (Responda de 1 a 12) '))


from datetime import datetime

ano_atual = datetime.now().year
mes_atual = datetime.now().month
dia_atual = datetime.now().day

if mes == mes_atual:
    dia = int(input('Em que dia você nasceu? '))
    if dia>dia_atual:
        idade = ano_atual - ano - 1
    else:
        idade = ano_atual - ano
elif mes > mes_atual:
    idade= ano_atual - ano - 1
else:
    idade = ano_atual - ano

if idade<=9:
    print('{} anos - Categoria Mirim.'.format(idade))
elif idade<=14:
    print('{} anos - Categoria Infantil.'.format(idade))
elif idade<=19:
    print('{} anos - Categoria Júnior.'.format(idade))
elif idade<=20:
    print('{} anos - Categoria Sênior.'.format(idade))
else:
    print('{} anos - Categoria Sênior.'.format(idade))
