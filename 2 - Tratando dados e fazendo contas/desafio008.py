#leia uma distancia em metros e converta-a pras outras medidas

m = float(input('Insira uma distância em metros:'))
km = m/1000
hm = m/100
dam = m/10
dm = m*10
cm = m*100
mm = m*1000

print(""""{} metros corresponde a:
{}km
{}hm
{}dam
{}m
{}dm
{}cm
{}mm""".format(m,km,hm,dam,dm,m,cm,mm))
