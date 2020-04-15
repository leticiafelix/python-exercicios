#crie um pequeno sistema modularizado que permita cadastrar pessoas
#pelo seu nome e idade em um arquivo de texto simples
#o sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas
#as pessoas cadastradas

import funcs115

while True:
    select = funcs115.menu(['CADASTRAR', 'CADASTRO ATUAL', 'ECERRAR PROGRAMA'])

    if select == 2:
        break

    funcs115.cadastroexiste()
    if select == 0:
        funcs115.cadastrar()
    elif select == 1:
        funcs115.vercadastro()

print('Programa encerrado, volte sempre! :)')
#elif select == 1:
#    funcs115.vercadastro()