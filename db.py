from datetime import datetime
import json

file_db = 'entries.json'

def makeEntry(text):
	now = datetime.now()
	ampm = 'pm' if now.hour >= 12 else 'am'
	hour = now.hour
	if hour >= 13:
		hour -= 12
	if hour == 0:
		hour = 12

	months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
	
	entry = {}
	entry['id'] = '%d%d%d%d%d%d%d' % (now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)
	entry['date'] = '%d %s \'%s' % (now.day, months[now.month - 1], str(now.year)[2:])
	entry['time'] = '%d:%02d %s' % (hour, now.minute, ampm)
	entry['text'] = text
	return entry

def getEntries():
	r = open(file_db, 'r')
	entries = json.load(r)
	r.close()
	return entries

def logEntry(entry):
	r = open(file_db, 'r')
	entries = json.load(r)
	r.close()
	entries.insert(0, entry)
	w = open(file_db, 'w')
	json.dump(entries, w)
	w.close()

def eraseEntry(id):
	r = open(file_db, 'r')
	entries = json.load(r)
	r.close()

	i = 0
	while i < len(entries):
		if id == entries[i]['id']:
			del entries[i]
			break
		i += 1

	w = open(file_db, 'w')
	json.dump(entries, w)
	w.close()
