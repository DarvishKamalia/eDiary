import json, urllib2, datetime

ENTRIES = 'storage/entries.json'
FEELINGS = 'storage/feelings.json'
QUOTE = 'storage/quote.json'
ENCRYPT_KEY = 10
QUOTE_API_URL = "http://api.theysaidso.com/qod.json"
MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

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
	entries = json.load(r)
	r.close()
	for entry in entries:
		for index, string in enumerate(entry["text"]):
			entry["text"][index] = cipher(string, 1)
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
	r = open(QUOTE, 'r')
	quote = json.load(r)
	r.close();

	if quote['day'] == datetime.datetime.now().day:
		return quote
	else:
		#Fetch JSON from API
		quoteJSON = urllib2.urlopen(QUOTE_API_URL)
		quoteData = json.loads(quoteJSON.read())
		quote =  { "quote" : quoteData["contents"]["quotes"][0]["quote"],
					  "author" : quoteData["contents"]["quotes"][0]["author"],
					  "day" : datetime.datetime.now().day }
		w = open(QUOTE, 'wb')
		json.dump(quote, w)
		w.close()
		return quote

##Load everything contained in FEELINGS
#@retval dict of feelings and their emojis
def loadFeelings():
	r = open(FEELINGS, 'r')
	feelings = json.load(r)
	return feelings
