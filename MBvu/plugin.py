# -*- coding: utf-8 -*-
## Multiboot Image Selector VU+ALL
## Script by gutosie
##
from Components.ActionMap import ActionMap
from Components.MenuList import MenuList
from Components.Label import Label
from os import listdir
from Plugins.Plugin import PluginDescriptor
from Screens.Console import Console
from Screens.Screen import Screen
import os
import sys
from os import system 
from Tools.Directories import fileExists, SCOPE_PLUGINS
from Screens.MessageBox import MessageBox
from Plugins.Extensions.MBvu.getinfo import getIMGmb, getIMGmbHddUsb, getCurrent, getCurrentToNine, getCurrentAfterNine, dirMB, dirIscripts, dirscripts, namber, getMovNextIMG, getHddOrUsb, getMountDevices, GetTranslator, getImageTeam0, getResultMount

PLUGINVERSION=open('/usr/lib/enigma2/python/Plugins/Extensions/MBvu/mbvuver').read().strip().upper()           
autoupdateplug = 'https://raw.githubusercontent.com/gutosie/MBvuSelector/master/imbvuver;'
try:
    mbvuver=open('/tmp/imbvuver').read().strip().upper()
except:
    mbvuver=PLUGINVERSION



class ScriptNeo(Screen):
        skin = """
	<screen position="center,center" size="1060,625" title="Select SLOT Image       Plug ver.: %s">
            <widget name="list" itemHeight="44" font="Regular;35" position="center,center" zPosition="1" size="870,480" scrollbarMode="showOnDemand" transparent="1">
            <convert type="StringList" font="Regular;70" />
            </widget>
            <widget name="key_red" position="35,575" zPosition="2" size="510,40" font="Regular;30" halign="left" valign="center" backgroundColor="red" transparent="1" />
            <widget name="key_yellow" position="545,575" zPosition="2" size="510,40" font="Regular;30" halign="left" valign="center" backgroundColor="yellow" transparent="1" />
	</screen>"""% (_(''+PLUGINVERSION+''))

        def __init__(self, session, args=None):
                Screen.__init__(self, session)
                self.session = session
                self["list"] = MenuList([])
                if not fileExists('/boot/STARTUP_9') or fileExists(''+dirscripts+'/_20') or fileExists('/tmp/.ilabel') and fileExists('/media/hdd') :
                    self['key_red'] = Label(_('Press red - Add slots on HDD'))
                if not fileExists('/boot/STARTUP_9') or fileExists(''+dirscripts+'/_20') or fileExists('/tmp/.ilabel') and fileExists('/media/usb') :
                    self['key_yellow'] = Label(_('Press yellow - Add slots on USB'))
                self["actions"] = ActionMap(["OkCancelActions", "ColorActions"], {'red': self.hddslots,
                 'yellow': self.usbslots,
                 "ok": self.run, 
                 "cancel": self.close}, -1)
                self.onLayoutFinish.append(self.loadScriptList)


        if fileExists('/STARTUP_RECOVERY') and not fileExists('/boot/STARTUP_RECOVERY'): 
                os.system(' mount / /boot')
	
        if fileExists('/tmp/imbvuver'):
                        os.system('rm -r /tmp/imbvuve*')
        try:
                os.system('cd /tmp; wget -q --no-check-certificate '+autoupdateplug+'')
        except:
                os.system('cd /tmp; curl -O --ftp-ssl -k '+autoupdateplug+'')
		
        if fileExists(''+getHddOrUsb()+'/linuxrootfs9/zImage') or fileExists('/boot/linuxrootfs9/zImage') :
            getMovNextIMG()
        
        if not fileExists(''+getHddOrUsb()+'/linuxrootfs'+namber+'/'):
            getMountDevices()
            
        if fileExists(''+dirIscripts+'') and fileExists(''+dirscripts+'') :
                os.system('rm -r '+dirscripts+'/*.sh; sleep 2; mv '+dirIscripts+'/* '+dirscripts+'/; sleep 2  ')
        elif fileExists(''+dirIscripts+'') and not fileExists(''+dirscripts+''):
                os.system('mv -f '+dirIscripts+' '+dirscripts+'; sleep 2  ')
	
        os.system('echo "linuxrootfs0" > /tmp/linuxrootfs')       
        if GetTranslator() == 'pl_PL':
                os.system('mv -f ' + dirscripts + '/_SlotR*.sh ' + dirscripts + '/_SlotR-'+getImageTeam0()+'-Tryb_awaryjny%s.sh' % getCurrent() )
        else:
                os.system('mv -f ' + dirscripts + '/_SlotR*.sh ' + dirscripts + '/_SlotR-'+getImageTeam0()+'-Recovery%s.sh' % getCurrent() )
        os.system('echo "linuxrootfs1" > /tmp/linuxrootfs')
        os.system('mv -f ' + dirscripts + '/1_Slot1*.sh ' + dirscripts + '/1_Slot1-'+getIMGmb()+'%s.sh' % getCurrent() )
        os.system('echo "linuxrootfs2" > /tmp/linuxrootfs') 
        os.system('mv -f ' + dirscripts + '/2_Slot2*.sh ' + dirscripts + '/2_Slot2-' +getIMGmb()+ '%s.sh' % getCurrent() )
        os.system('echo "linuxrootfs3" > /tmp/linuxrootfs')
        os.system('mv -f ' + dirscripts + '/3_Slot3*.sh ' + dirscripts + '/3_Slot3-' + getIMGmb() + '%s.sh' %getCurrent() ) 
        if fileExists('/boot/STARTUP') :
            os.system('echo "linuxrootfs4" > /tmp/linuxrootfs')
            os.system('mv -f ' + dirscripts + '/4_Slot4*.sh ' + dirscripts + '/4_Slot4-' + getIMGmbHddUsb() + '%s.sh' % getCurrentToNine() )
            os.system('echo "linuxrootfs5" > /tmp/linuxrootfs')  
            os.system('mv -f ' + dirscripts + '/5_Slot5*.sh ' + dirscripts + '/5_Slot5-' + getIMGmbHddUsb() + '%s.sh' % getCurrentToNine() )
            os.system('echo "linuxrootfs6" > /tmp/linuxrootfs')
            os.system('mv -f ' + dirscripts + '/6_Slot6*.sh ' + dirscripts + '/6_Slot6-' + getIMGmbHddUsb() + '%s.sh' % getCurrentToNine() )
            os.system('echo "linuxrootfs7" > /tmp/linuxrootfs')
            os.system('mv -f ' + dirscripts + '/7_Slot7*.sh ' + dirscripts + '/7_Slot7-' + getIMGmbHddUsb() + '%s.sh' % getCurrentToNine() )
            os.system('echo "linuxrootfs8" > /tmp/linuxrootfs')
            os.system('mv -f ' + dirscripts + '/8_Slot8*.sh ' + dirscripts + '/8_Slot8-' + getIMGmbHddUsb() + '%s.sh' % getCurrentToNine() )
            os.system('echo "linuxrootfs9" > /tmp/linuxrootfs')
            os.system('mv -f ' + dirscripts + '/9_Slot9*.sh ' + dirscripts + '/9_Slot9-' + getIMGmbHddUsb() + '%s.sh' % getCurrentToNine() )
            os.system('echo "linuxrootfs10" > /tmp/linuxrootfs')
            os.system('mv -f ' + dirscripts + '/Slot10*.sh ' + dirscripts + '/Slot10-' + getIMGmbHddUsb() + '%s.sh' % getCurrentAfterNine() )
            os.system('echo "linuxrootfs11" > /tmp/linuxrootfs')
            os.system('mv -f ' + dirscripts + '/Slot11*.sh ' + dirscripts + '/Slot11-' + getIMGmbHddUsb() + '%s.sh' % getCurrentAfterNine() )
            os.system('echo "linuxrootfs12" > /tmp/linuxrootfs')
            os.system('mv -f ' + dirscripts + '/Slot12*.sh ' + dirscripts + '/Slot12-' + getIMGmbHddUsb() + '%s.sh' % getCurrentAfterNine() )
            os.system('echo "linuxrootfs13" > /tmp/linuxrootfs')
            os.system('mv -f ' + dirscripts + '/Slot13*.sh ' + dirscripts + '/Slot13-' + getIMGmbHddUsb() + '%s.sh' % getCurrentAfterNine() )
            os.system('echo "linuxrootfs14" > /tmp/linuxrootfs')
            os.system('mv -f ' + dirscripts + '/Slot14*.sh ' + dirscripts + '/Slot14-' + getIMGmbHddUsb() + '%s.sh' % getCurrentAfterNine() )
            os.system('echo "linuxrootfs15" > /tmp/linuxrootfs')
            os.system('mv -f ' + dirscripts + '/Slot15*.sh ' + dirscripts + '/Slot15-' + getIMGmbHddUsb() + '%s.sh' % getCurrentAfterNine() )
            os.system('echo "linuxrootfs16" > /tmp/linuxrootfs')
            os.system('mv -f ' + dirscripts + '/Slot16*.sh ' + dirscripts + '/Slot16-' + getIMGmbHddUsb() + '%s.sh' % getCurrentAfterNine() )
            os.system('echo "linuxrootfs17" > /tmp/linuxrootfs')
            os.system('mv -f ' + dirscripts + '/Slot17*.sh ' + dirscripts + '/Slot17-' + getIMGmbHddUsb() + '%s.sh' % getCurrentAfterNine() )
            os.system('echo "linuxrootfs18" > /tmp/linuxrootfs')
            os.system('mv -f ' + dirscripts + '/Slot18*.sh ' + dirscripts + '/Slot18-' + getIMGmbHddUsb() + '%s.sh' % getCurrentAfterNine() )
            os.system('echo "linuxrootfs19" > /tmp/linuxrootfs')
            os.system('mv -f ' + dirscripts + '/Slot19*.sh ' + dirscripts + '/Slot19-' + getIMGmbHddUsb() + '%s.sh' % getCurrentAfterNine() )
            os.system('echo "linuxrootfs20" > /tmp/linuxrootfs')
            os.system('mv -f ' + dirscripts + '/Slot20*.sh ' + dirscripts + '/Slot20-' + getIMGmbHddUsb() + '%s.sh' % getCurrentAfterNine() )  

        if fileExists(''+dirIscripts+''):
                os.system('sleep 2; rm -r '+dirIscripts+' ')
        if not fileExists('/STARTUP') and fileExists(''+dirscripts+'/_Copying_plugin_to_other_image.sh'):
                        os.system('rm -f '+dirscripts+'/_Copying_plugin_to_other_image.sh')
        if not fileExists('/STARTUP') and fileExists(''+dirscripts+'/_20') :
                        os.system('sh '+dirMB+'/_Add_Slots.sh')
        if fileExists('/STARTUP') and fileExists('/STARTUP_9') and fileExists(''+dirscripts+'/_20') :
                        os.system('sh '+dirMB+'/_Add_Slots.sh')
        elif fileExists('/boot/STARTUP_20') and not fileExists(''+dirscripts+'/_20'):
                        os.system('rm -f '+dirscripts+'/_Copying_plugin_to_other_image.sh')
                
        os.system('chmod 755 '+dirscripts+'/*.sh; chmod 755 '+dirMB+'/_Add_Slots.sh')
                
