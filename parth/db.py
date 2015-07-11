import json

file_db = 'storage/entries.json'

# load everything from file_db
def load():
	r = open(file_db, 'r')
	entries = json.load(r)
	r.close()
	return entries

# store everything to file_db
def store(entries):
	w = open(file_db, 'w')
	json.dump(entries, w)
	w.close()
