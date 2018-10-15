# -*- coding: UTF-8 -*-
from qgis.core import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from selectiontool import SelectionTool
import resources_rc
import math


class ControlPoint:

    def __init__(self, iface):
      # Save reference to the QGIS interface
        self.iface = iface
        self.canvas = self.iface.mapCanvas()
        self.active = False

    def initGui(self):
        # 1 - CRIAR UM BOTÃO PARA ATIVAR A FERRAMENTA
        settings = QSettings()
        self.tAction = QAction(QIcon(":/plugins/ControlPoint/tr.png"), u'Trim', self.iface.mainWindow())
        self.tAction.setCheckable(True)
        self.toolbar = self.iface.addToolBar(u'Trim tools')

        self.wcb = QgsMapLayerComboBox(self.dlg)
        self.wcb.setFixedWidth(220)
        self.wcb.move(140,40)
        self.wcb.setFilters( QgsMapLayerProxyModel.RasterLayer )
        
        # 2 - CONECTAR O CLIQUE DO BOTÃO COM UM MÉTODO ("SLOT")
        self.tAction.toggled.connect(self.run)  
       
        #Padrões fixados  
        self.toolbar.addAction(self.tAction)

        # cria o objeto combobox:
        self.comboBox = QComboBox() 

    def unload(self):
        del self.toolbar


    def run(self):
    """Run method that performs all the real work"""
    #My code starts here
    layer = self.wcb.currentLayer()
.
.
.
    self.dlg.show()
    # Run the dialog event loop
    result = self.dlg.exec_()
    # See if OK was pressed
    if result:
        # Do something useful here - delete the line containing pass and
        # substitute with your code.
        #My code starts here
        message = "the raster average of " + filename + " is = " + str(average) 
        QMessageBox.information(None, "Raster Average", message)
        #My code ends here



    































        

    # def run(self):
    #     """Run method that performs all the real work"""
       
    #     self.comboBox.show()  # mostra o diálogo

    #     # Obter todas as camadas carregadas na interface
    #     layers = self.iface.legendInterface().layers()
    #     self.layers = [layer for layer in self.iface.legendInterface().layers() if layer.type() == QgsMapLayer.VectorLayer]
        
    #     # Cria uma lista vazia que possamos preencher
    #     layer_list = []
        
    #     # Para cada item (que chamamos de "camada") em todas as camadas carregadas
    #     for layer in layers:
    #         # Adicione-o à lista
    #         layer_list.append(layer.name())

    #     # Clear comboBox (útil para não criar itens duplicados na lista)
    #     self.comboBox.clear()
   
    #     # Adicione todos os itens na lista ao comboBox
    #     self.comboBox.addItems()
        
    # def layer_field():

    #     # Identifique a camada selecionada pelo seu índice
    #     selectedLayerIndex = self.dlg.comboBox.currentIndex()
    #     selectedLayer = self.layers[selectedLayerIndex]

    #     # Identifique os campos da camada selecionada
    #     fields = selectedLayer.pendingFields()

    #     # Obter nomes de campos dos campos
    #     fieldnames = [field.name() for field in fields]

    #     # Clear comboBox_5
    #     self.dlg.comboBox_5.clear()

    #     # Adicione nomes de campos ao comboBox_5
    #     self.dlg.comboBox_5.addItems()

    #     # Mesmos comentários como acima
    #     selectedLayerIndex = self.dlg.comboBox_2.currentIndex()
    #     selectedLayer = self.layers[selectedLayerIndex]
    #     fields = selectedLayer.pendingFields()
    #     fieldnames = [field.name() for field in fields]
    #     self.dlg.comboBox_3.clear()            
    #     self.dlg.comboBox_3.addItems(fieldnames)
    #     self.dlg.comboBox_4.clear()
    #     self.dlg.comboBox_4.addItems(fieldnames)

    # # Ao alterar a camada no comboBox, execute a função "layer_field ()"
    # # para atualizar os nomes dos campos nas comboBoxes associadas
    # self.dlg.comboBox.currentIndexChanged.connect()
    

    # # Para escolher uma camada: QgsMapLayerComboBox
    # # Para escolher um campo em uma camada: QgsFieldComboBox