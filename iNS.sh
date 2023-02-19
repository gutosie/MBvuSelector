#!/bin/sh
#
#skrypt instaluje neoscript
#
if `grep -q 'osd.language=pl_PL' </etc/enigma2/settings`; then
  PL=1
fi
if [ -f /etc/apt/apt.conf ] ; then
    STATUS='/var/lib/dpkg/status'
    OS='DreamOS'
elif [ -f /etc/opkg/opkg.conf ] ; then
   STATUS='/var/lib/opkg/status'
   OS='Opensource'
fi
#
    [ -e /tmp/MBvuSelector.zip ] && rm -f /tmp/MBvuSelector.zip
    [ -e /tmp/MBvuSelector-main ] && rm -rf /tmp/MBvuSelector-main
    echo ""
    echo "M U L T I B O O T   S E L E C T O R"
    echo ""
    [ $PL ] && echo "Pobieranie archiwum..." || echo "Downloading archive file..."
    echo "*****************************************************"
    URL='https://github.com/gutosie/MBvuSelector/archive/refs/heads/main.zip'
    Cel="/usr/lib/enigma2/python/Plugins/Extensions"
    MVmain="mv -f /tmp/main.zip /tmp/MBvuSelector.zip"
    cd /tmp/    

    #pobieranie i instalowanie
    if [ -f /usr/bin/curl ] ; then    
        curl -kLs $URL -o /tmp/MBvuSelector.zip
    fi
    if [ ! -e /tmp/MBvuSelector.zip ] ; then
        if [ -f /usr/bin/wget ]; then 
           wget --no-check-certificate $URL  
           $MVmain
        fi
    fi
    if [ ! -e /tmp/neoscript.zip ] ; then    
        if [ -f /usr/bin/fullwget ]; then 
           fullwget --no-check-certificate $URL  
           $MVmain
        fi           
    fi    
  
    if [ ! -e /tmp/MBvuSelector.zip ]; then
                [ $PL ] && echo "Nie pobrano pliku instalacyjnego" || echo "Installation file not downloaded"
                [ $PL ] && echo "Instalacja wtyczki zatrzymana" || echo "Plugin failed to install"
    else    
        unzip -qn ./MBvuSelector.zip
        rm -f /tmp/MBvuSelector.zip
        [ -e /tmp/main.zip ] && rm -rf /tmp/main.zip

        #kopiowanie
        [ $PL ] && echo "Instalowanie..." || echo "Instaling..."
        echo "*****************************************************"
        [ -e $Cel/MBvu ] && rm -rf $Cel/MBvu/* || mkdir -p $Cel/MBvu

        mv -f /tmp/MBvuSelector-main/MBvu/* $Cel/MBvu
        [ -e /tmp/MBvuSelector-main ] && rm -rf /tmp/MBvuSelector-main

        if [ $PL ] ; then
          echo ""
          echo "#####################################################"
          echo "#       SELECTOR MULTIBOOT ZAINSTALOWANY            #"
          echo "#####################################################"
          echo ""
        else
          echo ""
          echo "#####################################################"
          echo "#   >>> MBvu Selector INSTALLED SUCCESSFULLY <<<        #"
          echo "#####################################################"
          echo ""
        fi
        echo "*******************************************************"
        echo "                 MBvu Selector                     "    
        echo "          ----- Restart Enigma2 GUI -----              "
        echo "*******************************************************"
        sleep 2
        if [ $OS = 'DreamOS' ]; then 
            systemctl restart enigma2
        else
            killall -9 enigma2
        fi
    fi
cd /    
exit 0
