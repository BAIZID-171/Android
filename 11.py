import os
import time

php='php -S '
nahid=':'


def click():
	print("Waiting for Send a Notification 💎")
	time.sleep(10)
	print("Notification Sending Done ✅")
	print("Waiting for click 💎")
	time.sleep(15)
	print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
	print("Your Victim IP : "+str(ip))
	print("Access The Mobile")
	print("Permission List 👇")
	time.sleep(3)
	print("1/ File ✅ Permission")
	time.sleep(7)
	print("2/ Admin ✅ Permission")
	time.sleep(2)
	print("3/ System Notification ✅ Permission")
	time.sleep(1)
	print("4/ SMS ✅ Permission")
	print("5/ Camera ✅ Permission")
	time.sleep(2)
	print("6/ Voice ✅ Permission")
	print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
	stat = input("Press (1)")
	if stat in ['1']:
		os.system("ifconfig")
		time.sleep(2)
		pip = str(input('IP : '))
		code = str(input('CODE : '))
		os.system("cd && cd Android && cd BAIZID && "+php+str(pip+nahid+code))
	

def logo():
	os.system("clear")
	print("""
\033[0;96m╭━━╮╭━━━┳\033[1;92m━━┳\033[1;93m━━━━┳━━┳\033[1;91m━━━╮           
\033[0;96m┃╭╮┃┃╭━╮┣\033[1;92m┫┣┻\033[1;93m━━╮━┣┫┣┻\033[1;91m╮╭╮┃\033[1;92m
\033[0;96m┃╰╯╰┫┃╱┃┃\033[1;92m┃┃╱\033[1;93m╱╭╯╭╯┃┃╱\033[1;91m┃┃┃┃
\033[0;96m┃╭━╮┃╰━╯┃\033[1;92m┃┃╱\033[1;93m╭╯╭╯╱┃┃╱\033[1;91m┃┃┃┃
\033[0;96m┃╰━╯┃╭━╮┣\033[1;92m┫┣┳\033[1;93m╯━╰━┳┫┣┳\033[1;91m╯╰╯┃
\033[0;96m╰━━━┻╯╱╰┻\033[1;92m━━┻\033[1;93m━━━━┻━━┻\033[1;91m━━━╯\033[1;92m
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Tools    : MOBILE HACK                ┃
┃ Facebook : www.facebook.com/MrError171┃
┃ What'sapp: +88015**5**1*5             ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
""")

logo()
ip = input(str("Enter Victim IP : "))
print("Notification Catalogue Select 💎")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("""
\033[1;91m[\033[1;92m01\033[1;91m] \033[1;92mSexual
\033[1;91m[\033[1;92m02\033[1;91m] \033[1;92mNews
\033[1;91m[\033[1;92m03\033[1;91m] \033[1;92mHacking
\033[1;91m[\033[1;92m04\033[1;91m] \033[1;92mVirus
\033[1;91m[\033[1;92m05\033[1;91m] \033[1;92mApplication
\033[1;91m[\033[1;92m06\033[1;91m] \033[1;92mBkash
\033[1;91m[\033[1;92m07\033[1;91m] \033[1;92mWhatsApp
\033[1;91m[\033[1;92m08\033[1;91m] \033[1;92mWorld Cap
\033[1;91m[\033[1;92m09\033[1;91m] \033[1;92mFacebook
\033[1;91m[\033[1;92m10\033[1;91m] \033[1;92mimo
( More Options Coming soon 💎)
""")
noti = input(str("Choice : "))
if noti in ['01','1']:
	print("You Select Sexual Notification 💎")
	time.sleep(6)
	logo()
	click()

if noti in ['02','2']:
	print("You Select News Notification 💎")
	time.sleep(6)
	logo()
	click()

if noti in ['03','3']:
	print("You Select Hacking Notification 💎")
	time.sleep(6)
	logo()
	click()
	
if noti in ['04','4']:
	print("You Select Virus Notification 💎")
	time.sleep(6)
	logo()
	click()
	
if noti in ['05','5']:
	print("You Select Application Ads Notification 💎")
	time.sleep(6)
	logo()
	click()