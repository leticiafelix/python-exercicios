#leia uma temperatura em °C e retorne a mesma em Farenheit e Kelvin

c = float(input('Insira uma temperatura em °C:'))
f = c*(9/5)+32
k = c+273.15

print('{}°C corresponde a {}F e {}K'.format(c,f,k))
