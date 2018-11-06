# -*- coding: UTF-8 -*-
from qgis.core import *
from qgis.gui import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from dlg import Ui_Dialog as GUI
import math
from math import sqrt
import itertools


class Interface(QDialog, GUI):

    def __init__(self):
        super(Interface, self).__init__()
        self.setupUi(self)

        self.spinBox.setMaximum(99999999)
        self.spinBox.setMinimum(0)

        self.initSignals()

    def initSignals(self):
        self.enter.accepted.connect(self.accept)
    
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

        # Converter escala textual para numérica (denominador)
        # escala = self.escalaAvaliacao.currentText() # '1:100.000'
        # escalaAval = escala.split(':')[1].replace('.','')
        # escalaAval = int(escalaAval)

        raio = self.spinBox.value()
        layer1 = self.referenciaComboBox.currentLayer()
        layer2 = self.avaliacaoComboBox.currentLayer()

        XY = False
        Z = False

        if self.xy.isChecked():
            XY = True
        if self.z.isChecked():
            Z = True

        source1 = layer1.crs()
        source2 = layer2.crs()
        dest = QgsCoordinateReferenceSystem(3857)

        tr1 = QgsCoordinateTransform(source1, dest)
        tr2 = QgsCoordinateTransform(source2, dest)

        lista1 = []
        lista2 = []

        for f1 in layer1.getFeatures():
            lista1.append(f1)
        for f2 in layer2.getFeatures():
            lista2.append(f2)
            
        listaNotFound = []
        listaHomologosXY = {}
        listaHomologosZ = {}
            
        for f1 in lista1:
            geom1 = QgsGeometry(f1.geometry())
            geom1.transform(tr1)
            found = False
            raioTeste = raio
            maisPerto = None
                
            for f2 in lista2:
                geom2 = QgsGeometry(f2.geometry())
                geom2.transform(tr2)
                if geom1.buffer(raioTeste,20).contains(geom2):
                    raioTeste = sqrt(geom1.asPoint().sqrDist(geom2.asPoint()))
                    maisPerto = f2
                    found = True
                    
            if found == False:
                listaNotFound.append(int(f1.id()))
            
            else:
                if XY:
                    listaHomologosXY[int(f1.id()), int(maisPerto.id())] = (raioTeste)
                if Z:
                    listaHomologosZ[int(f1.id()), int(maisPerto.id())]  = f1.geometry().geometry().z() - maisPerto.geometry().geometry().z()
                lista2.remove(maisPerto)
        
        #print 'Id\'s nao encontrados: ', listaNotFound
        
        if XY or Z:
            #QMessageBox.information (self.iface.mainWindow() ,  u'Resultados: ' ,  'Homologos: ', listaHomologosXY.keys())
            print 'Homologos: ', (listaHomologosXY.keys(),listaHomologosXY.values())
            print 'DistanciaHomologados', listaHomologosXY.values()

        if XY:
            distAcum = 0
            for valorXY in listaHomologosXY.values():
                distAcum += valorXY

            resultado = str(distAcum / len(listaHomologosXY))
            
            #QMessageBox.about (self.iface.mainWindow() , u'Distancia media: ', resultado)
            print 'Distancia media: ', distAcum / len(listaHomologosXY)

        if Z:
            zAcum = 0
            
            for valorZ in listaHomologosZ.values():
                zAcum += valorZ

            resultado = str(zAcum / len(listaHomologosZ))

            #QMessageBox.information (self.iface.mainWindow() ,u'Diferenca media de elevacao:', resultado)
            print 'Diferenca media de elevacao: ', zAcum / len(listaHomologosZ)

            
            
            
            
            
            
            
            #_________________________________________________#
            #                                                 #
            #             Calculando a distância              #
            #     distAB = sqrt((xA-xB)**2) + ((yA-yB)**2)    #  
            #_________________________________________________#