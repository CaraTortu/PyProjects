import os
import requests
import smtplib
import mysql.connector
from datetime import date,datetime
from termcolor import colored
import sys
import threading

mydb = mysql.connector.connect(
  host="localhost",
  user="javier",
  password="",
  database="calendario"
)
db = mydb.cursor()

today = date.today()

daate = today.strftime("%d/%m/%Y")
aa = list(daate)
day = [aa[0],aa[1]]
day = ''.join(day)
month = [aa[3],aa[4]]
month = ''.join(month)
year = [aa[6],aa[7]]
year = ''.join(year)


# FUNCTIONS	

def add_homework(task,d,m,y):

	tabletocreate = str(str(d)+'-'+str(m)+'-'+str(y))
	tabletocreate = '`'+tabletocreate+'`'

	toexecute= """CREATE TABLE IF NOT EXISTS %s (homework VARCHAR(120),exams VARCHAR(120));""" % tabletocreate


	toexecute2 = """INSERT INTO %s (homework) VALUES (%s);""" % (tabletocreate, "'"+task+"'")

	db.execute(toexecute)
	db.execute(toexecute2)

	mydb.commit()

def see_homework(d,m,y):

	tabletocreate = str(str(d)+'-'+str(m)+'-'+str(y))
	tabletocreate = '`'+tabletocreate+'`'

	db.execute("SELECT homework FROM " + tabletocreate)

	result = db.fetchall()
	result = ' '.join(str(v) for v in result)
	result = result.replace('(','')
	result = result.replace(')','')
	result = result.replace("'",'')
	result = result.replace("none,",'')
	result = result.replace("None,",'')
	result = result.replace("none.",'')
	result = result.replace("None.",'')
	result = result.capitalize()
	last_char_index = result.rfind(",")
	result = result[:last_char_index] + "." + result[last_char_index+1:]
	return result

def delete_homework(name,d,m,y):
	tabletocreate = str(str(d)+'-'+str(m)+'-'+str(y))
	tabletocreate = '`'+tabletocreate+'`'
	name = str(name)

	toex = str("DELETE FROM "+tabletocreate+" "+ "WHERE homework = " + '"'+name+'"')

	db.execute(toex)

	mydb.commit()

	print(name+", is deleted.")

def add_exam(task,d,m,y):

	tabletocreate = str(str(d)+'-'+str(m)+'-'+str(y))
	tabletocreate = '`'+tabletocreate+'`'

	toexecute= """CREATE TABLE IF NOT EXISTS %s (homework VARCHAR(120),exams VARCHAR(120));""" % tabletocreate


	toexecute2 = """INSERT INTO %s (exams) VALUES (%s);""" % (tabletocreate, "'"+task+"'")

	db.execute(toexecute)
	db.execute(toexecute2)

	mydb.commit()

def see_exam(d,m,y):

	tabletocreate = str(str(d)+'-'+str(m)+'-'+str(y))
	tabletocreate = '`'+tabletocreate+'`'

	db.execute("SELECT exams FROM " + tabletocreate)

	result = db.fetchall()
	result = ' '.join(str(v) for v in result)
	result = result.replace('(','')
	result = result.replace(')','')
	result = result.replace("'",'')
	result = result.replace("none,",'')
	result = result.replace("None,",'')
	result = result.replace("none.",'')
	result = result.replace("None.",'')
	result = result.capitalize()
	last_char_index = result.rfind(",")
	result = result[:last_char_index] + "." + result[last_char_index+1:]
	return result

def delete_exam(name,d,m,y):
	tabletocreate = str(str(d)+'-'+str(m)+'-'+str(y))
	tabletocreate = '`'+tabletocreate+'`'
	name = str(name)

	toex = str("DELETE FROM "+tabletocreate+" "+ "WHERE exams = " + '"'+name+'"')

	db.execute(toex)

	mydb.commit()

	print(name+", is deleted.")

def send_email():

	gmail_user = 'calendario@20-21.com'
	sent_from = gmail_user
	to = 'javierdj@jadk.com'

	tabletocreate = str(str(int(day)+1) +'-'+str(month)+'-'+str(year))
	tabletocreate = '`'+tabletocreate+'`'
	tabletocreate2 = str(str(day) +'-'+str(month)+'-'+str(year))
	tabletocreate2 = '`'+tabletocreate2+'`'

	toexecute= """CREATE TABLE IF NOT EXISTS %s (homework VARCHAR(120),exams VARCHAR(120));""" % tabletocreate
	toexecute2= """CREATE TABLE IF NOT EXISTS %s (homework VARCHAR(120),exams VARCHAR(120));""" % tabletocreate2
	db.execute(toexecute)
	db.execute(toexecute2)
	mydb.commit()

	email_text = """From: Calendario
	Subject: For today

	Homework: %s

	Exams: %s

	Subject: For tomorrow

	Homework: %s

	Exams: %s
	""" % (see_homework(day,month,year),see_exam(day,month,year),see_homework(int(day)+1,month,year),see_exam(int(day)+1,month,year))


	server = smtplib.SMTP('localhost', 25)
	server.ehlo()
	server.sendmail(sent_from, to, email_text)
	print(colored('Email sent!', 'yellow'))
	server.close()

def screen_clear():
	_ = os.system('clear')
