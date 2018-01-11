#!/bin/bash
#
# Start the webserver.
#
WsBase=/home/sms/logs/sms-3001
PidFile=$WsBase.pid
if [ -f $PidFile ] ; then
    Pid=$(cat $PidFile)
    if kill -0 $Pid 2>&1 >/dev/null ; then
	echo "ERROR: webserver is already running, PID=$Pid"
	exit 1
    else
	# The process does not exist, remove the pid file.
	rm -f $PidFile
    fi
fi
python2.7 sms.py -p 3001 -l warning --no-dirlist -r /home/sms/www -d /home/sms/logs
echo "started"
