#!/bin/sh
echo ""
cd "$root"
pip3 install --upgrade pip &
pip3 install -r dependencies.txt &
clear
clear
sleep 3
clear
echo "Check Bot Status on Discord"
python3.6 bot.py
