#!/bin/sh
#script by gutosie
UUIDSD=$(cat /tmp/slotsx/sdXY)
dirscripts=/usr/lib/enigma2/python/Plugins/Extensions/MBvu/script
namber='4' || '5' || '6' || '7' || '8' || '9' || '10' || '11' || '12' || '13' || '14' || '15' || '16' || '17' || '18' || '19' || '20'
MODEL=$(cat /proc/stb/info/vumodel)
   
echo "*****************************************************"
if `grep -q 'osd.language=pl_PL' </etc/enigma2/settings`; then
  PL=1
fi
if [ -f /media/hdd/STARTUP ] && [ -f /media/usb/STARTUP ]  ; then
    [ $PL ] && echo "Wykryto plik STARTUP w lokalizacji HDD i USB" || echo "STARTUP file detected in HDD and USB location"
    [ $PL ] && echo "Usun plik STARTUP  z HDD lub USB" || echo "Delete the file STARTUP from hdd or usb"
    echo "Installation error !"
    echo "*****************************************************"
    sleep 8
    break;
else    
    if [ -f /media/hdd/STARTUP ] ; then
        LocationImg=/media/hdd
    elif [ -f /media/usb/STARTUP ] ; then    
        LocationImg=/media/usb
    else
        LocationImg=/media/hdd   
    fi
    
    if [ -f ${dirscripts}/_20 ] && [ -f /STARTUP_RECOVERY ]  ; then            
            echo " "
            echo "Solt4 >>>";
            if [ -f /STARTUP ] ; then
                    sleep 1
            fi
            
            echo "kernel=${MODEL}/linuxrootfs4/zImage root=UUID=${UUIDSD} rootsubdir=$MODEL/linuxrootfs4 rootwait=40" > /boot/STARTUP_4 
            echo "kernel=${MODEL}/linuxrootfs5/zImage root=UUID=${UUIDSD} rootsubdir=$MODEL/linuxrootfs5 rootwait=40" > /boot/STARTUP_5 
            echo "kernel=${MODEL}/linuxrootfs6/zImage root=UUID=${UUIDSD} rootsubdir=$MODEL/linuxrootfs6 rootwait=40" > /boot/STARTUP_6 
            echo "kernel=${MODEL}/linuxrootfs7/zImage root=UUID=${UUIDSD} rootsubdir=$MODEL/linuxrootfs7 rootwait=40" > /boot/STARTUP_7 
            echo "kernel=${MODEL}/linuxrootfs8/zImage root=UUID=${UUIDSD} rootsubdir=$MODEL/linuxrootfs8 rootwait=40" > /boot/STARTUP_8 
            echo "kernel=${MODEL}/linuxrootfs9/zImage root=UUID=${UUIDSD} rootsubdir=$MODEL/linuxrootfs9 rootwait=40" > /boot/STARTUP_9
