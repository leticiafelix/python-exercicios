#faça um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de 0 a 20
#le um numero entre 0 e 20 (verifica se foi inserido certo) e mostre-o por extenso

cont = ('zero','um','dois','três','quatro','cinco',
        'seis','sete','oito','nove','dez','onze',
        'doze','treze','quatorze','quinze','dezesseis',
        'dezessete','dezoito','dezenove','vinte')

while True:
    while True:
        n = int(input('Insira um número entre 0 e 20: '))
        if n in range(0,21):
            break
        print('\033[31mNúmero inválido.\033[m')

    print(f'Você digitou o número {cont[n]}.')

    rpt = str(input('Deseja continuar? [S/N] ')).strip().upper()
    while not rpt in 'SN':
        rpt = str(input('\033[31mInsira uma resposta válida.\033[m')).strip().upper()

    if rpt == 'N':
        print('Programa encerrado. Volte sempre!')
        break
