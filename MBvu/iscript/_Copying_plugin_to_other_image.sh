#!/bin/sh
#script by gutosie
echo "*****************************************************"
MODEL=$(cat /proc/stb/info/vumodel)
PluginMB='/usr/lib/enigma2/python/Plugins/Extensions/MBvu'
OutDir='/usr/lib/enigma2/python/Plugins/Extensions/'
namber='4' || '5' || '6' || '7' || '8' || '9' || '10'
if [ -f /media/hdd/STARTUP ] && [ -f /media/hdd/${MODEL}/linuxrootfs${namber}/zImage ]  ; then
    LocationImg=/media/hdd
elif [ -f /media/usb/STARTUP ] && [ -f /media/usb/${MODEL}/linuxrootfs${namber}/zImage ]  ; then    
    LocationImg=/media/usb
fi
if `grep -q 'osd.language=pl_PL' </etc/enigma2/settings`; then
  PL=1
fi
if [ -f /STARTUP ] && [ -f /STARTUP_RECOVERY ]   ; then
    #SLOT1
    if [ -f /boot/linuxrootfs1/zImage ]  ; then
        rm -r /boot/linuxrootfs1/${PluginMB} > /dev/null 2>&1
        sleep 1 
        cp -af ${PluginMB} /boot/linuxrootfs1/${OutDir}
        [ $PL ] && echo "Slot1 Plugin zainstalowany." || echo "Slots1 plugin install."
    fi
    #SLOT2
    if [ -f /boot/linuxrootfs2/zImage ]  ; then
        rm -r /boot/linuxrootfs2/${PluginMB} > /dev/null 2>&1
        sleep 1 
        cp -af ${PluginMB} /boot/linuxrootfs2/${OutDir}
        [ $PL ] && echo "Slot2 Plugin zainstalowany." || echo "Slot2 plugin install."
    fi
    #SLOT3
    if [ -f /boot/linuxrootfs3/zImage ]  ; then
        rm -r /boot/linuxrootfs3/${PluginMB} > /dev/null 2>&1
        sleep 1 
        cp -af ${PluginMB} /boot/linuxrootfs3/${OutDir}
        [ $PL ] && echo "Slot3 Plugin zainstalowany." || echo "Slot3 plugin install."
    fi
    #SLOT4                                                                             
    if [ -f ${LocationImg}/${MODEL}/linuxrootfs4/zImage ]  ; then
        rm -r ${LocationImg}/${MODEL}/linuxrootfs4/${PluginMB} > /dev/null 2>&1
        sleep 1 
        cp -af ${PluginMB} ${LocationImg}/${MODEL}/linuxrootfs4/${OutDir}         
        [ $PL ] && echo "Slot4 Plugin zainstalowany." || echo "Slot4 plugin install." 
    fi 
    #SLOT5
    if [ -f ${LocationImg}/${MODEL}/linuxrootfs5/zImage ]  ; then
        rm -r ${LocationImg}/${MODEL}/linuxrootfs5/${PluginMB} > /dev/null 2>&1
        sleep 1
        cp -af ${PluginMB} ${LocationImg}/${MODEL}/linuxrootfs5/${OutDir}
        [ $PL ] && echo "Slot5 Plugin zainstalowany." || echo "Slot5 plugin install." 
    fi 
    #SLOT6
    if [ -f ${LocationImg}/${MODEL}/linuxrootfs6/zImage ]  ; then
        rm -r ${LocationImg}/${MODEL}/linuxrootfs6/${PluginMB} > /dev/null 2>&1
        sleep 1
        cp -af ${PluginMB} ${LocationImg}/${MODEL}/linuxrootfs6/${OutDir}
        [ $PL ] && echo "Slot6 Plugin zainstalowany." || echo "Slot6 plugin install." 
    fi 
    #SLOT7    
    if [ -f ${LocationImg}/${MODEL}/linuxrootfs7/zImage ]  ; then
        rm -r ${LocationImg}/${MODEL}/linuxrootfs7/${PluginMB}  > /dev/null 2>&1
        sleep 1
        cp -af ${PluginMB} ${LocationImg}/${MODEL}/linuxrootfs7/${OutDir}
        [ $PL ] && echo "Slot7 Plugin zainstalowany." || echo "Slot7 plugin install." 
    fi
    #SLOT8    
    if [ -f ${LocationImg}/${MODEL}/linuxrootfs8/zImage ]  ; then
        rm -r ${LocationImg}/${MODEL}/linuxrootfs8/${PluginMB} > /dev/null 2>&1
        sleep 1
        cp -af ${PluginMB} ${LocationImg}/${MODEL}/linuxrootfs8/${OutDir}
        [ $PL ] && echo "Slot8 Plugin zainstalowany." || echo "Slot8 plugin install." 
    fi
    #SLOT9    
    if [ -f ${LocationImg}/${MODEL}/linuxrootfs9/zImage ]  ; then
        rm -r ${LocationImg}/${MODEL}/linuxrootfs9/${PluginMB} > /dev/null 2>&1
        sleep 1
        cp -af ${PluginMB} ${LocationImg}/${MODEL}/linuxrootfs9/${OutDir}
        [ $PL ] && echo "Slot9 Plugin zainstalowany." || echo "Slot9 plugin install." 
    fi
    #SLOT10    
    if [ -f ${LocationImg}/${MODEL}/linuxrootfs10/zImage ]  ; then
        rm -r ${LocationImg}/${MODEL}/linuxrootfs10/${PluginMB} > /dev/null 2>&1
        sleep 1
        cp -af ${PluginMB} ${LocationImg}/${MODEL}/linuxrootfs10/${OutDir}
        [ $PL ] && echo "Slot10 Plugin zainstalowany." || echo "Slot10 plugin install." 
    fi
    #SLOT11    
    if [ -f ${LocationImg}/${MODEL}/linuxrootfs11/zImage ]  ; then
        rm -r ${LocationImg}/${MODEL}/linuxrootfs11/${PluginMB} > /dev/null 2>&1
        sleep 1
        cp -af ${PluginMB} ${LocationImg}/${MODEL}/linuxrootfs11/${OutDir}
        [ $PL ] && echo "Slot11 Plugin zainstalowany." || echo "Slot11 plugin install." 
    fi
    #SLOT12    
    if [ -f ${LocationImg}/${MODEL}/linuxrootfs12/zImage ]  ; then
        rm -r ${LocationImg}/${MODEL}/linuxrootfs12/${PluginMB} > /dev/null 2>&1
        sleep 1
        cp -af ${PluginMB} ${LocationImg}/${MODEL}/linuxrootfs12/${OutDir}
        [ $PL ] && echo "Slot12 Plugin zainstalowany." || echo "Slot12 plugin install." 
    fi
    #SLOT13    
    if [ -f ${LocationImg}/${MODEL}/linuxrootfs13/zImage ]  ; then
        rm -r ${LocationImg}/${MODEL}/linuxrootfs13/${PluginMB} > /dev/null 2>&1
        sleep 1
        cp -af ${PluginMB} ${LocationImg}/${MODEL}/linuxrootfs13/${OutDir}
        [ $PL ] && echo "Slot13 Plugin zainstalowany." || echo "Slot13 plugin install." 
    fi
    #SLOT14    
    if [ -f ${LocationImg}/${MODEL}/linuxrootfs14/zImage ]  ; then
        rm -r ${LocationImg}/${MODEL}/linuxrootfs14/${PluginMB} > /dev/null 2>&1
        sleep 1
        cp -af ${PluginMB} ${LocationImg}/${MODEL}/linuxrootfs14/${OutDir}
        [ $PL ] && echo "Slot14 Plugin zainstalowany." || echo "Slot14 plugin install." 
    fi
    #SLOT15    
    if [ -f ${LocationImg}/${MODEL}/linuxrootfs15/zImage ]  ; then
        rm -r ${LocationImg}/${MODEL}/linuxrootfs15/${PluginMB} > /dev/null 2>&1
        sleep 1
        cp -af ${PluginMB} ${LocationImg}/${MODEL}/linuxrootfs15/${OutDir}
        [ $PL ] && echo "Slot15 Plugin zainstalowany." || echo "Slot15 plugin install." 
    fi
    #SLOT16    
    if [ -f ${LocationImg}/${MODEL}/linuxrootfs16/zImage ]  ; then
        rm -r ${LocationImg}/${MODEL}/linuxrootfs16/${PluginMB} > /dev/null 2>&1
        sleep 1
        cp -af ${PluginMB} ${LocationImg}/${MODEL}/linuxrootfs16/${OutDir}
        [ $PL ] && echo "Slot16 Plugin zainstalowany." || echo "Slot16 plugin install." 
    fi
    #SLOT17    
    if [ -f ${LocationImg}/${MODEL}/linuxrootfs17/zImage ]  ; then
        rm -r ${LocationImg}/${MODEL}/linuxrootfs17/${PluginMB} > /dev/null 2>&1
        sleep 1
        cp -af ${PluginMB} ${LocationImg}/${MODEL}/linuxrootfs17/${OutDir}
        [ $PL ] && echo "Slot17 Plugin zainstalowany." || echo "Slot17 plugin install." 
    fi
    #SLOT18    
    if [ -f ${LocationImg}/${MODEL}/linuxrootfs18/zImage ]  ; then
        rm -r ${LocationImg}/${MODEL}/linuxrootfs18/${PluginMB} > /dev/null 2>&1
        sleep 1
        cp -af ${PluginMB} ${LocationImg}/${MODEL}/linuxrootfs18/${OutDir}
        [ $PL ] && echo "Slot18 Plugin zainstalowany." || echo "Slot18 plugin install." 
    fi
    #SLOT19   
    if [ -f ${LocationImg}/${MODEL}/linuxrootfs19/zImage ]  ; then
        rm -r ${LocationImg}/${MODEL}/linuxrootfs19/${PluginMB} > /dev/null 2>&1
        sleep 1
        cp -af ${PluginMB} ${LocationImg}/${MODEL}/linuxrootfs19/${OutDir}
        [ $PL ] && echo "Slot19 Plugin zainstalowany." || echo "Slot19 plugin install." 
    fi
    #SLOT20    
    if [ -f ${LocationImg}/${MODEL}/linuxrootfs20/zImage ]  ; then
        rm -r ${LocationImg}/${MODEL}/linuxrootfs20/${PluginMB} > /dev/null 2>&1
        sleep 1
        cp -af ${PluginMB} ${LocationImg}/${MODEL}/linuxrootfs20/${OutDir}
        [ $PL ] && echo "Slot20 Plugin zainstalowany." || echo "Slot20 plugin install." 
    fi
else
    [ $PL ] && echo "Opcja dostepna tylko z poziomu Slot0 Recovery" || echo "Option available only from Slot0 Recovery"
fi
echo "*****************************************************"
exit 0
