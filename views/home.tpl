<!DOCTYPE html>

<html>
	<head>
		<title>Diary</title>
		<link rel='icon' href='/static/diary.png'>
		<link href='http://fonts.googleapis.com/css?family=Ubuntu+Mono:400,700,400italic,700italic|Cabin:400,700,400italic,700italic|Vollkorn:400italic,700italic,400,700|Boogaloo|Marck+Script' rel='stylesheet' type='text/css'>
		<link rel='stylesheet' href='//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css'>
		<link rel='stylesheet' href='/static/style.css'>
	</head>
	<body>
		<div id='left'>
		</div>
		<div id='middle'>
			<h1 id='diary'>Your Diary</h1>
			<form class='log' action='/log' method='POST'>
				<div class='log'>
					<textarea class='log' name='text' rows='7' placeholder="What's on your mind..."></textarea>
					<select class='log' name='feel'>
						<option value='' selected>How are you feeling...</option>
					% for feel, emoji in feelings.iteritems():
						<option value='{{feel}}'>&#x{{emoji}};&nbsp; {{feel}}</option>
					% end
					</select>
				</div>
				<button class='log' type='submit'><i class='fa fa-pencil'></i>&nbsp; Log</button>
			</form>
			<h3 id='all'>All Entries</h3>
			<div id='entries'>
			% i = 0
			% while i < len(entries):
				% entry = entries[i]
				<div class='entry'>
					<p class='date'>
				% if entry['feel'] != '':
						<span title='{{entry['feel']}}'>&#x{{feelings[entry['feel']]}};</span> &nbsp;|&nbsp;
				% end
						{{'%d:%02d %s' % (entry['hour'], entry['min'], entry['ampm'])}} &nbsp;|&nbsp;
						{{'%s %s \'%s' % (entry['day'], entry['mon'], entry['year'][2:])}} &nbsp;|&nbsp;
						<a href='/erase/{{entry['id']}}' title='erase'><i class='fa fa-eraser'></i></a>
					</p>
					<pre class='text'>{{entry['text']}}</pre>
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
