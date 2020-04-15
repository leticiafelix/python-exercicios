#faça um programa onde o usuario digite uma expressão qualquer que use parênteses.
#seu prog deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta

expressao = str(input('Insira uma expressão matemática: '))
pilha = []

for i in expressao:
    if i == '(':
        pilha.append('(')
    elif i == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) > 0:
    print('\033[31mSua expressão está errada.\033[m')
else:
    print('\033[32mSua expressão está correta.\033[m')
