def moeda(n):
    return f'R$:{n:>.2f}'.replace('.',',')

def aumentar(n, p, f = False):
    if f == True:
        return moeda(n * (1 + p/100))
    else:
        return n * (1 + p/100)

def diminuir(n, p, f = False):
    if f == True:
        return moeda(n * (p/100))
    else:
        return n * (p/100)


def dobro(n, f = False):
    if f == True:
        return moeda(2*n)
    else:
        return 2 * n


def metade(n, f = False):
    if f == True:
        return moeda(n/2)
    else:
        return n / 2


def resumo(n, m = "R$",pa = 0, pd = 0, f = False):
    print(f"""VALOR: {m}{moeda(n)}
METADE: {m}{metade(n, f)}
DOBRO: {m}{dobro(n,f)}
{pa}% DE AUMENTO: {m}{aumentar(n,pa,f)}
{pd}% DE REDUÇÃO: {m}{diminuir(n,pa,f)}""")