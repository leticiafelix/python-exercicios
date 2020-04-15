#leia uma altura e largura e retorne quantos litros de tinta são necessarios pra pintar a parede
#dado que cada litro de tinta pinta 2m²

larg = float(input('Insira a largura da parede:'))
alt = float(input('Insira a altura da parede:'))
area = larg*alt

print('A área da parede é de {}m², para pintá-la será necessário comprar {}l de tinta.'.format(area,area/2))
