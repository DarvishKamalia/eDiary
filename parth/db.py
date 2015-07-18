import json, urllib2, datetime
import json #JSON encoder and decoder
import urllib2 #HTTP interface library
import time #for current date
import random #for random number
import codecs

file_db = 'storage/entries.json'
ENTRIES = 'storage/entries.json'
FEELINGS = 'storage/feelings.json'
ENCRYPT_KEY = 10
MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
QUOTE_API_URL = "https://raw.githubusercontent.com/DarvishKamalia/learning-diary-project-/master/parth/quote.json"

# create a new entry (just create it in memory, do not yet save it to disk)
def newEntry(text, feel):
	now = datetime.datetime.now()
	ampm = 'pm' if now.hour >= 12 else 'am'
	hour = now.hour
	if hour >= 13:
		hour -= 12
	if hour == 0:
		hour = 12

	entry = {}
	entry['id'] = '%d%d%d%d%d%d%d' % (now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)
	entry['year'] = str(now.year)
	entry['mon'] = MONTHS[now.month - 1]
	entry['day'] = str(now.day)
	entry['hour'] = hour
	entry['ampm'] = ampm
	entry['min'] = now.minute
	entry['sec'] = now.second
	entry['ms'] = now.microsecond
	entry['text'] = text.split('\n')
	entry['feel'] = feel
	return entry

# load everything from ENTRIES
def loadEntries():
	r = open(ENTRIES, 'r')
	print "called load"
	entries = json.load(r)
	r.close()
	for entry in entries:
		for index, string in enumerate(entry["text"]):
			entry["text"][index] = cipher(string, 1)
	print "finished load" 
	return entries

# store everything to ENTRIES
def storeEntries(entries):
	for entry in entries:
		for index, string in enumerate(entry["text"]):
			entry["text"][index] = cipher(string, 0)
	w = open(ENTRIES, 'wb')
	json.dump(entries, w)
	w.close()

# encrypt or decrypt a given text string using ENCRYPT_KEY defined in the header
# @param string The string to encrypt or decrypt
# @param mode 0 indicates that the string should be encrypted, 1 indicates it should be decrypted
# @retval result The string after being encrypted using the given key
def cipher (string, mode):
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
	return result

##Returns a random quote from the quotes database
#@retval quote
def getQuote():

	#Fetch JSON from API
	quoteJSON = urllib2.urlopen(QUOTE_API_URL)
	quoteData = json.load(quoteJSON)
	json.dumps (quoteData, indent=4)
	random.seed()
	index = random.randint(0, len(quoteData) - 1)
	print quoteData[index]
	return quoteData[index]


##Load everything contained in FEELINGS
#@retval dict of feelings and their emojis
def loadFeelings():
	r = open(FEELINGS, 'r')
	feelings = json.load(r)
	return feelings
