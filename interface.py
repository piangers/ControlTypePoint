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
        layerReferencia = self.referenciaComboBox.currentLayer()
        layerAvaliacao  = self.avaliacaoComboBox.currentLayer()
        novaEscala = escalaAtual + escalaAval - escalaAtual
        
        if escalaAval == escalaAtual:
            pass
        else:      
            canvas.zoomScale(novaEscala)
            canvas.refresh()

    def distance (self, point1, point2): 

        layerReferencia = self.referenciaComboBox.currentLayer()
        layerAvaliacao  = self.avaliacaoComboBox.currentLayer()

        for feat in layerReferencia():
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
