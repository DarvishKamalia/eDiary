import json, datetime

ENTRIES = 'storage/entries.json'
FEELINGS = 'storage/feelings.json'
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
	entry['text'] = text
	entry['feel'] = feel
	return entry

# load everything from ENTRIES
def loadEntries():
	r = open(ENTRIES, 'r')
	entries = json.load(r)
	r.close()
	return entries

# store everything to ENTRIES
def storeEntries(entries):
	w = open(ENTRIES, 'w')
	json.dump(entries, w)
	w.close()

# load FEELINGS
def loadFeelings():
	r = open(FEELINGS, 'r')
	feelings = json.load(r)
	r.close()
	return feelings
