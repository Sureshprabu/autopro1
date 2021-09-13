
import sys
import os


import sys

import pyautogui as p
import time
import nltk
nltk.download('punkt')
from nltk import word_tokenize 



p.alert("Open browser ticket page")
time.sleep(1)
p.scroll(800)
time.sleep(1)
p.scroll(800)
p.alert("move me to issue Description")
time.sleep(1)
issue = p.position()
p.click(issue)
def test():
	
	global ask
	ask = p.prompt(text = "Amount of work in progress tickets ?", title= "Confirm")
	ask = int(ask)
	global d
	d = 0
	
	
	p.click(issue)
	for i in range(ask):
		time.sleep(0.5)
		a = (i*2)+1
		p.click(issue)
		time.sleep(1)
		p.click(issue)
		p.hotkey('ctrl','f')
		p.typewrite('No. Of T',interval=0.01)
		p.hotkey('enter')
		time.sleep(0.2)
		p.hotkey('esc')
		time.sleep(0.5)
		if (d == True):
			a = a-2

		for j in range(a):
			p.hotkey('tab')
		time.sleep(1)
		p.hotkey('enter')
		p.click(issue)
		time.sleep(6)
		p.click(issue)
		p.scroll(1000)
		for g in range(5):
			p.scroll(1000)
			p.scroll(1000)
		p.scroll(1000)
		p.scroll(1000)
		time.sleep(0.3)
		p.click(issue)
		for g in range(5):
			p.scroll(1000)
			p.scroll(1000)
		p.scroll(1000)
		p.click(issue)
		for g in range(5):
			p.scroll(1000)
			p.scroll(1000)
		p.scroll(1000)
		p.doubleClick(issue)
		p.doubleClick(issue)
		p.hotkey('ctrl','c')
		time.sleep(1)
		p.hotkey('win')
		time.sleep(1)
		p.typewrite('notepad',interval=0.001)
		
		p.hotkey('enter')
		time.sleep(1)
		p.hotkey('ctrl','v')
			
		p.hotkey('ctrl','s')
		p.typewrite('a')
		p.hotkey('enter')
		time.sleep(1)
		p.hotkey('left')
		p.hotkey('enter')
		time.sleep(1)
		p.hotkey('alt','f4')
		
			
		tokens = open('a.txt','r')
		tokens = tokens.read()
		tokens = tokens.lower()
		tokens = word_tokenize(tokens)
		lent = len(tokens)
		#p.alert(tokens)

	
		
		
		def act():
			
			time.sleep(0.5)
			p.hotkey('ctrl','f')
			p.typewrite('No. Of T')
			time.sleep(0.2)
			p.hotkey('esc')
			time.sleep(0.5)
			a = (i*2)+2
			for j in range(a):
				p.hotkey('tab')
			
			p.hotkey('space')
			time.sleep(1)
		

		def act1():
			p.hotkey('ctrl','f')
			time.sleep(1)
			p.typewrite("Catalog Details",interval=0.001)
		
			p.hotkey('esc')
			time.sleep(1)
			p.hotkey('enter')
			p.hotkey('tab')
			time.sleep(1)
			p.hotkey('enter')
			time.sleep(3)
			p.hotkey('tab')
			p.hotkey('tab')
			time.sleep(2)
			p.typewrite('email')
			time.sleep(3)
			p.hotkey('tab')
			p.typewrite('out')
			time.sleep(3)
			p.hotkey('tab')
			p.typewrite('out')
			time.sleep(3)
			p.hotkey('ctrl','f')
			time.sleep(0.5)
			p.typewrite('Update Ticket',interval=0.001)
			time.sleep(1)
			p.hotkey('esc')
			time.sleep(1)
			p.hotkey('enter')
			time.sleep(2)
			p.hotkey('ctrl','f')
			p.typewrite('Comments*',interval=0.01)
			p.hotkey('esc')
			time.sleep(1)
			p.hotkey('enter')
			p.hotkey('tab')
			time.sleep(1)
			p.hotkey('ctrl','a')
			p.typewrite("Dear team,\n"
					"Mail issue please check\n")
			time.sleep(2)
			p.hotkey('tab')
			time.sleep(1)
			p.typewrite('l1')
			time.sleep(0.5)
			p.hotkey('tab')
			time.sleep(1)
			p.typewrite('po')
			time.sleep(0.5)
			p.hotkey('tab')
			time.sleep(1)
			p.hotkey('enter')
			time.sleep(6)
	
			
		#MAIL

		if("mail" in tokens):
			act1()
			d = True
			continue
		if("email" in tokens):
			act1()
			d = True
			continue

		#OUTLOOK
		
		if("outlook" in tokens):
			act1()
			d = True
			continue


		#LOTUS NOTES

		if("lotus notes" in tokens):
			act1()
			d = True
			continue
		if("lotus" in tokens):
			act1()
			d = True
			continue
		if("notes" in tokens):
			act1()
			d = True
			continue
		if("archive" in tokens):
			act1()
			d = True
			continue
		if("office" in tokens):
			act1()
			d = True
			continue
		
		
		#O365
		
		if("office365" in tokens):
			act1()
			d = True
			continue
		if("o365" in tokens):
			act1()
			d = True
			continue
		

		#EXCHANGE MAIL
		
		if("exchange" in tokens):
			act1()
			d = True
			continue
		
		#MIGRATION
		if("migration" in tokens):
			act1()
			d = True
			continue
	

		#WEBMAIL
		
		if("webmail" in tokens):
			act1()
			d = True
			continue
		if("myapp" in tokens):
			act1()
			d = True
			continue
		if("ibm" in tokens):
			act1()
			d = True
			continue
		if("group" in tokens):
			act1()
			d = True
			continue
		
				
		#PASSWORD

		if("pwd" in tokens):
			act1()
			d = True
			continue
		
		if("password" in tokens):
			act1()
			d = True
			continue
	
		if("reset" in tokens):
			act1()
			d = True
			continue
		if("locked" in tokens):
			act1()
			d = True
			continue
		
		if("password" in tokens):
			act1()
			d = True
			continue
		
		else:
			
			continue
	
