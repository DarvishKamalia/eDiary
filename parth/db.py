import json

file_db = 'storage/entries.json'

ENCRYPT_KEY = 10

# load everything from file_db
def load():
	r = open(file_db, 'r')
	entries = json.load(r)
	r.close()
	return entries

# store everything to file_db
def store(entries):
	w = open(file_db, 'w')
	for entry in entries:
		entry["text"] = cipher(entry["text"], 0)
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
		if character.isAlpha():
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
