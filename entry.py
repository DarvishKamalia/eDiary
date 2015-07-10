from datetime import datetime

class Entry:

	months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
	
	def __init__(self, text):
		now = datetime.now()
		ampm = 'pm' if now.hour >= 12 else 'am'
		hour = now.hour
		if hour >= 13:
			hour -= 12
		if hour == 0:
			hour = 12

		self.id = '%d%d%d%d%d%d%d' % (now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)
		self.date = '%d %s \'%s' % (now.day, Entry.months[now.month - 1], str(now.year)[2:])
		self.time = '%d:%02d %s' % (hour, now.minute, ampm)
		self.text = text

if __name__ == '__main__':
	x = Entry('parth')
	print x.id
	print x.date
	print x.time
	print x.text
