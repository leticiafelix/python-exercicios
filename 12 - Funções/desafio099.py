#faça um programa que tenha uma função maior() que receba varios parametros
#analise todos eles e diga qts valores foram passados e qual é o maior

from time import sleep

def maior(*num):
    mai = 0
    print('-'*60)
    print('Analisando os valores passados...')
    sleep(2)
    print('-'*60)

    print('VALORES PASSADOS: ', end ='')
    for i, v in enumerate(num):
        print(v, end = ' ')
        if i == 0:
            mai = v
        elif v > mai:
            mai = v

    print(f'\nTOTAL DE VALORES: {len(num)}')
    print(f'MAIOR VALOR: {mai}')


#programa principal
maior()
maior(7,2,3,1)
maior(0,1,3,8,1,3)
maior(9,2,3,10)
maior(-1,-2,-3,-7)
