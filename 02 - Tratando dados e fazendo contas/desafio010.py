#leia um valor em reais e converta-o pra dolares e euros
#cotação do dolar = 4.07 reais
#cotação do euro = 4.55 reais

r = float(input('Insira um valor em real:'))
d = r/4.07
e = r/4.55

print('Com {} reais, você pode comprar {} dólares ou {} euros.'.format(r,d,e))
