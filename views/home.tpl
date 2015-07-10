<!DOCTYPE html>

<html>
	<head>
		<title>Diary</title>
		<link rel='icon' href='/static/diary.png'>
		<link href='http://fonts.googleapis.com/css?family=Ubuntu+Mono:400,700,400italic,700italic|Cabin:400,700,400italic,700italic|Marck+Script|Vollkorn:400italic,700italic,400,700|Boogaloo' rel='stylesheet' type='text/css'>
		<link rel='stylesheet' href='//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css'>
		<link rel='stylesheet' href='/static/given.css'>
		<link rel='stylesheet' href='/static/home.css'>
	</head>
	<body>
		<div id='left'></div>
		<div id='middle'>
			<form action='/log' method='POST'>
				<textarea name='entry' rows='7' placeholder="What's on your mind..."></textarea>
				<button type='submit' title='Log'><i class='fa fa-pencil'></i></button>
			</form>
			<h3 id='recent'>-- Most Recent Entries --</h3>
			<div id='entries'>
			% i = 0
			% while i < len(entries):
				% entry = entries[i]
				<div class='entry'>
					<p class='date'>
						{{entry.time}} &nbsp;|&nbsp; {{entry.date}} &nbsp;|&nbsp;
						<a href='/erase/{{entry.id}}' title='Erase'><i class='fa fa-eraser'></i></a>
					</p>
					<p class='text'>{{entry.text}}</p>
				</div>
				% if i != len(entries) - 1:
					<hr>
				% end
				% i += 1
			% end
			</div>
		</div>
		<div id='right'></div>
	</body>
</html>