#>HDD
        def hddslots(self):
            if fileExists('/media/hdd') and fileExists('/STARTUP'):
                                os.system('mkdir /tmp/slotsx; touch /tmp/slotsx/addhdd; blkid /dev/sda1 > /tmp/slotsx/sda1; blkid -s UUID -o value /dev/sda1 > /tmp/slotsx/usda; blkid /dev/sdb1 > /tmp/slotsx/sdb1; blkid -s UUID -o value /dev/sdb1 > /tmp/slotsx/usdb; df -h | grep ^/dev/sda1 > /tmp/slotsx/labelsda1; df -h | grep ^/dev/sdb1 > /tmp/slotsx/labelsdb1;')
                                getResultMount()
                                os.system('sh '+dirMB+'/_Add_Slots.sh')
            else:
                                self.myClose(_('Sorry, Slots can be installed or upgraded only when booted from Slot0 Recovery or slots exists'))
                                  
#>USB
        def usbslots(self):
            if fileExists('/media/usb') and fileExists('/STARTUP'):
                                os.system('mkdir /tmp/slotsx; touch /tmp/slotsx/addusb; blkid /dev/sda1 > /tmp/slotsx/sda1; blkid -s UUID -o value /dev/sda1 > /tmp/slotsx/usda; blkid /dev/sdb1 > /tmp/slotsx/sdb1; blkid -s UUID -o value /dev/sdb1 > /tmp/slotsx/usdb; df -h | grep ^/dev/sda1 > /tmp/slotsx/labelsda1; df -h | grep ^/dev/sdb1 > /tmp/slotsx/labelsdb1;')
                                getResultMount()
                                os.system('sh '+dirMB+'/_Add_Slots.sh')
            else:
                                self.myClose(_('Sorry, Slots can be installed or upgraded only when booted from Slot0 Recovery or slots exists'))

        def loadScriptList(self):
                if fileExists('/tmp/imbvuver') and PLUGINVERSION != mbvuver:
                    if GetTranslator() == 'pl_PL' and fileExists('/STARTUP'):
                        os.system('mv -f '+dirscripts+'/_Update_Plugin '+dirscripts+'/_Aktualizacja.sh')
                    else:
                        os.system('mv -f '+dirscripts+'/_Update_Plugin '+dirscripts+'/_Update_Plugin.sh')
                else:
                    if GetTranslator() == 'pl_PL' and fileExists('/STARTUP'):
                        os.system('mv -f '+dirscripts+'/_Aktualizacja.sh '+dirscripts+'/_Update_Plugin')
                    else:
                        os.system('mv -f '+dirscripts+'/_Update_Plugin.sh '+dirscripts+'/_Update_Plugin')
                        
                if fileExists(''+dirscripts+'/_Copying_plugin_to_other_image.sh') and GetTranslator() == 'pl_PL' and fileExists('/STARTUP'):
                        os.system('mv -f '+dirscripts+'/_Copying_plugin_to_other_image.sh '+dirscripts+'/_Kopiowanie_wtyczki_do_innych_image.sh')
                try:
                        list = listdir("/usr/lib/enigma2/python/Plugins/Extensions/MBvu/script/")
                        list.sort()
                        list = [x[:-3] for x in list if x.endswith('.sh')]
                except:
                        list = []
                
                self["list"].setList(list)

        def run(self):
                try:
                        script = self["list"].getCurrent()
                except:
                        script = None
                
                if script is not None:
                        title = script
                        script = "/usr/lib/enigma2/python/Plugins/Extensions/MBvu/script/%s.sh" % script
                
                self.session.open(Console, title, cmdlist=[script])
			
        def myClose(self, message):
            self.session.open(MessageBox, message, MessageBox.TYPE_INFO)
            self.close()

