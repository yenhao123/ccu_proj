<?php 
$url = 'http://db4b606e8643.ngrok.io/action_page.phphttp://db4b606e8643.ngrok.io/ccuproj/action_page.php?Name=f&Email=f&Subject=f&Comment=f'; 
//$url = "http://127.0.0.1/ccuproj/action_page.php?Name=f&Email=f&Subject=f&Comment=f";

$param = array( 
	'name'=>'fdipzone', 
	'gender'=>'male', 
	'age'=>30 
); 
var_dump($param);
asyncRequest($url, $param); 
function asyncRequest($url, $param=array()){ 	
	$urlinfo = parse_url($url); 
	$host = $urlinfo['host']; 
	$path = $urlinfo['path']; 
	$query = isset($param)? http_build_query($param) : ''; 
	$port = 80; 
	$errno = 0; 
	$errstr = ''; 
	$timeout = 30; 
	$fp = @fsockopen($host, $port, $errno, $errstr, $timeout); 
	$out = "POST ".$path." HTTP/1.1\r\n"; 
	$out .= "host:".$host."\r\n"; 
	$out .= "content-length:".strlen($query)."\r\n"; 
	$out .= "content-type:application/x-www-form-urlencoded\r\n"; 
	$out .= "connection:close\r\n\r\n"; 
	$out .= $query; 
	echo "<p>".$out."</p>";
	fputs($fp, $out); 
	fclose($fp); 
} 
?>
