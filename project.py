from uuid import getnode
from pathlib import Path
from getpass import getuser
from os import name , system
from requests import get , ConnectionError
from hashlib import md5

def clear_screen():
	if name == 'nt':
		system('cls')
	else:
		system('clear')

if name == 'nt':
	home = (str(Path.home()))
else:
	home = (str(Path.home()))+'/'

text = 'SYS113'
open(home + 'license', 'a').close()
code = md5((hex(getnode()) + text).encode('utf-8')).hexdigest()
license = md5(code.encode('utf-8')).hexdigest()

# PROJECT SOURCE CODE ...

def main():
	print('hello world!')
	input('')
try:
	get('https://www.google.com/')
	if open(home + 'license','r').read() == license:
		main()
	else:
		print('\n\t\t' + ' --- CODED BY SYS113 --- ' + '\n')
		print("\t" + "Code : %s"%code)
		print("\n\t\tuser : "+getuser())
		password = input("\n\t\tpass : ")
		if password == license:
				file = open(home + 'license','w')
				file.write(password)
				file.close()
				clear_screen()
				main()
		else:
				clear_screen()
				print('error , worng password ...')
		input('')
except ConnectionError:
	print('error , connect to network ...')
	input('')