test()

pn = p.confirm(text = "Do you need to pend ticket ?", buttons = ["Yes","No"])
if (pn == "Yes"):
	time.sleep(1)
	p.hotkey('ctrl','f')
	p.typewrite(', item')
	p.hotkey('esc')
	p.hotkey('enter')
	time.sleep(0.5)
	for i in range(4):
		p.hotkey('tab')
	time.sleep(0.5)
	p.typewrite('All')
	


	def action():
		p.alert("Please select all tickets then click action pending")
		time.sleep(10)
	action()

	def action1():
		p.alert("Please select all tickets then click action pending")
		time.sleep(5)
	
	for i in range(5):
		ask1 = p.confirm(text = "Is Pending page loaded ?", buttons =['Yes','No'])

		if (ask1 == "No"):
			action1()	
		if (ask1 == "Yes"):
			break	
		
	
	
	def pend():
				
				time.sleep(1)
				p.hotkey('ctrl','f')
				time.sleep(1)
				p.typewrite('s : *')
				p.hotkey('enter')
				p.hotkey('esc')
				time.sleep(0.01)
				p.hotkey('enter')
				p.hotkey('tab')
				time.sleep(1)
				p.typewrite('req')
				time.sleep(1)	
				p.hotkey('tab')
				time.sleep(1)
				p.hotkey('right')			
				p.hotkey('right')
				p.hotkey('right')
				p.hotkey('right')
				p.hotkey('right')
				p.hotkey('right')
				p.hotkey('right')
				p.hotkey('enter')
				p.hotkey('right')
				p.hotkey('right')
				p.hotkey('right')
				time.sleep(1)
				p.hotkey('right')			
				p.hotkey('right')
				p.hotkey('right')
				p.hotkey('right')
				p.hotkey('right')
				p.hotkey('right')
				p.hotkey('right')			
				p.hotkey('right')
				p.hotkey('right')
				p.hotkey('right')
				p.hotkey('right')
				p.hotkey('right')
				p.hotkey('left')
				p.hotkey('enter')
				time.sleep(1)
				p.hotkey('right')			
				p.hotkey('right')
				p.hotkey('right')
				p.hotkey('right')
				p.hotkey('right')
				p.hotkey('right')
				p.hotkey('right')			
				p.hotkey('right')
				p.hotkey('right')
				p.hotkey('right')
				p.hotkey('right')
				p.hotkey('right')
				p.hotkey('left')
				p.hotkey('enter')
				time.sleep(1)

				p.hotkey('tab')
				time.sleep(1)
				p.typewrite("Your ticket has been acknowledged and we will get back to you Shortly.\n"
 						"|Ultimatix.HelpDesk@tcs.com \n"
						"| https://tcs2.webex.com/ For any queries Toll Free(INDIA) \n"
						": 1-800-267- 6563 Toll Free(US/CANADA) : 1-877-TCS-INDY VOIP : 500555\n",interval=0.01)
				time.sleep(1)
				p.hotkey('tab')
				time.sleep(1)
				p.hotkey('enter')
				time.sleep(7.5)
			
			
				p.click()
				
				time.sleep(0.5)
				p.scroll(2000)
				time.sleep(1)
				p.scroll(2000)
	
	
	pend()

	ask1 = p.confirm(text = "Is Pending page loaded ?", buttons =['Yes','No'])
			
	if (ask1 == "No"):
		time.sleep(4)
			



	
	ask = p.confirm(text = "Please confirm", buttons = ["Run again","Exit"])
		
	
	if(ask == "Run again"):
		test()


if (pn == "No"):
	



	ask = p.confirm(text = "Please confirm", buttons = ["Run again","Exit"])

	if(ask == "Run again"):
		test()
			



















