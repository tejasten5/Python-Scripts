# -*- coding: utf-8 -*-
li=[

"are","can","could","what","where",
"when","which","who","whom","whose",
"why","would","will","were","whether",
"was","do","does","did","dosen't",
"does","dosent","have","has","had",
"how","should","shall","may","if",
"isn't","isnt","is","any","whatsoever",
"aren't","arent","haven't","havent","wouldn't",
"wouldnt","whose","in","at","to",
"from","on","under","over","didn't",
"didnt","whatever","whoever","whomever","whichever",
"whenever","wherever","however","your","her",
"his","am","what's","how's","i've",
"i","we","they","he","she",
"be","i'm","won’t","list","enlist",
"any","suggest","tell","give","gave",
"m'i",""

]

# Check the end of string for ?
def checkend(question):
	if question.endswith('?') is True:
		return True
	else:
		return False

#check the list
def checklist(question):
	c=question.split(" ")[0]
	c=c.lower()
	if c in li:
		return True
	else:
		return False

#For checking we've/i'm types shortcut
def shortcut(question):
	c=question.split(" ")[0]
	d=c.split("'")[0]
	d=d.lower()	
	if(d in li):
		return True
	else:
		return False
	
	
question=""
while(question!="stop"):
	question=raw_input('Enter Question')

	if(checkend(question)==True):
		print("Ends with ?")

	elif(checklist(question)==True):
		print("List Present")

	elif(shortcut(question)==True):
		print("Last Block")

	else:
		print("Not a question")


	

