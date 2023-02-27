#!/bin/sh
echo "*****************************************************"
if `grep -q 'osd.language=pl_PL' </etc/enigma2/settings`; then
  PL=1
fi
if [ -f /boot/STARTUP_RECOVERY ] && [ -f /boot/linuxrootfs1/zImage ] ; then
    sleep 1
    cp -af /boot/STARTUP_1 /boot/STARTUP
    [ $PL ] && echo "Restart systemu !" || echo "Reboot system !"
    echo " ";
    echo "*****************************************************";
    sleep 2
    /etc/init.d/reboot    
else
    [ $PL ] && echo "Slot 1 jest pusty !" || echo "Slot 1 is empty !"
    echo " "
fi
exit 0
