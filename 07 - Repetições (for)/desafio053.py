#crie um programa que leia uma frase qualquer e diga se ela é um palíndromo (desconsiderando os espaços)
#palindromo = se ler de frente pra tras e de tras pra frente fica igual
#ex: apos a sopa, a sacada da casa, a torre da derrota, o lobo ama o bolo, anotaram a data da maratona

print('{:=^50}'.format(' PALÍNDROMOS '))

frase = str(input('Insira uma frase: ')).strip().lower()

inverso = ''

for i in range(len(frase)-1,-1,-1):
    if frase[i] != ' ':
        inverso += frase[i]

palindromo = inverso == frase

print('A frase é um palíndromo.' if palindromo == True else 'A frase não é um palíndromo.')


#solução do video
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
#ou inverso = inverso[::-1]

for letra in range(len(junto)-1,-1,-1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palíndromo! O inverso de {} é {}.'.format(frase,inverso))
else:
    print('Não temos um palíndromo. O inverso de {} é {}.'.format(frase,inverso))
