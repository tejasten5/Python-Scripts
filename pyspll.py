from spellchecker import SpellChecker

spell = SpellChecker()
misspelled = spell.unknown([

"clint",
"vendr",
"campign",
"pending",
"assigned"
"live",
"completed",
"lead rejected reason",
"lead rectified reason",
"Tech",
"tickits",
"User Access",
"Notifation",
"Reenue",
"clint list",
"venor list",
"caaign list",
"onbarding",




	])

for word in misspelled:
	print(spell.correction(word))

  