li=[
"are","can","could","what","where",
"when","which","who","whom","whose",
"why","would","will","were","whether",
"was","do","does","did","dosen't",
"does","dosent","have","has","had",
"how","should","shall","may","if",
"isn't","isnt","is","any","whatsoever",
"aren't","arent","haven't","havent","wouldn't",
"wouldnt","whose","in","at","to","from","on",
"under","over","didn't","didnt","whatever",
"whoever","whomever","whichever","whenever",
"wherever","however","your","her",
"his","am","what's","how's","i've","i've","i",
"we","they","he","she","he'll","she'll",
"you'll","they'll","we'll","it'll","i'll","be",
"i'm",
]
question=""
	
while(question!='stop'):
	question=raw_input('enter string')
	wh=question.split(' ')[0]
	wh=wh.lower()	
	c=wh in li

	if question.endswith('?') is True:
		print(" end with ? condition execute")	

	elif(c is True):
		print("List word condition execute")	

	else:
		print("Ooops!")


