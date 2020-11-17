<?php
include_once 'include/config.inc.php'; 
error_reporting(E_ALL); 
ini_set('ignore_repeated_errors', TRUE); 
ini_set('display_errors', FALSE); 
ini_set('log_errors', TRUE);
ini_set("error_log", "$SiteHeadName.log"); 
include 'Mobile_Detect.php';
$detect = new Mobile_Detect();
$cookie_name = "authorization";
if(!isset($_COOKIE[$cookie_name])) {
   // maybe add something later.
} else {
  $datacookie = $_COOKIE[$cookie_name];
}

function getUserIpAddr(){
    if(!empty($_SERVER['HTTP_CLIENT_IP'])){
        $ip = $_SERVER['HTTP_CLIENT_IP'];
    }elseif(!empty($_SERVER['HTTP_X_FORWARDED_FOR'])){
        $ip = $_SERVER['HTTP_X_FORWARDED_FOR'];
    }else{
        $ip = $_SERVER['REMOTE_ADDR'];
    }
	return $ip;
}

function get_ip_address($proxy = false)
{
    if ($proxy === true)
    {
        foreach (array('HTTP_CLIENT_IP', 'HTTP_X_FORWARDED_FOR', 'HTTP_X_FORWARDED', 'HTTP_X_CLUSTER_CLIENT_IP', 'HTTP_FORWARDED_FOR', 'HTTP_FORWARDED') as $key)
        {
            if (array_key_exists($key, $_SERVER) === true)
            {
                foreach (array_map('trim', explode(',', $_SERVER[$key])) as $ip)
                {
                    if (filter_var($ip, FILTER_VALIDATE_IP, FILTER_FLAG_IPV4 | FILTER_FLAG_IPV6 | FILTER_FLAG_NO_PRIV_RANGE | FILTER_FLAG_NO_RES_RANGE) !== false)
                    {
                        return $ip;
                    }
                }
            }
        }
    }

    return $_SERVER['REMOTE_ADDR'];
}

function generateRandomString($length = 10) {
    $characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
    $charactersLength = strlen($characters);
    $randomString = '';
    for ($i = 0; $i < $length; $i++) {
        $randomString .= $characters[rand(0, $charactersLength - 1)];
    }
    return $randomString;
}

$v6 = preg_match("/^[0-9a-f]{1,4}:([0-9a-f]{0,4}:){1,6}[0-9a-f]{1,4}$/", getUserIpAddr());
$v4 = preg_match("/^([0-9]{1,3}\.){3}[0-9]{1,3}$/", getUserIpAddr());
$userip = getUserIpAddr();


