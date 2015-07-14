<!DOCTYPE html>

<html>
	<head>
		<title>Diary</title>
		<link rel='icon' href='/static/diary.png'>
		<link href='http://fonts.googleapis.com/css?family=Ubuntu+Mono:400,700,400italic,700italic|Cabin:400,700,400italic,700italic|Vollkorn:400italic,700italic,400,700|Boogaloo|Marck+Script' rel='stylesheet' type='text/css'>
		<link rel='stylesheet' href='//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css'>
		<link rel='stylesheet' href='/static/given.css'>
		<link rel='stylesheet' href='/static/home.css'>
	</head>
	<body>
		<div id='left'>
			<form class='search' action='/search'>
				<div class='search'>
					<select class='search' name='day'>
						<option selected value=''>dd</option>
					% for date in range(1,32):
						<option value='{{date}}'>{{date}}</option>
					% end
					</select>
					<select class='search' name='mon'>
						<option selected value=''>mmm</option>
					% months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
					% for month in months:
						<option value='{{month}}'>{{month}}</option>
					% end
					</select>
					<select class='search' name='year'>
						<option selected value=''>yyyy</option>
					% import datetime
					% for year in range(2015, datetime.datetime.now().year + 1):
						<option value='{{year}}'>{{year}}</option>
					% end
					</select>
				</div>
				<button class='search' type='submit'><i class='fa fa-search'></i>&nbsp; Search</button>
			</form>
		</div>
		<div id='middle'>
			<h1 id='diary'>Your Diary</h1>
			<form class='log' action='/log' method='POST'>
				<textarea class='log' name='entry' rows='7' placeholder="What's on your mind..."></textarea>
				<button class='log' type='submit'><i class='fa fa-pencil'></i>&nbsp; Log</button>
			</form>
			<h3 id='recent'>Recent Entries</h3>
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
		<div id='right'>
			<form class='name' action='/signout'>
				<p class='name'>Hi there, {{name}}!</p>
				<button class='name' type='submit'><i class='fa fa-sign-out'></i>&nbsp; Sign Out</button>
			</form>
		</div>
	</body>
</html>
