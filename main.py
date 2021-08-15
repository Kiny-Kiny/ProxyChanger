from os import system
banner='''
 __  __     __     __   __     __  __    
/\ \/ /    /\ \   /\ "-.\ \   /\ \_\ \   
\ \  _"-.  \ \ \  \ \ \-.  \  \ \____ \  
 \ \_\ \_\  \ \_\  \ \_\\"\_\  \/\_____\ 
  \/_/\/_/   \/_/   \/_/ \/_/   \/_____/ \n
'''
try:
	from requests import get
except:
	system('pip install requests');print('_ ! _ Instalação do módulo requests foi concluída. Execute o script novamente. _ ! _');exit()
try:
	time=int(input(f'''{banner}_ ! _ Digite os segundos que deseja ficar conectado >>> '''))
except:
	print('_ ! _ Caracteres inválidos. _ ! _');exit()
while(time > 0):
	try:
		from time import sleep
		r=get('http://pubproxy.com/api/proxy').json()
		proxy=r['data'][0]['ip']+':'+r['data'][0]['port']
		response=get('https://httpbin.org/ip', proxies={'https': proxy, 'http': proxy})
		print(response.json())
		#print(response)
		sleep(1)
		time=time-1
	except:
		None
op=input('Deseja continuar? \n1 - Sim\n2 - Não\n>>> ')
if op == '1': from sys import argv; from sys import execl; from sys import executable;execl(executable, executable, *argv)
elif op == '2': system('cls');system('clear');exit()
else: print('_ ! _ Opção inválida. _ ! _')
