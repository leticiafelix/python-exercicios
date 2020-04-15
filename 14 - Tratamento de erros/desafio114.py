#crie um código em python que teste se o site pudim esta acessivel pelo
#computador usado
import urllib.request

url = 'http://pudim.com.br'

try:
    status = urllib.request.urlopen(url).getcode()
except:
    print('\033[31mNão foi possível acessar o site. \033[m')
else:
    print('\033[32mO site está disponível.\033[m')