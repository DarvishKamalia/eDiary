import json #JSON encoder and decoder
import urllib2 #HTTP interface library
import time #for current date

file_db = 'storage/entries.json'

ENCRYPT_KEY = 10
QUOTE_API_URL = "http://api.theysaidso.com/qod.json"
QUOTE_FILE_NAME = "quote.json"

# load everything from file_db
def load():
	r = open(file_db, 'r')
	entries = json.load(r)
	for entry in entries:
		for index, string in enumerate(entry["text"]):
		 entry["text"][index] = cipher(string, 1)
	r.close()
	return entries

# store everything to file_db
def store(entries):
	w = open(file_db, 'wb')
	for entry in entries:
		for index, string in enumerate(entry["text"]):
		 entry["text"][index] = cipher(string, 0)
	json.dump(entries, w, indent=4)
	w.close()

# encrypt or decrypt a given text string using ENCRYPT_KEY defined in the header
# @param string The string to encrypt or decrypt
# @param mode 0 indicates that the string should be encrypted, 1 indicates it should be decrypted
# @retval result The string after being encrypted using the given key
def cipher (string, mode):
	print "encrypting ", string
	key = ENCRYPT_KEY
	if (mode == 1) :
		key = -key
	result = ""
	for character in string:
		if character.isalpha():
			num = ord(character) #Get ordinal number from the character
			num += key

			#These ensure that the encrypted character is alphanumeric
			if character.isupper():
				if num > ord('Z'):
					num -= 26
				elif num < ord('A'):
					num += 26
			elif character.islower():
				if num > ord('z'):
					num -= 26
				elif num < ord('a'):
					num += 26
			result += chr(num) #convert number back to a string

		else:
			result += character

	print "encrypted ", result
	return result

##Returns a random quote from the quotes database
#@retval quote
def getQuote():

	#Fetch JSON from API
	r = open (QUOTE_FILE_NAME, 'r')
	today = time.strftime("%d/%m/%Y")
	quoteData = json.load(r)
	exists = True

	try:
		storedDate = quoteData["date"]

	except KeyError:
		exists = False

	if (not exists or quoteData["date"] != today):
			print "loading" 
			quoteJSON = urllib2.urlopen(QUOTE_API_URL)
			quoteData = json.loads(quoteJSON.read())
			quoteData["date"] = today
			w = open (QUOTE_FILE_NAME, 'wb')
			json.dump(quoteData, w)

	return {"text" : quoteData["contents"]["quotes"][0]["quote"] ,
				"author" : quoteData["contents"]["quotes"][0]["author"]}
