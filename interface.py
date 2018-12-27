# -*- coding: UTF-8 -*-
from qgis.core import QgsCoordinateReferenceSystem, QgsCoordinateTransform, QgsGeometry, QgsSpatialIndex, QgsPoint, QgsFeatureRequest, QgsFeature
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

        listaHomologosXY = {} # dicionario yx.
        listaHomologosZ = {} # dicionario z.    
       
        # Raio definido
        raio = self.spinBox.value()

        # Layers selecionados
        layer1 = self.referenciaComboBox.currentLayer()
        layer2 = self.avaliacaoComboBox.currentLayer()

        # Teste para identificar se esta setado.
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

        lista1 = [feat1 for feat1 in layer1.getFeatures()]
        lista2 = [feat2 for feat2 in layer2.getFeatures()]

        # indice espacial 
        spIndex1 = QgsSpatialIndex()

        neighbour = QgsFeature()
     
        
        for feat1 in lista1: 

            spIndex1.insertFeature(feat1)  # transforma features em indices espaciais

            geom1 = QgsGeometry(feat1.geometry()) 
            geom1.transform(tr1)        
            raioTeste = raio 
            neighbour = None
            encontrado =  False
            
                
            for feat2 in lista2:
                pt = feat2.geometry().asPoint()
                # # QgsSpatialIndex.nearestNeighbor (QgsPoint point, int neighbors)
                nearestid = spIndex1.nearestNeighbor(pt, 1)[0] # realiza a analise do vizinho mais próximo, numero de vizinhos é definido no segundo argumento.
                request = QgsFeatureRequest().setFilterFid(nearestid)
                #neighbour = feat2
                
                geom2 = QgsGeometry(feat2.geometry()) 
                 
                geom2.transform(tr2) 

                if geom1.buffer (raioTeste, 20 ) .contains (geom2):
                     raioTeste = sqrt (geom1.asPoint (). sqrDist (geom2.asPoint ()))
                     neighbour = feat2  
                     encontrado =   True
                
            
            # apenas pra descobrir se não foi encontrado.
            if encontrado == False: 
                print u'\nHouve pontos não encontrados dentro do raio definido.'
                
            else:
                if XY:
                    listaHomologosXY[int(feat1.id()), int(neighbour.id())] = (raioTeste)
                if Z:
                    listaHomologosZ[int(feat1.id()), int(neighbour.id())]  = feat1.geometry().geometry().z() - neighbour.geometry().geometry().z()
                lista2.remove(neighbour)     

        if XY or Z:   
            print '\nHomologos: \n', listaHomologosXY.keys()
            resultado = listaHomologosXY.values()   
            print '\nDistancia entre pontos Homologados:\n',resultado
                     
        if XY: 
            distAcum = 0
            for valorXY in listaHomologosXY.values():
                distAcum += valorXY    

            resultado = int(distAcum / len(listaHomologosXY))
            print '\nDistancia media:\n', round(resultado,2)  
            
        if Z:
            zAcum = 0     
            for valorZ in listaHomologosZ.values(): 
                zAcum += valorZ
            resultado = int(zAcum / len(listaHomologosZ)) 
            print '\nDiferenca media de elevacao: \n', round(resultado,3)
            


        #     #_________________________________________________#
        #     #                                                 #
        #     #               Calculo distância                 #
        #     #     distAB = sqrt((xA-xB)**2) + ((yA-yB)**2)    #  
        #     #_________________________________________________#

# target_spatial_index = QgsSpatialIndex()
# # populate the spatial index
# for f in featB:
#     target_spatial_index.insertFeature(f)


# with edit(layerB):
#     for feat in featA:

#         # Skip if into deleted list
#         if feat.id() not in del_feat:

#             point1 = feat.geometry().asPoint()

#             nearest_ids = target_spatial_index.nearestNeighbor(point1,2)

#             high_id=0
#             for id in nearest_ids:

#                 outFeat = layerB.getFeatures(QgsFeatureRequest().setFilterFid(id)).next()

#                 #skip himself
#                 if outFeat.id() != feat.id():

#                     # distance between points
#                     point2 = outFeat.geometry().asPoint()
#                     dist = sqrt(point1.sqrDist(point2))

#                     high_id=outFeat.id()


#                     if dist <= 15:
#                         # remove from spatial index
#                         target_spatial_index.deleteFeature(outFeat)

#                         layerB.deleteFeatures([high_id])
#                         # add to list of deleted
#                         del_feat.append(high_id)