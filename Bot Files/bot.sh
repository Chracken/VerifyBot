#!/bin/sh
echo ""
cd "$root"
pip3 install --upgrade pip &
pip3 install -r dependencies.txt &
sleep 3
clear
python3.6 bot.py &
exit 0