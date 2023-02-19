#!/usr/bin/python
# -*- coding: utf-8 -*-
## Multiboot Image Selector VU+
## Script by gutosie
import sys
import os
from Tools.Directories import fileExists, SCOPE_PLUGINS

dirMB='/usr/lib/enigma2/python/Plugins/Extensions/MBvu'
dirscripts='/usr/lib/enigma2/python/Plugins/Extensions/MBvu/script'
dirIscripts='/usr/lib/enigma2/python/Plugins/Extensions/MBvu/iscript'
namber='4' or '5' or '6' or '7' or '8' or '9' or '10' or '11' or '12' or '13' or '14' or '15' or '16' or '17' or '18' or '19' or '20' #itd.. add
namberout = '10' or '11' or '12' or '13' or '14' or '15' or '16' or '17' or '18' or '19' or '20' 

def getROOT():
    try:
        if os.path.exists('/tmp/linuxrootfs'):
            with open('/tmp/linuxrootfs', 'r') as f:
                myboxEXT = f.readline().strip()
                f.close()
        return myboxEXT 
    except:
        pass

def getUnknownImage():
                    if fileExists('/boot/'+getROOT()+'/etc/issue'):
                        imageteam = 'Unknown-image'
                    if fileExists(''+getHddOrUsb()+'/'+getROOT()+'/etc/issue'):
                        imageteam = 'Unknown-image'
  
                    else:
                        imageteam ='empty_Slot'
                    return imageteam                          

#Image Recovery Slot0
def getImageTeam0():
        imageteam = '_RECOVERY_Slot0'
        if fileExists('/usr/lib/enigma2/python/boxbranding.so') and fileExists('/STARTUP'):
            from boxbranding import getImageDistro
            imagedistro = getImageDistro()
            return imagedistro
        elif fileExists("/boot/etc/issue") and fileExists('/boot/STARTUP'):
            for line in open("/boot/etc/issue"):
                if "openbh" in line:
                    imageteam = 'OpenBH'          
        return imageteam
        
def getCurrent():
    try:
        slot0 = ""
        if fileExists('/boot/STARTUP'):
            with open('/boot/STARTUP', 'r') as f:
                lines = f.read()
                f.close()
            if lines.find('linuxrootfs0') != -1:
                if GetTranslator() == 'pl_PL':
                    slot0 = '---[Aktualny]'
                else:
                    slot0 = '____'+GetTranslator()+''
                    
        return slot0
    except:
        pass

#Images Slots
def getIMGmb():
        imageteam = getUnknownImage()
        if fileExists('/boot/'+getROOT()+'/etc/issue'):
            for line in open('/boot/'+getROOT()+'/etc/issue'):     
                if "openbh" in line:
                    imageteam = 'OpenBH'
                elif "openspa" in line:
                    imageteam = 'OpenSPA'
                elif "egami" in line:
                    imageteam = 'EGAMI'
                elif "openvix" in line:
                    imageteam = 'OpenVix'
                elif "openatv" in line:
                    imageteam = 'openATV'
                elif "cobraliberosa" in line:
                    imageteam = 'Cobraliberosat'
                elif "openvision" in line:
                    imageteam = 'OpenVision'
                elif "opendroid" in line:
                    imageteam = 'OpenDroid'
                elif "openpli" in line:
                    imageteam = 'OpenPLi'
                elif "pure2" in line:
                    imageteam = 'PurE2'
                elif "Nonsolosat" in line:
                    imageteam = 'Nonsolosat'
                elif "rudream" in line:
                    imageteam = 'Rudream'
                elif "satdreamgr" in line:
                    imageteam = 'SatdreamGR'
                elif "opentr" in line:
                    imageteam = 'OpenTR'
                elif "openesi" in line:
                    imageteam = 'OpenESI'                    
                elif "openesi" in line:
                    imageteam = 'OpenESI'
                elif "openbox" in line:
                    imageteam = 'openBOX'
                elif "opendonki" in line:
                    imageteam = 'OpenDonki'
                elif "openplus" in line:
                    imageteam = 'OpenPlus'
                elif "openld" in line:
                    imageteam = 'OpenLD'
                elif "opennfr" in line:
                    imageteam = 'OpenNFR'
                elif "openten" in line:
                    imageteam = 'OpenTEN'
                elif "PKTeam" in line or "Hyperion" in line :
                    imageteam = 'PKTeamHyperion'
                elif fileExists('/boot/'+getROOT()+'/etc/vtiversion.info'):
                    imageteam = 'VTiTeam'
                elif fileExists('/boot/'+getROOT()+'/etc/bhversion'):
                    for line in open('/boot/'+getROOT()+'/etc/bhversion'):
                        if "BlackHole" in line:
                            imageteam = 'BlackHole'
                elif "vuplus" in line:
                    imageteam = 'VuPlus'
                                              
        return imageteam
        
def getCurrentToNine():
    try:
        slotX = ""
        if fileExists('/boot/STARTUP'):
            with open('/boot/STARTUP', 'r') as f:
                lines = f.read()
                f.close()
            if lines.find(''+getROOT()+'') != -1 and not lines.find(''+namberout+'') :
                if GetTranslator() == 'pl_PL':
                    slotX = '---[Aktualny]'
                else:
                    slotX = '____'+GetTranslator()+''
        return slotX
    except:
        pass
        
