from markdown import markdown
import os

# load head, midd, foot

head_file = open('html/head.html')
head = head_file.read()
head_file.close()

midd_file = open('html/midd.html')
midd = midd_file.read()
midd_file.close()

foot_file = open('html/foot.html')
foot = foot_file.read()
foot_file.close()

mds = os.listdir('md')
for md in mds:
	
	# convert md to html
	body_file = open('md/' + md)
	body = markdown(body_file.read())
	body_file.close()

	title = md[:-3]

	# combine everything, write to file
	site_file = open(title + '.html', 'w')
	site_file.write(head + title + midd + body + foot)
	site_file.close()