#ponizszych slots, za slot9, nie ma potrzeby dodawac
            #echo "kernel=${MODEL}/linuxrootfs10/zImage root=UUID=$${UUIDSD} rootsubdir=${MODEL}/linuxrootfs10 rootwait=40" > /boot/STARTUP_10
            #echo "kernel=${MODEL}/linuxrootfs11/zImage root=UUID=$${UUIDSD} rootsubdir=${MODEL}/linuxrootfs11 rootwait=40" > /boot/STARTUP_11
            #echo "kernel=${MODEL}/linuxrootfs12/zImage root=UUID=$${UUIDSD} rootsubdir=${MODEL}/linuxrootfs12 rootwait=40" > /boot/STARTUP_12
            #echo "kernel=${MODEL}/linuxrootfs13/zImage root=UUID=$${UUIDSD} rootsubdir=${MODEL}/linuxrootfs13 rootwait=40" > /boot/STARTUP_13
            #echo "kernel=${MODEL}/linuxrootfs14/zImage root=UUID=$${UUIDSD} rootsubdir=${MODEL}/linuxrootfs14 rootwait=40" > /boot/STARTUP_14
            #echo "kernel=${MODEL}/linuxrootfs15/zImage root=UUID=$${UUIDSD} rootsubdir=${MODEL}/linuxrootfs15 rootwait=40" > /boot/STARTUP_15
            #echo "kernel=${MODEL}/linuxrootfs16/zImage root=UUID=$${UUIDSD} rootsubdir=${MODEL}/linuxrootfs16 rootwait=40" > /boot/STARTUP_16
            #echo "kernel=${MODEL}/linuxrootfs17/zImage root=UUID=$${UUIDSD} rootsubdir=${MODEL}/linuxrootfs17 rootwait=40" > /boot/STARTUP_17
            #echo "kernel=${MODEL}/linuxrootfs18/zImage root=UUID=$${UUIDSD} rootsubdir=${MODEL}/linuxrootfs18 rootwait=40" > /boot/STARTUP_18
            #echo "kernel=${MODEL}/linuxrootfs19/zImage root=UUID=$${UUIDSD} rootsubdir=${MODEL}/linuxrootfs19 rootwait=40" > /boot/STARTUP_19
            #echo "kernel=${MODEL}/linuxrootfs20/zImage root=UUID=$${UUIDSD} rootsubdir=${MODEL}/linuxrootfs20 rootwait=40" > /boot/STARTUP_20

            if [ -f /STARTUP ] ; then
                    sleep 1
            fi
            echo "Slot20 <<<";
    fi
    if [ -f ${dirscripts}/_20 ] && [ ! -f ${dirscripts}/Slot20.sh ]  ; then        
            mv ${dirscripts}/4_ ${dirscripts}/4_Slot4.sh
            mv ${dirscripts}/5_ ${dirscripts}/5_Slot5.sh
            mv ${dirscripts}/6_ ${dirscripts}/6_Slot6.sh
            mv ${dirscripts}/7_ ${dirscripts}/7_Slot7.sh
            mv ${dirscripts}/8_ ${dirscripts}/8_Slot8.sh
            mv ${dirscripts}/9_ ${dirscripts}/9_Slot9.sh
            mv ${dirscripts}/_10 ${dirscripts}/Slot10.sh
            mv ${dirscripts}/_11 ${dirscripts}/Slot11.sh
            mv ${dirscripts}/_12 ${dirscripts}/Slot12.sh
            mv ${dirscripts}/_13 ${dirscripts}/Slot13.sh
            mv ${dirscripts}/_14 ${dirscripts}/Slot14.sh
            mv ${dirscripts}/_15 ${dirscripts}/Slot15.sh
            mv ${dirscripts}/_16 ${dirscripts}/Slot16.sh
            mv ${dirscripts}/_17 ${dirscripts}/Slot17.sh
            mv ${dirscripts}/_18 ${dirscripts}/Slot18.sh
            mv ${dirscripts}/_19 ${dirscripts}/Slot19.sh
            mv ${dirscripts}/_20 ${dirscripts}/Slot20.sh
            #touch ${LocationImg}/STARTUP
            echo " "
            if [ -f /STARTUP ] ; then
                    sleep 1
                    fi
                    [ $PL ] && echo "Dodano dodatkowo 4<->20 Slot." || echo "Added 4<->20 Slots."
                    [ $PL ] && echo "Dodatkowe sloty dla dysku SSD lub HDD." || echo "Slots for SSD or HDD hard drive."
                    [ $PL ] && echo "Poprawne motowanie sda1 to hdd." || echo "Mount sda1 to hdd."
                    [ $PL ] && echo "Restart interfejsu E2 za 8 sek... " || echo "Restart E2 8 sec..."
                    if [ -f /STARTUP ] ; then
                            sleep 8
                    fi
                    echo " "
                    echo "*****************************************************"
                    rm -r /tmp/slotsx
                    killall -9 enigma2;  
    else
                    [ $PL ] && echo "Dodatkowe slot 4 -> 20 dodane." || echo "Slots 4 -> 20 exist."
                    echo "*****************************************************"
    fi
fi 
exit 0
