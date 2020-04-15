#leia uma variável e a disseque

var = input('Digite algo:')
print("""Você digitou:{}
É caractere? {}.
É numérico? {}.
Possui caracteres ou números? {}.
É formado por espaços? {}.
Está em letras maiúsculas? {}.
Está em letras minúsculas? {}.
Está capitalizado? {}.""".format(var,var.isalpha(),var.isnumeric(),var.isalnum(),var.isspace(),var.isupper(),var.islower(),var.istitle()))
