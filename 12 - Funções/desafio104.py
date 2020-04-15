#faça um programa que tenha a função leiaint() que vai funcionar de forma semelhante
#a função input() do python, só que fazendo a validação para aceitar apenas um valor numérico
# ex:  n = leiaint('Digite um n')

def leiaint(txt):
    """
    -> Verifica se a entrada do usuário é um número inteiro, caso contrário
    mostra uma mensagem de erro até que o usuário insira uma entrada válida.
    :param txt: Mensagem que será mostrada ao usuário ao solicitar o número.
    :return: Retorna o número inteiro.
    """
    n = str(input(txt)).strip()
    while not n.isnumeric():
        print('\033[31mEntrada inválida. \033[m')
        n = str(input(txt)).strip()
    n = int(n)
    return n


#programa principal
n = leiaint('Digite um número inteiro: ')
print(f'\033[32mVocê digitou o número {n}.\033[m')
