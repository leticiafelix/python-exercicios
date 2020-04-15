#faça um programa que abra e reproduza um audio de arquivo mp3

print('{:=^20}'.format("MP3 Player"))

import playsound
name = input('Digite o nome da música:')
print("Now Playing... {}".format(name))

playsound.playsound('{}.mp3'.format(name))
