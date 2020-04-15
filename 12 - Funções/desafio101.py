#faça um programa que tenha uma função chamada voto() que vai receber
#como parametro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO
#OPCIONAL ou OBRIGATORIO nas eleições (mais de 65 voto opcional)

def voto(ano):
    """
    -> Função que analisa, pelo ano de nascimento, se a pessoa tem voto negado, opcional ou obrigatório.
    :param ano: ano em que a pessoa nasceu.
    :return: "NEGADO" se a pessoa tem menos de 16 anos
             "OPCIONAL" se a pessoa tem 16 ou 17 anos, ou se tem mais de 65 anos
             "OBRIGATÓRIO" se a pessoa tem entre 18 e 65 anos
    Função criada por Letícia Felix.
    """
    from datetime import datetime #ou import date e usar date.today().year

    atual = datetime.now().year
    idade = atual - ano
    if idade < 16:
        return f'{idade} anos: VOTO NEGADO'
    elif idade in range(16,18) or idade > 65:
        return f'{idade} anos: VOTO OPCIONAL'
    elif idade in range(18,66):
        return f'{idade} anos: VOTO OBRIGATÓRIO'


#PROGRAMA PRINCIPAL
print('-'*30)
ano = int(input('Em que ano você nasceu? '))

print('-'*30)
print(voto(ano))
print('-'*30)
