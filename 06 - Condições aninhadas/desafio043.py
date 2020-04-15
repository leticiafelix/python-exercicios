#crie um programa que leia o peso e a altura de uma pessoa e calcule seu IMC
#mostre seu status de acordo com a tabela abaixo
#abaixo de 18.5 - abaixo do peso
#entre 18.5 e 25 - peso ideal
#25 até 30 - sobrepeso
#30 até 40 - obesidade
#acima de 40 - obesidade mórbida

print('{:=^50}'.format(' IMC '))

peso = float(input('Qual é o seu peso? '))
alt = float(input('Qual a sua altura? '))
imc = peso/alt**2

if imc<18.5:
    print('\033[31mVocê está abaixo do peso ideal.\033[m')
elif imc<25:
    print('\033[32mVocê está no peso ideal.\033[m')
elif imc<30:
    print('\033[31mVocê está com sobrepeso.\033[m')
elif imc<40:
    print('\033[31mVocê está com obesidade.\033[m')
else:
    print('\033[31mVocê está com obesidade mórbida.\033[m')
