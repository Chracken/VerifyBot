# VerifyBot  
Verify System for Discord servers made with Python, MySQL and PHP.  
How it works?  
When someone joins your server they will get a validation link from bot on DM  
When they start Validation Process, their unique browser id will be sent in database (Also Their IP if you want to use IP BAN SYSTEM by default it is disabled).  
So! When you ban someone using verifybot that person will be banned on browser id (or/and ip if you enable that feature).  
Validation url don't allow proxy servers, vpn clients or incognito mode!  
Sometimes it can be accessed using chrome incognito but don't bother too much they will be recognized by the bot anyway  

#Requirements
Ubuntu 16.04 server or any other linux, just adapt!  
WebServer with php5.0+ and mysqli enabled.  

#Commands  
`!verify <code>` - With this you get verified using your code!  
`!ban @mention reason` - ban someone with or without reason  
`!unban name#0000` - unban someone  
`!unbandb id` - unban someoone by discord id (use it only if you already unbanned someone using another bot or by hand, if you don't use it the bot will still ban that person).  
`!setup` - sets notverified role to all channels!

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
!!remember to change `siteusername` with any username and `sitepassword` with any password  
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

Download the following archive on your pc: https://github.com/Chracken/VerifyBot/archive/main.zip  
upload the content from Bot Files folder in your root then use the following commands:  
`sudo pip3 install -r dependencies.txt`  
`curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -`  
`sudo apt-get install -y nodejs`  
`sudo apt-get install -y build-essential`  
`sudo npm i -g npm`  
`sudo npm install pm2`  

----
Bot Settings
---
1. go to https://discord.com/developers/applications  
2. click on New Application , give it a name: ex: VerifyBot then click create  
3. go to Bot section then click on Add Bot  
4. copy your token somewhere safe or add it directly to credentials.json
5. open your server settings -> roles -> create a new role called NotVerified, right click on that role and copy role id into credentials.json file.
6. go to your application and get the client id from general information , edit the following link with your client id to invite verifybot on your server  
`https://discord.com/oauth2/authorize?client_id=`client-id-here`&scope=bot&permissions=469839031`

open credentials.json and fill everything.
```
  "DISCORD_TOKEN": "Your Bot Token",
  "PREFIX": "!",
  "SITE": "https://yoursite.com", // site location where you uploaded web files, take care don't add trailing slash "/" at the end.
  "SERVERID": 000000000000000000, // Your server ID
  "ROLEID": 000000000000000000, // NotVerified role ID from your SERVER
  "BOT_OWNER_ID": 000000000000000000, //fill with your id
  "mysql_ip": "localhost", //let it localhost, we just installed mysql.
  "mysql_username": "siteusername", //fill with your mysql username
  "mysql_password": "sitepassword" //fill with your mysql password
```
also if you want to enable ip ban change `"allowipban": false` to `"allowipban": true`  

Now login to your webserver and make sure you have mysqli enabled.  
Upload Web Files, go to include folder and edit config.inc.php  
if everything is set run the bot and test it using:  
`sh start.sh`

How to use pm2?  
`pm2 list` - shows you a list with all pm2 processes  
`pm2 stop id` - stop some process from pm2 list by id  
`pm2 kill` - stop all pm2 processes  
`pm2 logs` - shows logs about all processes in real time! Use it to see VerifyBot activity.




 
