def moeda(n):
    return f'R$:{n:.2f}'

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
