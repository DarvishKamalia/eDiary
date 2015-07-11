<!DOCTYPE html>

<html>
	<head>
		<title>Diary</title>
		<link rel='icon' href='/static/diary.png'>
		<link href='http://fonts.googleapis.com/css?family=Ubuntu+Mono:400,700,400italic,700italic|Cabin:400,700,400italic,700italic|Vollkorn:400italic,700italic,400,700|Boogaloo|Marck+Script' rel='stylesheet' type='text/css'>
		<link rel='stylesheet' href='//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css'>
		<link rel='stylesheet' href='/static/given.css'>
		<link rel='stylesheet' href='/static/signin.css'>
	</head>
	<body>
		<div id='left'></div>
		<div id='middle'>
			<h2 class='signin'>Welcome!</h2>
			<form class='signin' action='/signin' method='POST'>
				<input class='signin' type='text' name='name' placeholder='First/Nick Name'>
				<button class='signin' type='submit'><i class='fa fa-sign-in'></i>&nbsp; Sign In</button>
			</form>
		</div>
		<div id='right'></div>
	</body>
</html>
