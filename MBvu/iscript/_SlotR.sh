#!/bin/sh
echo "*****************************************************"
echo "Start up Slot0 RECOVERY" 
if `grep -q 'osd.language=pl_PL' </etc/enigma2/settings`; then
  PL=1
fi
sleep 1
if [ -f /boot/STARTUP_RECOVERY ] ; then
    sleep 1
    cp -af /boot/STARTUP_RECOVERY /boot/STARTUP
    [ $PL ] && echo "Restart systemu !" || echo "Reboot system !"
    echo " ";
    echo "*****************************************************";
    sleep 2
    /etc/init.d/reboot       
else
    [ $PL ] && echo "Nie ma pliku STARTUP !" || echo "STARTUP not found !"
    echo " "
fi 
exit 0
