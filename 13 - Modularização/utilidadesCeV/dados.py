def leiadinheiro():
    valido = False
    while not valido:
        n = str(input('Digite um valor: R$:')).strip().replace(',','.')
        if n.isalpha() or n == '':
            print('\033[31mEntrada Inválida.\033[m')
        else:
            valido = True
            return float(n)



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