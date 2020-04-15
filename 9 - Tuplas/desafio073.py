#crie uma tupla preenchida com os 20 primeiros colocados
#da tabela do campeonato brasileiro de futebol, na ordem de colocação
#depois mostre: apenas os 5 primeiros colocados, os ultimos 4 da tabela
#uma lista com os times em ordem alfabetica, em q posição está o chapecoense

colocados = ('Flamengo','Santos','Palmeiras','Grêmio','Atlético Paranaense','São Paulo','Internacional','Corinthians','Fortaleza','Goiás','Bahia','Vasco','Atlético Mineiro','Fluminense','Botafogo','Ceará','Cruzeiro','CSA','Chapecoense','Avaí')


print('-' * 50)
print('                   BRASILEIRÃO       ')
print('-' * 50)
print(f"""20 primeiros colocados: {colocados}
Os 5 primeiros colocados são: {colocados[:5]}
Os últimos 4 colocados são: {colocados[-4:]}
Os primeiros 20 colocados em ordem alfabética: {sorted(colocados)}
O Chapecoense está na {colocados.index('Chapecoense')+1}° posição.""")
