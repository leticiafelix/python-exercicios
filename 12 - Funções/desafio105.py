#faça um programa que tenha uma função chamada notas() que pode receber várias
#notas de alunos e vai retornar um dicionario com as seguintes informações
#quantidade de notas, maior nota, menor nota, média da turma, situação (opcional)(situação: boa, razoavel ou ruim)
#adicione tambem as docstrings da funcao

def notas(*n, sit = False):
    """
    -> Mostra um resumo das notas dos alunos.
    :param n: (aceita várias) Notas dos alunos.
    :param sit: (opcional) Se verdadeiro, mostra se as notas estão boas, regulares ou ruins.
    :return: Retorna um dicionário com informações sobre as notas.
    """
    from statistics import mean

    resumo = {'quantidade de notas': len(n), 'maior nota': max(n), 'menor nota': min(n),
              'média das notas': round(mean(n),2)}
    if sit:
        if mean(n) < 5:
            resumo['sit'] = 'ruim'
        elif mean(n) < 7:
            resumo['sit'] = 'regular'
        elif mean(n) > 7:
            resumo['sit'] = 'boa'

    return resumo


#programa principal
help(notas)
print(notas(3,2,4,6,2,1,4,6,3))
print(notas(5,1.6,9,10,6,2.5,4.5, sit = True))
print(notas(6,7.5,5,8, sit = True))
print(notas(9,8,10,9.7, sit = True))
