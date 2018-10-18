# -*- coding: UTF-8 -*-
from qgis.core import *
from qgis.gui import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from selectiontool import SelectionTool
import resources_rc
import math
import sys
import os
from PyQt4 import uic

from interface import Interface

#Carrega o arquivo da interface .ui
#sys.path.append(os.path.dirname(__file__))
#GUI,_= uic.loadUiType (os.path.join(os.path.dirname(__file__),'ui','dlg.ui'),resource_suffix='')

class ControlTypePoint:

    def __init__(self, iface):
      # Save reference to the QGIS interface
        self.iface = iface
        self.canvas = self.iface.mapCanvas()
        self.active = False
        self.dlg = Interface()

    def initGui(self):
        # 1 - CRIAR UM BOTÃO PARA ATIVAR A FERRAMENTA
        settings = QSettings()
        self.tAction = QAction(QIcon(':/plugins/ControlTypePoint/tr.png'), u'Control tools', self.iface.mainWindow())
        self.toolbar = self.iface.addToolBar(u'Control tools')
        
        # 2 - CONECTAR O CLIQUE DO BOTÃO COM UM MÉTODO ("SLOT")
        self.tAction.triggered.connect(self.openWindow)
       
        #Padrões fixados
        
        self.toolbar.addAction(self.tAction)
        
    def unload(self):
        del self.toolbar
        
    def openWindow(self):
        self.dlg.show()


##################################################################################################################################
##################################################################################################################################