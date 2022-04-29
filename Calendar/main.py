import os
import requests
import smtplib
import mysql.connector
from datetime import date,datetime
from termcolor import colored
import sys
import threading
import src.functions as func

today = date.today()

daate = today.strftime("%d/%m/%Y")
aa = list(daate)
day = [aa[0],aa[1]]
day = ''.join(day)
month = [aa[3],aa[4]]
month = ''.join(month)
year = [aa[6],aa[7]]
year = ''.join(year)

def start():

	while True:
		print(colored("see_homework, add_homework, delete_homework, see_exam, add_exam, delete_exam, clear, send_email, exit", "red"))
		response = str(input("Command: "))

		if response == 'see_homework':
			a = input('Day: ')
			if str(a) == 'today':
				print(colored(func.see_homework(day,month,year),"blue"))
			else:
				b = int(input('Month: '))
				c = int(input('Year: '))
				print(colored(func.see_homework(a,b,c),"green"))
		elif response == 'add_homework':
			a = input('Day: ')
			if str(a) == 'today':
				d = str(input('Name: '))
				func.add_homework(d,day,month,year)
			else:
				b = int(input('Month: '))
				c = int(input('Year: '))
				d = str(input('Name: '))
				func.add_homework(d,a,b,c)
		elif response == 'delete_homework':
			a = input('Day: ')
			if str(a) == 'today':
				d = str(input('Name: '))
				func.delete_homework(d,day,month,year)
			else:
				b = int(input('Month: '))
				c = int(input('Year: '))
				d = str(input('Name: '))
				func.delete_homework(d,a,b,c)
		elif response == 'see_exam':
			a = input('Day: ')
			if str(a) == 'today':
				print(colored(func.see_exam(day,month,year),"blue"))
			else:
				b = int(input('Month: '))
				c = int(input('Year: '))
				print(colored(func.see_exam(a,b,c),'green'))
		elif response == 'add_exam':
			a = input('Day: ')
			if str(a) == 'today':
				d = str(input('Name: '))
				func.add_exam(d,day,month,year)
			else:
				b = int(input('Month: '))
				c = int(input('Year: '))
				d = str(input('Name: '))
				func.add_homework(d,a,b,c)
		elif response == 'delete_exam':
			a = input('Day: ')
			if str(a) == 'today':
				d = str(input('Name: '))
				func.delete_exam(d,day,month,year)
			else:
				b = int(input('Month: '))
				c = int(input('Year: '))
				d = str(input('Name: '))
				func.delete_exam(d,a,b,c)
		elif response == 'send_email':
			func.send_email()
		elif response == 'clear':
			func.screen_clear()

		elif response == 'exit':
			sys.exit(0)

def start2():

	sent = False

	while sent:
		if now[12] == '0':
			sent = False
			pass

	while not sent:

		now = datetime.now()
		now = now.strftime("%d/%m/%Y %H:%M:%S")
		now = list(now)
		
		if sent == False:
			if now[12] == '9':
				func.send_email()
				sent = True
				break
		elif sent == True:
			pass

		elif now[12] == '0':
			sent == False
		else:
			pass
	

#ACTIONS

proc1 = threading.Thread(target=start)
proc2 = threading.Thread(target=start2)
proc1.start()
proc2.start()
proc1.join()
proc2.join()
