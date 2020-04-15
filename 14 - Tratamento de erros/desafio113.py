#reescreva a funcao leia int do desafio 104, incluindo agora a
#possibilidade da digitação de um numero de tipo invalido
#aproveite e crie também uma função leiaFloat() com a mesma funcionalidade

def leiaint(txt = 'Digite um número inteiro: '):
    valido = False
    while not valido:
        try:
            n = int(input(txt))
        except (KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m')
        except:
            print('\033[31mEntrada Inválida\033[m')
        else:
            valido = True
            print(f'Você digitou o número {n}.')


def leiafloat(txt = 'Digite um número real: '):
    valido = False
    while not valido:
        try:
            n = float(input(txt))
        except:
            print('\033[31mEntrada Inválida\033[m')
        else:
            valido = True
            print(f'\033[32mVocê digitou o número {n}.\033[m')


#programa principal
leiaint()
leiafloat()