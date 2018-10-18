# -*- coding: UTF-8 -*-
from qgis.core import *
from qgis.gui import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from dlg import Ui_Dialog as GUI

class Interface(QDialog, GUI):

    def __init__(self):
        super(Interface, self).__init__()
        self.setupUi(self)

        self.initSignals()

    def initSignals(self):
    #     self.enter.accepted.connect(self.executar)
        pass
    
    def accept(self):
        if self.referenciaComboBox.currentLayer() is None:
            print 'Sem layer referencia definido.'
        
        elif self.avaliacaoComboBox.currentLayer() is None:
            print 'Sem layer de avaliacao definido.'
        
        elif not self.xy.isChecked() and not self.z.isChecked():
            print 'Parametros de avaliacao nao selecionados.'

        else:
            self.run()
            super(Interface, self).accept()

    def run(self):
        print 'Codigo entra aqui'
        # Converter escala textual para numérica (denominador)
        escala = self.escalaAvaliacao.currentText() # '1:100.000'
        escalaNum = escala.split(':')[1].replace('.','')
        escalaNum = int(escalaNum)

        # Recuperar layer selecionado nas combos
        layerReferencia = self.referenciaComboBox.currentLayer()
        layerAvaliacao  = self.avaliacaoComboBox.currentLayer()
    
    # def run(self):

    #     """Run method that performs all the real work"""

    #     # exibe o diálogo
    #     self.dlg.show()

    #     # cria o objeto combobox:
    #     #self.dlg.comboBox = QComboBox() 
        
    #     # Obter todas as camadas carregadas na interface
    #     layers = self.iface.legendInterface().layers()
    #     self.layers = [layer for layer in self.iface.legendInterface().layers() if layer.type() == QgsMapLayer.VectorLayer]
        
    #     # Cria uma lista vazia que possamos preencher
    #     layer_list = []
        
    #     # Para cada item (que chamamos de "camada") em todas as camadas carregadas
    #     for layer in layers:
    #         # Adicione-o à lista
    #         layer_list.append(layer.name())

    #     ''' CAMADA DE REFERÊNCIA '''   

    #     # Clear comboBox ( útil para não criar itens duplicados na lista )
    #     self.dlg.comboBox.clear()
    #     # Adicione todos os itens na lista ao comboBox por nome
    #     self.dlg.comboBox.addItems(layer_list)
        
    #     ''' CAMADA DE AVALIAÇÃO '''

    #     # Clear comboBox_2 ( útil para não criar itens duplicados na lista )
    #     self.dlg.comboBox_2.clear()
    #     # Adicione nomes de campos ao comboBox_2
    #     self.dlg.comboBox_2.addItems(layer_list)

    #     ''' ESCALA DE AVALIAÇÃO '''

    #     # Clear comboBox_3 ( útil para não criar itens duplicados na lista )
    #     self.dlg.comboBox_3.clear() 
    #     # Adicione nomes de campos ao comboBox_3          
    #     self.dlg.comboBox_3.addItems("1:250.000","1:100.000","1:50.000","1:25.000","1:10.000","1:2.000","1:1000")
        
    #     ''' CHECKBOX '''

    #     # CheckBox de X/Y
    #     if self.dlg.checkBoxXY.isChecked():
    #         doSomething()
    #     else:
    #         doSomethingElse()
        
    #     # CheckBox de Z
    #     if self.dlg.checkBoxZ.isChecked():
    #         doSomething()
    #     else:
    #         doSomethingElse()
    
    
    
    
    
    
    
    
    
    
    
    
    # # Ao alterar a camada no comboBox, execute a função "layer_field ()"
    # # para atualizar os nomes dos campos nas comboBoxes associadas
    

    # # Para escolher uma camada: QgsMapLayerComboBox
    # # Para escolher um campo em uma camada: QgsFieldComboBox


    # # # Identifique a camada selecionada pelo seu índice
    # # selectedLayerIndex = self.dlg.comboBox.currentIndex()
    # # selectedLayer = self.layers[selectedLayerIndex]

    # # # Identifique os campos da camada selecionada
    # # fields = selectedLayer.pendingFields()

    # # Obter nomes de campos dos campos
    # # fieldnames = [field.name() for field in fields]
