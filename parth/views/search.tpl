<!DOCTYPE html>

<html>
	<head>
		<title>Diary</title>
		<link rel='icon' href='/static/diary.png'>
		<link href='http://fonts.googleapis.com/css?family=Ubuntu+Mono:400,700,400italic,700italic|Cabin:400,700,400italic,700italic|Vollkorn:400italic,700italic,400,700|Boogaloo|Josefin+Sans:400,600,400italic,600italic' rel='stylesheet' type='text/css'>
		<link rel='stylesheet' href='//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css'>
		<link rel='stylesheet' href='/static/given.css'>
		<link rel='stylesheet' href='/static/home.css'>
	</head>
	<body>
		<div id='middle'>
			<h3 id='recent'>Search Results</h3>
			<div id='entries'>
			% i = 0
			% while i < len(entries):
				% entry = entries[i]
				<div class='entry'>
					<p class='date'>
						{{'%d:%02d %s' % (entry['hour'], entry['min'], entry['ampm'])}} &nbsp;|&nbsp;
						{{'%s %s \'%s' % (entry['day'], entry['mon'], entry['year'][2:])}} &nbsp;|&nbsp;
						<a href='/erase/{{entry['id']}}' title='Erase'><i class='fa fa-eraser'></i></a>
					</p>
				% for line in entry['text']:
					% if line != u'\r':
						<p class='text'>{{line}}</p>
					% else:
						<br>
					% end
				% end
				</div>
				% if i != len(entries) - 1:
					<hr>
				% end
				% i += 1
			% end
			</div>
		</div>
	</body>
</html>
