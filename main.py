import os, sys, requests
os.system('clear')
url = 'https://httpbin.org/ip'
proxy = input('''#Proxy Changer | A simple script to hide your IP Adress| By: KinyCrimson#
# Website with free proxies: http://free-proxy.cz/en/
#Ex: 159.203.12.49:8888
IP/PORT: ''')
try:
		while True:
			response = requests.get(url, proxies={'http': proxy, 'https': proxy})
			print(response.json())
except:
	print('Check your internet connection or use another proxy');exit()
