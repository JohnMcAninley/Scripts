#!/bin/sh

LOGFILE=/home/pi/Scripts/reconnect.log

if ! ifconfig wlan0 | grep -q "inet"; then
	echo "$(date) : wlan0 down. attempting reconnection" >> $LOGFILE
	sudo systemctl restart dhcpcd
else
	echo "$(date) : wlan0 OK." >> $LOGFILE
fi
