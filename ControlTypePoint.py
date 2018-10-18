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

#Carrega o arquivo da interface .ui
sys.path.append(os.path.dirname(__file__))
GUI,_= uic.loadUiType (os.path.join(os.path.dirname(__file__),'ui','dlg.ui'),resource_suffix='')

class ControlTypePoint( QDialog, GUI ):


    def __init__(self, iface):
      # Save reference to the QGIS interface
        self.iface = iface
        self.canvas = self.iface.mapCanvas()
        self.active = False

    def initGui(self):
        # 1 - CRIAR UM BOTÃO PARA ATIVAR A FERRAMENTA
        settings = QSettings()
        self.tAction = QAction(QIcon(':/plugins/ControlTypePoint/tr.png'), u'Control tools', self.iface.mainWindow())
        self.tAction.setCheckable(True)
        self.spinBox = QDoubleSpinBox(self.iface.mainWindow())
        self.toolbar = self.iface.addToolBar(u'Control tools')
        
        # 2 - CONECTAR O CLIQUE DO BOTÃO COM UM MÉTODO ("SLOT")
        self.tAction.toggled.connect(self.run)
        self.spinBox.valueChanged.connect(self.setRaio)
        self.comboBox.currentIndexChanged.connect(self.layer_field)
       
        #Padrões fixados
        
        self.spinBox.setDecimals(1)
        self.spinBox.setMinimum(0.000)
        self.spinBox.setMaximum(5000.000)
        self.spinBox.setSingleStep(0.100)
        self.raio = self.spinBox.value()
        self.spinBox.setToolTip("Raio de busca de Pontos.")
        self.toolbar.addAction(self.tAction)
        

    def unload(self):
        del self.toolbar
        
    def setRaio(self, t):
        self.raio = t # recebendo Raio atravéz de t.




###########################################################################################################################
###########################################################################################################################




    
    def run(self):
        """Run method that performs all the real work"""

        # exibe o diálogo
        self.dlg.show()

        # cria o objeto combobox:
        #self.dlg.comboBox = QComboBox() 
        
        # Obter todas as camadas carregadas na interface
        layers = self.iface.legendInterface().layers()
        self.layers = [layer for layer in self.iface.legendInterface().layers() if layer.type() == QgsMapLayer.VectorLayer]
        
        # Cria uma lista vazia que possamos preencher
        layer_list = []
        
        # Para cada item (que chamamos de "camada") em todas as camadas carregadas
        for layer in layers:
            # Adicione-o à lista
            layer_list.append(layer.name())

        ''' CAMADA DE REFERÊNCIA '''   

        # Clear comboBox ( útil para não criar itens duplicados na lista )
        self.dlg.comboBox.clear()
        # Adicione todos os itens na lista ao comboBox por nome
        self.dlg.comboBox.addItems(layer_list)
        
        ''' CAMADA DE AVALIAÇÃO '''

        # Clear comboBox_2 ( útil para não criar itens duplicados na lista )
        self.dlg.comboBox_2.clear()
        # Adicione nomes de campos ao comboBox_2
        self.dlg.comboBox_2.addItems(layer_list)

        ''' ESCALA DE AVALIAÇÃO '''

        # Clear comboBox_3 ( útil para não criar itens duplicados na lista )
        self.dlg.comboBox_3.clear() 
        # Adicione nomes de campos ao comboBox_3          
        self.dlg.comboBox_3.addItems("1:250.000","1:100.000","1:50.000","1:25.000","1:10.000","1:2.000","1:1000")
        
        ''' CHECKBOX '''

        # CheckBox de X/Y
        if self.dlg.checkBoxXY.isChecked():
            doSomething()
        else:
            doSomethingElse()
        
        # CheckBox de Z
        if self.dlg.checkBoxZ.isChecked():
            doSomething()
        else:
            doSomethingElse()
    
    
    
    
    
    
    
    
    
    
    
    
    # Ao alterar a camada no comboBox, execute a função "layer_field ()"
    # para atualizar os nomes dos campos nas comboBoxes associadas
    

    # Para escolher uma camada: QgsMapLayerComboBox
    # Para escolher um campo em uma camada: QgsFieldComboBox


    # # Identifique a camada selecionada pelo seu índice
    # selectedLayerIndex = self.dlg.comboBox.currentIndex()
    # selectedLayer = self.layers[selectedLayerIndex]

    # # Identifique os campos da camada selecionada
    # fields = selectedLayer.pendingFields()

    # Obter nomes de campos dos campos
    # fieldnames = [field.name() for field in fields]
