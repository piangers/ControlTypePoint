# -*- coding: UTF-8 -*-
from qgis.core import QgsCoordinateReferenceSystem, QgsCoordinateTransform, QgsGeometry, QgsSpatialIndex
from qgis.gui import QgsMessageBar
from PyQt4.QtGui import QDialog
from dlg import Ui_Dialog as GUI
import math
from math import sqrt
import itertools
import qgis

class Interface(QDialog, GUI):

    def __init__(self,iface):
        super(Interface, self).__init__()
        self.setupUi(self)
        self.iface = iface
        self.canvas = self.iface.mapCanvas()  
        self.spinBox.setMaximum(99999999)
        self.spinBox.setMinimum(0)
        
        self.initSignals() 


    # Sinal para realizar a execução.
    def initSignals(self):
        self.enter.accepted.connect(self.accept)
    
    
    # Necessario para o funcionamento da UI.
    def accept(self):  

        if self.referenciaComboBox.currentLayer() is None:  
            print 'Sem layer referencia definido.\n'
        
        elif self.avaliacaoComboBox.currentLayer() is None:
            print 'Sem layer de avaliacao definido.\n'
        
        elif not self.xy.isChecked() and not self.z.isChecked():
             print 'Defina um eixo.\n'
        else:
            self.run()
            super(Interface, self).accept()
 


    def run(self):

        # Converter escala textual para numérica (denominador)
        escala = self.escalaAvaliacao.currentText() # '1:100.000'
        escalaAval = escala.split(':')[1].replace('.','')    
        escalaAval = int(escalaAval)
        
        self.canvas.zoomScale(escalaAval)
         
        lista1 = [] # todas as features da layer1
        lista2 = [] # todas as features da layer2

        listaHomologosXY = {} # dicionario yx.
        listaHomologosZ = {} # dicionario z.    
       
        raio = self.spinBox.value()


        # layers
        layer1 = self.referenciaComboBox.currentLayer()
        layer2 = self.avaliacaoComboBox.currentLayer()
       

        XY = False
        Z = False

        if self.xy.isChecked():
            XY = True 
        if self.z.isChecked(): 
            Z = True

        # Troca de referência CRS para uma que utiliza medição em metros (3857).
        source1 = layer1.crs()
        source2 = layer2.crs()
        dest = QgsCoordinateReferenceSystem(3857)

        tr1 = QgsCoordinateTransform(source1, dest)
        tr2 = QgsCoordinateTransform(source2, dest)

        # indice espacial
        spIndex = QgsSpatialIndex()


        for f1 in layer1.getFeatures(): 
            spIndex.insertFeature(f1)  
            lista1.append(f1)
       
        # pegando as features da layer2 e copiando pra lista. 
        for f2 in layer2.getFeatures():   
            lista2.append(f2)  
            # QgsSpatialIndex.nearestNeighbor (QgsPoint point, int neighbors)
            nearestid = spIndex.nearestNeighbor(f2, 1)    


        # for f1 in lista1: 
  
        #     geom1 = QgsGeometry(f1.geometry()) 
        #     geom1.transform(tr1)        
        #     raioTeste = raio # raio teste recebe inicioalmente o raio definido.
        #     maisPerto = None
        #     encontrado =  False
        #     pt = f2.geometry().asPoint()
        #     nearestSpIndids = spIndex.nearestNeighbor(pt,2)    
        #     for f2 in lista2: 
        #         geom2 = QgsGeometry(f2.geometry())   
        #         geom2.transform(tr2) 
        #         if geom1.buffer(raioTeste,20).contains(geom2):
        #             raioTeste = sqrt(geom1.asPoint().sqrDist(geom2.asPoint() ))
        #             maisPerto = f2  
        #             encontrado =  True
 

            # apenas pra descobrir se não foi encontrado.
            if encontrado == False:
                
                print u'\nHouve pontos não encontrados dentro do raio definido.'
                self.iface.messageBar().pushMessage(u'Houve pontos não encontrados dentro do raio definido.', level=QgsMessageBar.WARNING, duration=5)
            
            else:
                if XY:
                    listaHomologosXY[int(f1.id()), int(maisPerto.id())] = (raioTeste)
                if Z:
                    listaHomologosZ[int(f1.id()), int(maisPerto.id())]  = f1.geometry().geometry().z() - maisPerto.geometry().geometry().z()
                lista2.remove(maisPerto)     


        if XY or Z: 
            
            print '\nHomologos: \n', listaHomologosXY.keys()
            self.iface.messageBar().pushMessage(u'\nHomologos: \n'+str(listaHomologosXY.keys()), level=QgsMessageBar.WARNING, duration=5)
            resultado = listaHomologosXY.values()
            
        print '\nDistancia entre pontos Homologados:\n',resultado
    
        if XY:
            for valorXY in listaHomologosXY.values():
                distAcum += valorXY    
 
            resultado = float(distAcum / len(listaHomologosXY))

            print '\nDistancia media:\n', round(resultado,2)  
  
        if Z:
            zAcum = 0     
            for valorZ in listaHomologosZ.values(): 
                zAcum += valorZ

            resultado = float(zAcum / len(listaHomologosZ)) 
            print '\nDiferenca media de elevacao: \n', round(resultado,3)

 




            #_________________________________________________#
            #                                                 #
            #               Calculo distância                 #
            #     distAB = sqrt((xA-xB)**2) + ((yA-yB)**2)    #  
            #_________________________________________________#

            