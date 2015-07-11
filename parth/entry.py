import datetime

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

def make(text):
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
	entry['mon'] = months[now.month - 1]
	entry['day'] = str(now.day)
	entry['hour'] = hour
	entry['ampm'] = ampm
	entry['min'] = now.minute
	entry['sec'] = now.second
	entry['ms'] = now.microsecond
	entry['text'] = text.split('\n')
	return entry
