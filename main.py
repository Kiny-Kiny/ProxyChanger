#---------------------------------------#
global R,B,C,G
R='\033[1;31m';
B='\033[1;34m';
C='\033[1;37m';
G='\033[1;32m';
Format="\033[0m";
Letra="\033[38;5;15m";
Fundo="\033[48;5;19m"
banner='''
 __  __     __     __   __     __  __    
/\ \/ /    /\ \   /\ "-.\ \   /\ \_\ \   
\ \  _"-.  \ \ \  \ \ \-.  \  \ \____ \  
 \ \_\ \_\  \ \_\  \ \_\\"\_\  \/\_____\ 
  \/_/\/_/   \/_/   \/_/ \/_/   \/_____/ \n
'''
#---------------------------------------#
from os import system
from sys import argv
from os import execl
from sys import executable
#---------------------------------------#
def clear():
	system('cls');system('clear')
#---------------------------------------#
try:
	from requests import get
except:
	system('pip install requests');print('_ ! _ Instalação do módulo requests foi concluída. Execute o script novamente. _ ! _');exit()
try:
	clear();time=int(input(f'''{B}{banner}_ ! _ {Fundo}{Letra}{C}Digite os segundos que deseja ficar conectado{Format} {B}>>>{C} '''))
except:
	print(f'{R}_ ! _{C} Caracteres inválidos. {R}_ ! _{C}');exit()
#---------------------------------------#
while(time > 0):
	try:
		from time import sleep
		r=get('http://pubproxy.com/api/proxy').json()
		proxy=r['data'][0]['ip']+':'+r['data'][0]['port']
		response=get('https://httpbin.org/ip', proxies={'http': proxy, 'https': proxy}).json()
		try:
			print(f'{G}Conectado a proxy: '+response['origin'])
		except:
			print(f'{R}Não foi possível se conectar a proxy: {proxy}')
		#print(response)
		sleep(1)
		time=time-1
	except:
		pass
#---------------------------------------#
op=input(f'{B}_ ! _{C} Deseja continuar?{B}_ ! _{C} \n{B}1{C} - Sim\n{B}2{C} - Não\n{B}>>>{C} ')
if op == '1': execl(executable, executable, *argv)
elif op == '2': system('cls');system('clear');exit()
else: print(f'{R}_ ! _{C} Opção inválida. {R}_ ! _{C}')
#---------------------------------------#
