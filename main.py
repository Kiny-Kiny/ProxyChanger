from threading import Thread;
from random import choice;
from subprocess import call;
from sys import executable;
from time import sleep;
from os import name;

ip_local=['192.168.0.1',  '192.168.0.2', '192.168.0.3','192.168.0.10'];

with open('proxies.txt','r') as f:
	proxies=str(f.read())
	proxies=proxies.split('\n')

call([executable,'-m','pip','install','requests']);
from requests import get;

global R,B,C,G

# Vermelho = Red | Azul = Blue | Branco = White | Verde = Green
Vermelho='\033[1;31m';Azul='\033[1;34m';Branco='\033[1;37m';Verde='\033[1;32m';

call([{'nt':'cls','posix':'clear'}[name]])

print('''%s  __  __     __     __   __     __  __    
 /\ \/ /    /\ \   /\ "-.\ \   /\ \_\ \   
 \ \  _"-.  \ \ \  \ \ \-.  \  \ \____ \  
  \ \_\ \_\  \ \_\  \ \_\\"\_\   \/\_____\ 
   \/_/\/_/   \/_/   \/_/ \/_/   \/_____/ \n%s'''%(Azul,Branco))


def main(proxy):
    network_type = input('Are you using a wireless or wired network??\n1. Wireless\n2. Wired\nChoice: ')

    if network_type == '1':
        call(['ifconfig', 'wlan0', 'down'])
        call(['ifconfig', 'wlan0', choice(ip_local), 'up'])
    elif network_type == '2':
        call(['ifconfig', 'eth0', 'down'])
        call(['ifconfig', 'eth0', choice(ip_local), 'up'])
    else:
        print('Invalid selection.')

    try:
        print('[ %s!%s ] Connected To %s%s%s.' % (Verde, Branco, Verde, get('https://httpbin.org/ip', proxies={'http://': proxy, 'https://': proxy}).json()['origin'], Branco))
    except Exception:
        print('[ %sX%s ] Not Connected To %s%s%s.' % (Vermelho, Branco, Vermelho, proxy, Branco))

if __name__ == '__main__':
	while True:
		for ip in proxies: Thread(target=main(ip)).start();sleep(0.7)
