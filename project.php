<?php
	#$ip = $_GET['ip'];
	$ip = "140.123.0.0/16";
	$count = 5;
	$filename = "project.txt";
	//echo "<p>Please wait a minute, we are addressing your data now.</p>";
	
	//$url = "http://7dee16c23e43.ngrok.io/ccuproj/home.html";
	$command = "python ./api/main.py --ip ".$ip." --count ".$count." > ".$filename;
	shell_exec($command);
	sleep(2);
?>
