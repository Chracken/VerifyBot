#!/bin/sh
root=$(pwd)

	echo ""
	cd "$root"
	echo "Starting VerifyBot with auto-restart"
	sudo pm2 start "$root/bot.sh" --interpreter=bash --name=VerifyBot
	sudo pm2 startup
	sudo pm2 save

exit 0
