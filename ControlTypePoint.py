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
        self.spinBox = QDoubleSpinBox(self.iface.mainWindow())
        self.toolbar = self.iface.addToolBar(u'Trim tools')
        
        # 2 - CONECTAR O CLIQUE DO BOTÃO COM UM MÉTODO ("SLOT")
        self.tAction.toggled.connect(self.run)
        self.spinBox.valueChanged.connect(self.setTolerancia)
       
        #Padrões fixados
        
        self.spinBox.setDecimals(1)
        self.spinBox.setMinimum(0.000)
        self.spinBox.setMaximum(5000.000)
        self.spinBox.setSingleStep(0.100)
        self.tolerancia = self.spinBox.value()
        self.spinBox.setToolTip("Escala de avaliacao")
        self.toolbar.addAction(self.tAction)
        # self.combobox = QComboBox() # cria o objeto combobox:

    def unload(self):
        del self.toolbar
        
    def setTolerancia(self, t):
        self.tolerancia = t # recebendo tolerância atravéz de t.

    def run(self):
        """Run method that performs all the real work"""
        # show the dialog
        self.dlg.show()

        # Get all loaded layers in the interface
        #layers = self.iface.legendInterface().layers()
        layers = [layer for layer in self.iface.legendInterface().layers() if layer.type() == QgsMapLayer.VectorLayer]
        # Create an empty list which we can populate
        layer_list = []
        # For every item (which we call "layer") in all loaded layers
        for layer in layers:
            # Add it to the list
            layer_list.append(layer.name())
        # Clear comboBox (useful so we don't create duplicate items in list)
        self.dlg.comboBox.clear()
        # Add all items in list to comboBox
        self.dlg.comboBox.addItems(layer_list)
        # Clear comboBox_2
        self.dlg.comboBox_2.clear()
        # Add all items in list to comboBox_2
        self.dlg.comboBox_2.addItems(layer_list)

    def layer_field():
        # Identify selected layer by its index
        selectedLayerIndex = self.dlg.comboBox.currentIndex()
        selectedLayer = layers[selectedLayerIndex]
        # Identify fields of the selected layer
        fields = selectedLayer.pendingFields()
        # Get field names of the fields
        fieldnames = [field.name() for field in fields]
        # Clear comboBox_5
        self.dlg.comboBox_5.clear()
        # Add field names to comboBox_5
        self.dlg.comboBox_5.addItems(fieldnames)

    def table_field():
        # Same comments as above
        selectedLayerIndex = self.dlg.comboBox_2.currentIndex()
        selectedLayer = layers[selectedLayerIndex]
        fields = selectedLayer.pendingFields()
        fieldnames = [field.name() for field in fields]
        self.dlg.comboBox_3.clear()            
        self.dlg.comboBox_3.addItems(fieldnames)
        self.dlg.comboBox_4.clear()
        self.dlg.comboBox_4.addItems(fieldnames)

    # When changing layer in comboBox, run the function "layer_field()"
    # to refresh the field names in the associated comboBoxes
    self.dlg.comboBox.currentIndexChanged.connect(layer_field)
    self.dlg.comboBox_2.currentIndexChanged.connect(table_field)

    # Para escolher uma camada: QgsMapLayerComboBox
    # Para escolher um campo em uma camada: QgsFieldComboBox