def getCurrentAfterNine():
    try:
        slotX = ""
        if fileExists('/boot/STARTUP'):
            with open('/boot/STARTUP', 'r') as f:
                lines = f.read()
                f.close()
            if lines.find(''+getROOT()+'') != -1 and lines.find(''+namberout+'') :
                if GetTranslator() == 'pl_PL':
                    slotX = '---[Aktualny]'
                else:
                    slotX = '____'+GetTranslator()+''
        return slotX
    except:
        pass

def getIMGmbHddUsb():
        imageteam = getUnknownImage()
        if fileExists(''+getHddOrUsb()+'/'+getROOT()+'/etc/issue'):
            for line in open(''+getHddOrUsb()+'/'+getROOT()+'/etc/issue'):
                if "openbh" in line:
                    imageteam = 'OpenBH'
                elif "openspa" in line:
                    imageteam = 'OpenSPA'
                elif "egami" in line:
                    imageteam = 'EGAMI'
                elif "openvix" in line:
                    imageteam = 'OpenVix'
                elif "openatv" in line:
                    imageteam = 'openATV'
                elif "cobraliberosa" in line:
                    imageteam = 'Cobraliberosat'
                elif "openvision" in line:
                    imageteam = 'OpenVision'
                elif "opendroid" in line:
                    imageteam = 'OpenDroid'
                elif "openpli" in line:
                    imageteam = 'OpenPLi'
                elif "pure2" in line:
                    imageteam = 'PurE2'
                elif "Nonsolosat" in line:
                    imageteam = 'Nonsolosat'
                elif "rudream" in line:
                    imageteam = 'Rudream'
                elif "satdreamgr" in line:
                    imageteam = 'SatdreamGR'
                elif "opentr" in line:
                    imageteam = 'OpenTR'
                elif "openesi" in line:
                    imageteam = 'OpenESI'                    
                elif "openesi" in line:
                    imageteam = 'OpenESI'
                elif "openbox" in line:
                    imageteam = 'openBOX'
                elif "opendonki" in line:
                    imageteam = 'OpenDonki'
                elif "openplus" in line:
                    imageteam = 'OpenPlus'
                elif "openld" in line:
                    imageteam = 'OpenLD'
                elif "opennfr" in line:
                    imageteam = 'OpenNFR'
                elif "openten" in line:
                    imageteam = 'OpenTEN'
                elif "PKTeam" in line or "Hyperion" in line :
                    imageteam = 'PKTeamHyperion'
                elif fileExists(''+getHddOrUsb()+'/'+getROOT()+'/etc/vtiversion.info'):
                    imageteam = 'VTiTeam'
                elif fileExists(''+getHddOrUsb()+'/'+getROOT()+'/etc/bhversion'):
                    for line in open(''+getHddOrUsb()+'/'+getROOT()+'/etc/bhversion'):
                        if "BlackHole" in line:
                            imageteam = 'BlackHole'
                elif "vuplus" in line:
                    imageteam = 'VuPlus'                      
        return imageteam 

def GetTranslator():
    imglang = ""
    usedlang = open('/etc/enigma2/settings', 'r')
    lang = 'config.osd.language=pl_PL'
    local = usedlang.read().find(lang)
    if local != -1:
        imglang = 'pl_PL'
    else:
        imglang = '---Current'
    return imglang

def getHddOrUsb():
    locatino = '/media/hdd'
    if fileExists('/media/hdd/STARTUP') and fileExists('/media/hdd/linuxrootfs'+namber+'/zImage'):
            locatino = '/media/hdd'
    elif fileExists('/media/usb/STARTUP') and fileExists('/media/usb/linuxrootfs'+namber+'/zImage'):
            locatino = '/media/usb'
    return locatino

def getMountDevices(): 
    if fileExists('/proc/mounts'):
        with open('/proc/mounts', 'r') as f:
            lines = f.read()
            f.close()
        if lines.find('/dev/sda1') != -1:
            if not fileExists('/media/hdd'):
                os.system('mkdir -p /media/hdd')
            os.system('mount /dev/sda1 /media/hdd')
        if lines.find('/dev/sdb1') != -1:
            if not fileExists('/media/usb'):
                os.system('mkdir -p /media/usb')
            os.system('mount /dev/sdb1 /media/usb')

