from markdown import markdown

# load head, midd, foot

head_file = open('head.html')
head = head_file.read()
head_file.close()

midd_file = open('midd.html')
midd = midd_file.read()
midd_file.close()

foot_file = open('foot.html')
foot = foot_file.read()
foot_file.close()

# convert md to html

home_file = open('home.md')
title = 'home'
body = markdown(home_file.read())
home_file.close()

# combine everything, write to file
home_file = open('home.html', 'w')
everything = head + title + midd + body + foot
home_file.write(everything)
home_file.close()
