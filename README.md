# VerifyBot  
Verify System for Discord servers made with Python, MySQL and PHP.  
How it works?  
When someone joins your server they will get a validation link from bot on DM  
When they start Validation Process, their unique browser id will be sent in database (Also Their IP if you want to use IP BAN SYSTEM by default it is disabled).  
So! When you ban someone using verifybot that person will be banned on browser id and will be hard for them to join again.  
Validation url don't allow proxy servers, vpn clients or incognito mode!  
Sometimes it can be accessed using chrome incognito but don't bother too much they will be recognized by the bot anyway  

#Requirements
Ubuntu 16.04 server or any other linux, just adapt!  
WebServer with php5.0+ and mysqli enabled.  

#Tutorial
----
Install MySQL (SSH CONSOLE)
----
`sudo apt update`  
`sudo apt install mysql-server`  
You have to remember your mysql root password!

----
Edit MySQL (SSH CONSOLE)
----
Use the following command in terminal:  
`nano /etc/mysql/mysql.conf.d/mysqld.cnf`  
search for:  
`bind-address		= 127.0.0.1`  
disable it by adding # before it, now it should look like:   
`#bind-address		= 127.0.0.1`  

search for:   
`#max_connections        = 100`  
enable it removing # and edit with:  
`max_connections        = 512`  
Now leave nano using ctrl+x then press y and hit enter twice  

Use the following command in terminal:  
`mysql -u root -p`  
now use your password from mysql installation.  

Now let's build our mysql   
!!remember to change <siteusername> with any username and <sitepassword> with any password  
  Use the following mysql commands:  

`GRANT ALL PRIVILEGES ON *.* to 'siteusername'@'%' identified by 'sitepassword' with grant option;`  
`Flush Privileges;`  
`CREATE DATABASE verifybot;`  
`use verifybot;`  
`SET FOREIGN_KEY_CHECKS=0;`  
```
CREATE TABLE `security` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `userid` bigint(20) DEFAULT NULL,
  `status` varchar(255) DEFAULT 'OK',
  `authorization` varchar(255) DEFAULT 'NOTSET',
  `passcode` varchar(255) DEFAULT 'NOTSET',
  `key1` varchar(255) DEFAULT 'NOTSET',
  `key2` varchar(255) DEFAULT 'NOTSET',
  `key3` varchar(255) DEFAULT 'NOTSET',
  `key4` varchar(255) DEFAULT 'NOTSET',
  `key5` varchar(255) DEFAULT 'NOTSET',
  `key6` varchar(255) DEFAULT 'NOTSET',
  `key7` varchar(255) DEFAULT 'NOTSET',
  `key8` varchar(255) DEFAULT 'NOTSET',
  `key9` varchar(255) DEFAULT 'NOTSET',
  `key10` varchar(255) DEFAULT 'NOTSET',
  `ipv41` varchar(255) DEFAULT '0.0.0.0',
  `ipv42` varchar(255) DEFAULT '0.0.0.0',
  `ipv43` varchar(255) DEFAULT '0.0.0.0',
  `ipv61` varchar(255) DEFAULT 'FEC0:0000:0000:0000:0000:0000:0000:0001',
  `ipv62` varchar(255) DEFAULT 'FEC0:0000:0000:0000:0000:0000:0000:0001',
  `ipv63` varchar(255) DEFAULT 'FEC0:0000:0000:0000:0000:0000:0000:0001',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
```  
`quit`

Use the following command in terminal:  
`sudo /etc/init.d/mysql restart`  

----
Install BOT Dependencies
----
`sudo apt update`  
`sudo apt install python3.6`  

upload bot files then use the following commands:
`sudo pip3 install -r dependencies.txt`  
`curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -`  
`sudo apt-get install -y nodejs`  
`sudo apt-get install -y build-essential`  
`sudo npm i -g npm`  
`sudo npm install pm2`  

----
Bot Settings
---
open credentials.json and fill everything.
```
  "DISCORD_TOKEN": "Your Bot Token",
  "PREFIX": "!",
  "SITE": "https://yoursite.com", // take care don't add trailing slash "/" at the end.
  "SERVERID": 000000000000000000, // Your server ID
  "ROLEID": 000000000000000000, // NotVerified role ID from your SERVER
  "BOT_OWNER_ID": 000000000000000000, //fill with your id
  "mysql_ip": "localhost", //let it localhost, we just installed mysql.
  "mysql_username": "siteusername", //fill with your mysql username
  "mysql_password": "sitepassword" //fill with your mysql password
```
also if you want to enable ip ban change `"allowipban": false` to `"allowipban": true`  

Now login to your webserver and make sure you have mysqli enabled.  
Upload WebFiles, go to include folder and edit config.inc.php  
if everything is set run the bot and test it using:  
`sh start.sh`




 
