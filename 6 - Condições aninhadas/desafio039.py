# crie um programa que leia o ano de nascimento de um jovem e informe
# se ele ainda vai se alistar ao serviço militar
# se é a hora de se alistar
# se já passou do tempo do alistamento
# também deve mostrar o tempo que falta ou que passou do prazo

print('{:=^50}'.format(' ALISTAMENTO '))

ano = int(input('Em que ano você nasceu? '))

from datetime import datetime

ano_atual = datetime.now().year

idade = atual - ano

if idade == 18:
    print('\033[32m Você deve se alistar esse ano!\033[m')
elif idade < 18:
    print('Ainda falta(m) {} ano(s) pra você se alistar.'.format(18-idade))
else:
    print('\033[31mVocê deveria ter se alistado há {} ano(s) atrás.\033[m'.format(idade-18))
