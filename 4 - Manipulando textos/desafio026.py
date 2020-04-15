#leia uma frase e diga quantas vezes aparece a letra a
#em que posição aparece pela primeira vez
#em que posição aparece pela ultima vez

print('{:=^50}'.format(' NÚMERO DE As '))

frase = str(input('Digite uma frase:')).strip()
cont = frase.lower().count('a')
prim = frase.lower().find('a')+1
ult = frase.lower().rfind('a')+1

print('Esta frase tem {} letras "a", a primeira aparece na posição {}, a última aparece na posição {}'.format(cont,prim,ult))