def getMovNextIMG():
    if fileExists('/boot/linuxrootfs9/zImage'):
        os.system('mv -f /linuxrootfs9 '+getHddOrUsb()+'/linuxrootfs9; sleep 1; ')
    if fileExists(''+getHddOrUsb()+'/linuxrootfs9/zImage'):
        if not fileExists(''+getHddOrUsb()+'/linuxrootfs10/zImage'):
            os.system('mv -f '+getHddOrUsb()+'/linuxrootfs9 '+getHddOrUsb()+'/linuxrootfs10; sleep 1; echo "kernel=/linuxrootfs10/zImage root=/dev/sda1 rootsubdir=linuxrootfs10" > /boot/STARTUP; sleep 1 ')
        elif not fileExists(''+getHddOrUsb()+'/linuxrootfs11/zImage'):
            os.system('mv -f '+getHddOrUsb()+'/linuxrootfs9 '+getHddOrUsb()+'/linuxrootfs11; sleep 1; echo "kernel=/linuxrootfs11/zImage root=/dev/sda1 rootsubdir=linuxrootfs11" > /boot/STARTUP; sleep 1 ')
        elif not fileExists(''+getHddOrUsb()+'/linuxrootfs12/zImage'):
            os.system('mv -f '+getHddOrUsb()+'/linuxrootfs9 '+getHddOrUsb()+'/linuxrootfs12; sleep 1; echo "kernel=/linuxrootfs12/zImage root=/dev/sda1 rootsubdir=linuxrootfs12" > /boot/STARTUP; sleep 1 ')
        elif not fileExists(''+getHddOrUsb()+'/linuxrootfs13/zImage'):
            os.system('mv -f '+getHddOrUsb()+'/linuxrootfs9 '+getHddOrUsb()+'/linuxrootfs13; sleep 1; echo "kernel=/linuxrootfs13/zImage root=/dev/sda1 rootsubdir=linuxrootfs13" > /boot/STARTUP; sleep 1 ')
        elif not fileExists(''+getHddOrUsb()+'/linuxrootfs14/zImage'):
            os.system('mv -f '+getHddOrUsb()+'/linuxrootfs9 '+getHddOrUsb()+'/linuxrootfs14; sleep 1; echo "kernel=/linuxrootfs14/zImage root=/dev/sda1 rootsubdir=linuxrootfs14" > /boot/STARTUP; sleep 1 ')
        elif not fileExists(''+getHddOrUsb()+'/linuxrootfs15/zImage'):
            os.system('mv -f '+getHddOrUsb()+'/linuxrootfs9 '+getHddOrUsb()+'/linuxrootfs15; sleep 1; echo "kernel=/linuxrootfs15/zImage root=/dev/sda1 rootsubdir=linuxrootfs15" > /boot/STARTUP; sleep 1 ')
        elif not fileExists(''+getHddOrUsb()+'/linuxrootfs16/zImage'):
            os.system('mv -f '+getHddOrUsb()+'/linuxrootfs9 '+getHddOrUsb()+'/linuxrootfs16; sleep 1; echo "kernel=/linuxrootfs16/zImage root=/dev/sda1 rootsubdir=linuxrootfs16" > /boot/STARTUP; sleep 1 ')
        elif not fileExists(''+getHddOrUsb()+'/linuxrootfs17/zImage'):
            os.system('mv -f '+getHddOrUsb()+'/linuxrootfs9 '+getHddOrUsb()+'/linuxrootfs17; sleep 1; echo "kernel=/linuxrootfs17/zImage root=/dev/sda1 rootsubdir=linuxrootfs17" > /boot/STARTUP; sleep 1 ')
        elif not fileExists(''+getHddOrUsb()+'/linuxrootfs18/zImage'):
            os.system('mv -f '+getHddOrUsb()+'/linuxrootfs9 '+getHddOrUsb()+'/linuxrootfs18; sleep 1; echo "kernel=/linuxrootfs18/zImage root=/dev/sda1 rootsubdir=linuxrootfs18" > /boot/STARTUP; sleep 1 ')
        elif not fileExists(''+getHddOrUsb()+'/linuxrootfs19/zImage'):
            os.system('mv -f '+getHddOrUsb()+'/linuxrootfs9 '+getHddOrUsb()+'/linuxrootfs19; sleep 1; echo "kernel=/linuxrootfs19/zImage root=/dev/sda1 rootsubdir=linuxrootfs19" > /boot/STARTUP; sleep 1 ')
        elif not fileExists(''+getHddOrUsb()+'/linuxrootfs20/zImage'):
            os.system('mv -f '+getHddOrUsb()+'/linuxrootfs9 '+getHddOrUsb()+'/linuxrootfs20; sleep 1; echo "kernel=/linuxrootfs20/zImage root=/dev/sda1 rootsubdir=linuxrootfs20" > /boot/STARTUP; sleep 1 ')
        #elif not fileExists(''+getHddOrUsb()+'/linuxrootfs21/zImage'):
            #os.system('mv -f '+getHddOrUsb()+'/linuxrootfs9 '+getHddOrUsb()+'/linuxrootfs21; sleep 1; echo "kernel=/linuxrootfs21/zImage root=/dev/sda1 rootsubdir=linuxrootfs21" > /boot/STARTUP; sleep 1 ')
        #elif not fileExists(''+getHddOrUsb()+'/linuxrootfs22/zImage'):
            #os.system('mv -f '+getHddOrUsb()+'/linuxrootfs9 '+getHddOrUsb()+'/linuxrootfs22; sleep 1; echo "kernel=/linuxrootfs22/zImage root=/dev/sda1 rootsubdir=linuxrootfs22" > /boot/STARTUP; sleep 1 ')

#END script gutosie
