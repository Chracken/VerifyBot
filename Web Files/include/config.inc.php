<?php

/////////////////////////////////////////
//DATABASE SETTINGS//////////////////////
/////////////////////////////////////////

 define('DB_HOST', 'localhost'); //edit with bot server ip
 define('DB_USERNAME', 'siteusername'); //edit with mysql username
 define('DB_PASSWORD', 'sitepassword'); // edit with mysql password
 define('DB_NAME', 'verifybot'); // if you changed db_name change it here too.
 $botprefix = "!"; // edit with bot prefix
 $command = "verify"; // edit with verify comamand if you changed it
 $ProtectionLayer1 = TRUE;
 $ProtectionLayer2 = TRUE;
 $ProtectionLayer3 = TRUE;
/////////////////////////////////////////
//TRANSLATIONS///////////////////////////
/////////////////////////////////////////
 $SiteHeadName = "VerifyBot";
 $userbanned = "You are banned from this server!";
 $welcomemessage = "Welcome to VerifyBot Verification";
 $yourcodeis = "Your verification code is: ";
 $howtoverify = "Now go back to bot DM and write the following command: ";
 $warning = "If someone other than server team or verifybot told you to access this page please don't give verification code to him/her!";
 $sqlconnecterror = "Connect failed report this to administrator: ";
 $intro = "If you want to get verified, use the link from verifybot,<br> it can  be found in your dm if you started verification process!";
 $proxyblock = "Incognito, Proxy and VPN Clients are blocked on this SITE!";
/////////////////////////////////////////
//BROWSER SETTINGS///////////////////////
/////////////////////////////////////////
 $background_location_or_link = "include/background.png";
 $welcomemessagetextcolor = "white";
 $bordercolor = "gray";
 $yourcodeiscolor = "white";
 $passcodecolor = "white";
 $howtoverifycolor = "white";
 $commandcolor = "white";
 $warningcolor = "black";
 $introcolor = "white";
 $debug = FALSE;
/////////////////////////////////////////
//DATABASE CONNECTION////////////////////
/////////////////////////////////////////
$db = new mysqli(DB_HOST, DB_USERNAME, DB_PASSWORD, DB_NAME); 
if ($db->connect_errno) { 
	printf("'$sqlconnecterror' %s\n", $db->connect_error); 
exit(); 
}