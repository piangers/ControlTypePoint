# -*- coding: UTF-8 -*-
from qgis.core import *
from qgis.gui import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from dlg import Ui_Dialog as GUI
import math

class Interface(QDialog, GUI):

    def __init__(self):
        super(Interface, self).__init__()
        self.setupUi(self)

        self.initSignals()

    def initSignals(self):
    #  self.enter.accepted.connect(self.executar)
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
        escalaAval = escala.split(':')[1].replace('.','')
        escalaAval = int(escalaAval)
        canvas = self.iface.mapCanvas()
        scala = canvas.scale()
        escalaAtual = scala.split('.')[0]
        # Recuperar layer selecionado nas combos
        layerRef = self.referenciaComboBox.currentLayer()
        layerAval = self.avaliacaoComboBox.currentLayer()
        novaEscala = escalaAtual + escalaAval - escalaAtual
        
        if signal:

            listaLr = []
            listaLa = []

            for lr in layerRef.getFeatures():
                # coordenada xy de layer de referência
                lr.geometry().asPoint()
                # coordenada Z de layerReferência
                geometryV2 = l.geometry().geometry()
                geometryV2.z()
                
            for la in layerAval.getFeatures():
                # coordenada xy de layer de avaliação
                la.geometry().asPoint()
                # coordenada Z de layer de avaliação
                geometryV2 = l.geometry().geometry()
                geometryV2.z()















        if escalaAval == escalaAtual:
            pass
        else:      
            canvas.zoomScale(novaEscala)
            canvas.refresh()

    def distance (self, point1, point2): 

        layerReferencia = self.referenciaComboBox.currentLayer()
        layerAvaliacao  = self.avaliacaoComboBox.currentLayer()

        for feat in layerReferencia():pointFather
            attrs = feat.attributes()
            geom = feat.geometry()
            coords = geom.asPoint()
            new_coords = (QgsPoint(coords[1], coords[0]))
            geom = QgsGeometry.fromPoint(new_coords)
        
        

        #Create a measure object

        distance = QgsDistanceArea()
        crs = QgsCoordinateReferenceSystem()
        crs.createFromSrsId(3452) # EPSG:4326
        distance.setSourceCrs(crs)
        distance.setEllipsoidalMode(True)
        distance.setEllipsoid('WGS84')
        m = distance.measureLine(point1, point2)
        return math.sqrt (point1.sqrDist (point2)) 






            # dpi=self.iface.mainWindow().physicalDpiX()
            # maxScalePerPixel = 156543.04
            # inchesPerMeter = 39.37
            # zoomlevel = int(round(math.log( ((dpi* inchesPerMeter * maxScalePerPixel) / escalaAtual), 2 ), 0))
            # print zoomlevel

import random
def generate_wind_turbines(spacing):
    layer = self.iface.activeLayer()
    crs = layer.crs()
    
    point_density = 0.0001
    fid = 1
    distance_area = QgsDistanceArea()
    # List of features
    fts = []
    # Create points
    points = dict() # changed from me 
    index = QgsSpatialIndex()# changend from me 
    nPoints = 0 # changed in the edit 
    pointCount = 0 # changed in the edit 

    for f in layer.getFeatures():
        fGeom = QgsGeometry(f.geometry())
        bbox = fGeom.boundingBox()
        # changed here as well 
        pointCount = int(round(point_density * distance_area.measure(fGeom))) + int(pointCount)
        fid += 1
        nIterations = 0
        maxIterations = pointCount * 200
        random.seed()
        while nIterations < maxIterations and nPoints < pointCount:
            rx = bbox.xMinimum() + bbox.width() * random.random()
            ry = bbox.yMinimum() + bbox.height() * random.random()
            pnt = QgsPoint(rx, ry)    
            geom = QgsGeometry.fromPoint(pnt)
            if geom.within(fGeom) and checkMinDistance(pnt, index, spacing, points):
                f = QgsFeature(nPoints)
                f.setAttributes([fid])
                f.setGeometry(geom)
                fts.append(f)
                index.insertFeature(f)
                points[nPoints] = pnt
                nPoints += 1
            nIterations += 1
    provider.addFeatures(fts)
    memory_lyr.updateFields()
    memory_lyr.commitChanges()








    def dist(x0, y0, x1, y1):
        a = (x1 - x0)**2 + (y1 - y0)**2
        b = math.sqrt(a)
        return b



# def checkMinDistance( point, index, distance, points):
#     if distance == 0:
#         return True
#     neighbors = index.nearestNeighbor(point, 1)
#     if len(neighbors) == 0:
#         return True
#     if neighbors[0] in points:
#         np = points[neighbors[0]]
#         if np.sqrDist(point) < (distance * distance):
#             return False
#     return True