if ($ProtectionLayer1 == TRUE) {
	if (get_ip_address() !== get_ip_address(true))
	{
		die("$proxyblock");
	}
}
if ($ProtectionLayer2 == TRUE) {
	$cont = @file_get_contents($_SERVER["REMOTE_ADDR"]);
	$errormsg = "nginx";
	if(strpos($cont, $errormsg)){
		die("$proxyblock");
	}
}
if ($ProtectionLayer3 == TRUE) {
	$ports = array(8080,80,81,443,1080,6588,8000,3128,553,554,4480);
	foreach($ports as $port) {
		if (@fsockopen($_SERVER['REMOTE_ADDR'], $port, $errno, $errstr, 1)) {
			die("$proxyblock");
		}
	}
}
$headkey = get('u');
$authorization = "SELECT * FROM security WHERE authorization = '$headkey'";
$letsqueryusers = $db->query($authorization);
	if ($letsqueryusers->num_rows > 0) {
		while($row = $letsqueryusers->fetch_assoc()) {
			if(get('u') == $row["authorization"]) 
			{
				if(!isset($_COOKIE[$cookie_name])) {
					$cookiecode = $row["authorization"] . generateRandomString(150);
				} else {
					$cookiecode = $_COOKIE[$cookie_name];
				}

				if ($v6 == True)
				{
					if ($debug == TRUE)
					{
						echo 'V6 TRUE<br>';
					}
				}
				else if ($v6 == False)
				{
					if ($debug == TRUE)
					{
						echo 'V6 FALSE<br>';
					}
				}
				if ($v4 == True)
				{
					if ($debug == TRUE)
					{
						echo 'V4 TRUE<br>';
					}	
				}
				else if ($v4 == False)
				{
					if ($debug == TRUE)
					{
						echo 'V4 FALSE<br>';
					}	
				}
				if ($detect->isMobile()){
					if( $detect->isiOS() ){
						//ios
						if ($debug == TRUE)
						{
							echo 'iOS TRUE<br>';
						}
						if ($v6 == True)
						{
							if ($row["ipv63"] == "FEC0:0000:0000:0000:0000:0000:0000:0001")
							{
								$sendipv63ios = "UPDATE security SET ipv63 = '$userip' WHERE authorization = '$headkey'";
								$db->query($sendipv63ios);
							}
						}
						if ($v4 == True)
						{
							if ($row["ipv43"] == "0.0.0.0")
							{
								$sendipv43ios = "UPDATE security SET ipv43 = '$userip' WHERE authorization = '$headkey'";
								$db->query($sendipv43ios);
							}
						}
						if ($row["key7"] == "NOTSET")
						{
							setcookie("authorization", "$cookiecode", 2147483647);
							$sendcookiecodeios = "UPDATE security SET key7 = '$cookiecode' WHERE authorization = '$headkey'";
							$db->query($sendcookiecodeios);
						}
						else
						{
							$getcookiecodeios2 = $datacookie;
							if ($getcookiecodeios2 == $row["key7"])
							{
								//return
							}
							else
							{
								if ($row["key8"] == "NOTSET")
								{
									setcookie("authorization", "$cookiecode", 2147483647);
									$sendcookiecodeios2 = "UPDATE security SET key8 = '$cookiecode' WHERE authorization = '$headkey'";
									$db->query($sendcookiecodeios2);
								}
								else
								{
									$getcookiecodeios3 = $datacookie;
									if ($getcookiecodeios3 == $row["key8"])
									{
										//return
									}
									else
									{
										if ($row["key9"] == "NOTSET")
										{
											setcookie("authorization", "$cookiecode", 2147483647);
											$sendcookiecodeios3 = "UPDATE security SET key9 = '$cookiecode' WHERE authorization = '$headkey'";
											$db->query($sendcookiecodeios3);
										}
										else
										{
											$getcookiecodeios4 = $datacookie;
											if ($getcookiecodeios4 == $row["key9"])
											{
												//return
											}
											else
											{
												setcookie("authorization", "$cookiecode", 2147483647);
												$sendcookiecodeios4 = "UPDATE security SET key7 = '$cookiecode' WHERE authorization = '$headkey'";
												$db->query($sendcookiecodeios4);
											}
										}
									}
								}
							}
						}
					}
					if( $detect->isAndroidOS() ){
					//android
						if ($debug == TRUE)
						{
							echo 'Android TRUE<br>';
						}
						if ($v6 == True)
						{
							if ($row["ipv62"] == "FEC0:0000:0000:0000:0000:0000:0000:0001")
							{
								$sendipv62android = "UPDATE security SET ipv62 = '$userip' WHERE authorization = '$headkey'";
								$db->query($sendipv62android);
							}
						}
						if ($v4 == True)
						{
							if ($row["ipv42"] == "0.0.0.0")
							{
								$sendipv42android = "UPDATE security SET ipv42 = '$userip' WHERE authorization = '$headkey'";
								$db->query($sendipv42android);
							}
						}
						if ($row["key4"] == "NOTSET")
						{
							setcookie("authorization", "$cookiecode", 2147483647);
							$sendcookiecodeandroid = "UPDATE security SET key4 = '$cookiecode' WHERE authorization = '$headkey'";
							$db->query($sendcookiecodeandroid);
						}
						else
						{
							$getcookiecodeandroid2 = $datacookie;
							if ($getcookiecodeandroid2 == $row["key4"])
							{
								//return
							}
							else
							{
								if ($row["key5"] == "NOTSET")
								{
									setcookie("authorization", "$cookiecode", 2147483647);
									$sendcookiecodeandroid2 = "UPDATE security SET key5 = '$cookiecode' WHERE authorization = '$headkey'";
									$db->query($sendcookiecodeandroid2);
								}
								else
								{
									$getcookiecodeandroid3 = $datacookie;
									if ($getcookiecodeandroid3 == $row["key5"])
									{
										//return
									}
									else
									{
										if ($row["key6"] == "NOTSET")
										{
											setcookie("authorization", "$cookiecode", 2147483647);
											$sendcookiecodeandroid3 = "UPDATE security SET key6 = '$cookiecode' WHERE authorization = '$headkey'";
											$db->query($sendcookiecodeandroid3);
										}
										else
										{
											$getcookiecodeandroid4 = $datacookie;
											if ($getcookiecodeandroid4 == $row["key6"])
											{
												//return
											}
											else
											{
												setcookie("authorization", "$cookiecode", 2147483647);
												$sendcookiecodeandroid4 = "UPDATE security SET key4 = '$cookiecode' WHERE authorization = '$headkey'";
												$db->query($sendcookiecodeandroid4);
											}
										}
									}
								}
							}
						}
					}
				}
				else {
					//dekstop
					if ($debug == TRUE)
					{
						echo 'Desktop TRUE<br>';
					}
					
					if ($v6 == True)
					{
						if ($row["ipv61"] == "FEC0:0000:0000:0000:0000:0000:0000:0001")
						{
							$sendipv61desktop = "UPDATE security SET ipv61 = '$userip' WHERE authorization = '$headkey'";
							$db->query($sendipv61desktop);
						}
					}
					if ($v4 == True)
					{
						if ($row["ipv41"] == "0.0.0.0")
						{
							$sendipv41desktop = "UPDATE security SET ipv41 = '$userip' WHERE authorization = '$headkey'";
							$db->query($sendipv41desktop);
						}
					}
					
					if ($row["key1"] == "NOTSET")

					{
						setcookie("authorization", "$cookiecode", 2147483647);
						$sendcookiecodedesktop = "UPDATE security SET key1 = '$cookiecode' WHERE authorization = '$headkey'";
						$db->query($sendcookiecodedesktop);
					}
					else
					{
						$getcookiecodedesktop2 = $datacookie;
						if ($getcookiecodedesktop2 == $row["key1"])
						{
							//return
						}
						else
						{
							if ($row["key2"] == "NOTSET")
							{
								setcookie("authorization", "$cookiecode", 2147483647);
								$sendcookiecodedesktop2 = "UPDATE security SET key2 = '$cookiecode' WHERE authorization = '$headkey'";
								$db->query($sendcookiecodedesktop2);
							}
							else
							{
								$getcookiecodedesktop3 = $datacookie;
								if ($getcookiecodedesktop3 == $row["key2"])
								{
									//return
								}
								else
								{
									if ($row["key3"] == "NOTSET")
									{
										setcookie("authorization", "$cookiecode", 2147483647);
										$sendcookiecodedesktop3 = "UPDATE security SET key3 = '$cookiecode' WHERE authorization = '$headkey'";
										$db->query($sendcookiecodedesktop3);
									}
									else
									{
										$getcookiecodedesktop4 = $datacookie;
										if ($getcookiecodedesktop4 == $row["key3"])
										{
											//return
										}
										else
										{
											setcookie("authorization", "$cookiecode", 2147483647);
											$sendcookiecodedesktop4 = "UPDATE security SET key1 = '$cookiecode' WHERE authorization = '$headkey'";
											$db->query($sendcookiecodedesktop4);
										}
									}
								}
							}
						}
					}
				}
				$passcode = $row["passcode"];
				$commandtoinsert = "$botprefix$command $passcode";
	
				echo "
				<html>
					<head>
						<title>$SiteHeadName</title>
						<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
						<link rel=\"apple-touch-icon\" sizes=\"180x180\" href=\"/favicons/apple-touch-icon.png\">
						<link rel=\"icon\" type=\"image/png\" sizes=\"32x32\" href=\"/favicons/favicon-32x32.png\">
						<link rel=\"icon\" type=\"image/png\" sizes=\"16x16\" href=\"/favicons/favicon-16x16.png\">
						<link rel=\"manifest\" href=\"/favicons/site.webmanifest\">
						<link rel=\"mask-icon\" href=\"/favicons/safari-pinned-tab.svg\" color=\"#5bbad5\">
						<link rel=\"shortcut icon\" href=\"/favicons/favicon.ico\">
						<meta name=\"msapplication-TileColor\" content=\"#da532c\">
						<meta name=\"msapplication-config\" content=\"/favicons/browserconfig.xml\">
						<meta name=\"theme-color\" content=\"#ffffff\">
					</head>
					<style>
						body {
							font-family: 'Poppins', sans-serif !important;
							background: url('$background_location_or_link') no-repeat center center fixed; 
							-webkit-background-size: cover;
							-moz-background-size: cover;
							-o-background-size: cover;
							background-size: cover;
							color: #fff;
							-webkit-font-smoothing: antialiased;
							-moz-osx-font-smoothing: grayscale;
							text-rendering: optimizeLegibility;
							font-size: 16px;
						}
					</style>
					<body>
					<script>
					async function main() {
					  if ('storage' in navigator && 'estimate' in navigator.storage) {
					      const {usage, quota} = await navigator.storage.estimate();
					      console.log(`Using \${usage}\ out of \${quota}\ bytes.`);
					
					      if(quota < 120000000){
					        window.location.href = \"incognito.php\";
					      } else {
					      }   
 					 } else {
      
 					 }
					}
					main();
					</script>
					<script src=\"BrowsingModeDetector.js\"></script>
					<script>
					var myCallback = function (browsingInIncognitoMode, BrowsingModeDetectorInstance) {
					    console.log('Is private?', browsingInIncognitoMode);
					    console.log('Browsing Mode:', BrowsingModeDetectorInstance.getBrowsingMode());
  
					    if (browsingInIncognitoMode) {
					        window.location.href = \"incognito.php\";
					        return;
 					   }
  
					    // Normal mode detected
					};
					var BrowsingModeDetector = new BrowsingModeDetector();
					BrowsingModeDetector.do(myCallback);
					</script>
						<div style='position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); opacity:0.9;filter:alpha(opacity=90); width: 80%;  height: 70%; background: $bordercolor;BORDER=8'><br>
						<center>
						<font size='5' color='$welcomemessagetextcolor'>$welcomemessage</font><br><br>";
				if ($row["status"] == "OK")
				{
					echo "
					<font size='4' color='$yourcodeiscolor'>$yourcodeis</font><br><font size='5' color='$passcodecolor'>$passcode</font><br><br><br>
					<font size='4' color='$howtoverifycolor'>$howtoverify</font><br>
					<font size='5' color='$commandcolor'>$commandtoinsert</font><br><br><br><br>
					<font size='3' color='$warningcolor'>$warning</font><br> 
					</center></div></body></html>";
				}
				if ($row["status"] == "BLOCKED")
				{
					echo "
					<font size='4' color='red'>$userbanned</font><br>
					<font size='4' color='blue'>$userbanned</font><br>
					<font size='4' color='green'>$userbanned</font><br>
					<font size='4' color='white'>$userbanned</font><br>
					<font size='4' color='yellow'>$userbanned</font><br>
					<font size='4' color='black'>$userbanned</font><br>
					<font size='4' color='orange'>$userbanned</font><br>
					<font size='4' color='cyan'>$userbanned</font><br>
					</center></div></body>
				</html>";		
				}
			}
		}
	}
	else {
		if ($debug == TRUE)
		{
			echo 'User Not Found';
		}
		echo "
		<html>
			<head>
				<title>$SiteHeadName</title>
				<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
				<link rel=\"apple-touch-icon\" sizes=\"180x180\" href=\"/favicons/apple-touch-icon.png\">
				<link rel=\"icon\" type=\"image/png\" sizes=\"32x32\" href=\"/favicons/favicon-32x32.png\">
				<link rel=\"icon\" type=\"image/png\" sizes=\"16x16\" href=\"/favicons/favicon-16x16.png\">
				<link rel=\"manifest\" href=\"/favicons/site.webmanifest\">
				<link rel=\"mask-icon\" href=\"/favicons/safari-pinned-tab.svg\" color=\"#5bbad5\">
				<link rel=\"shortcut icon\" href=\"/favicons/favicon.ico\">
				<meta name=\"msapplication-TileColor\" content=\"#da532c\">
				<meta name=\"msapplication-config\" content=\"/favicons/browserconfig.xml\">
				<meta name=\"theme-color\" content=\"#ffffff\">

			</head>
			<style>
				body {
				font-family: 'Poppins', sans-serif !important;
				background: url('$background_location_or_link') no-repeat center center fixed; 
				-webkit-background-size: cover;
				-moz-background-size: cover;
				-o-background-size: cover;
				background-size: cover;
				color: #fff;
				-webkit-font-smoothing: antialiased;
				-moz-osx-font-smoothing: grayscale;
				text-rendering: optimizeLegibility;
				font-size: 16px;
				}
			</style>
			<body>
				<script>
				async function main() {
 				 if ('storage' in navigator && 'estimate' in navigator.storage) {
  				    const {usage, quota} = await navigator.storage.estimate();
 				     console.log(`Using \${usage}\ out of \${quota}\ bytes.`);

 				     if(quota < 120000000){
 				       window.location.href = \"incognito.php\";
 				     } else {
				      }   
				  } else {
      
 				 }
				}
				main();
				</script>
				<script src=\"BrowsingModeDetector.js\"></script>
				<script>
				var myCallback = function (browsingInIncognitoMode, BrowsingModeDetectorInstance) {
				    console.log('Is private?', browsingInIncognitoMode);
				    console.log('Browsing Mode:', BrowsingModeDetectorInstance.getBrowsingMode());
  
				    if (browsingInIncognitoMode) {
				        window.location.href = \"incognito.php\";
				        return;
				    }
  
				    // Normal mode detected
				};
				var BrowsingModeDetector = new BrowsingModeDetector();
				BrowsingModeDetector.do(myCallback);
				</script>

			
				<div style='position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); opacity:0.9;filter:alpha(opacity=90); width: 60%; height: 60%; background: $bordercolor;BORDER=8'><br>
				<center>
					<font size='5' color='$welcomemessagetextcolor'>$welcomemessage</font><br><br><br><br>
					<font size='4' color='$introcolor'>$intro</font> <br>
				</center>
				</div>
			</body>
		</html>";
	}
function get($key, $default=NULL) {
  return array_key_exists($key, $_GET) ? $_GET[$key] : $default;
}
?>