def checkimage():
    mycheck = False
    if fileExists('/proc/stb/info/vumodel') and not fileExists('/proc/stb/info/boxtype'):
        mycheck = True
    else:
        mycheck = False
    return mycheck
    
def main(session, **kwargs):
    if fileExists('/boot/STARTUP') or fileExists('/STARTUP') and checkimage():
            session.open(ScriptNeo)
    else:
            if GetTranslator() == 'pl_PL':
                    session.open(MessageBox, _('Przepraszamy: Musisz zainstalowac we flashu vu+ image, albo kexec, lub uruchom slot0 RECOVERY.'), MessageBox.TYPE_INFO, 8)
            else:
                    session.open(MessageBox, _('Sorry: Wrong image in flash found. You have to install in flash VuPLUS Image or back to RECOVERY Slot0.'), MessageBox.TYPE_INFO, 8)

def startList(menuid):
    if menuid != 'mainmenu':
        return []
    else:
        return [(_('MBvu Selector'),         
          main,
          'tvlist',
          None)]

from Plugins.Plugin import PluginDescriptor

def Plugins(**kwargs):
    list = [PluginDescriptor(name='MBvu Selector', description='Boot Image', where=PluginDescriptor.WHERE_MENU, fnc=startList), PluginDescriptor(name='MBvu Selector', description=_('Boot Image'), icon='mbvu.png', where=PluginDescriptor.WHERE_PLUGINMENU, fnc=main)]
    list.append(PluginDescriptor(name=_('MBvu Selector'), where=PluginDescriptor.WHERE_EXTENSIONSMENU, fnc=main))
    return list
