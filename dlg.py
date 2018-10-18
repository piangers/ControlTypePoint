# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dlg.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from qgis.gui import QgsMapLayerComboBox, QgsMapLayerProxyModel

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(336, 266)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.referenciaComboBox = QgsMapLayerComboBox(Dialog)
        self.referenciaComboBox.setFilters(QgsMapLayerProxyModel.PointLayer)
        self.referenciaComboBox.setObjectName(_fromUtf8("referenciaComboBox"))
        self.horizontalLayout.addWidget(self.referenciaComboBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.avaliacaoComboBox = QgsMapLayerComboBox(Dialog)
        self.avaliacaoComboBox.setFilters(QgsMapLayerProxyModel.PointLayer)
        self.avaliacaoComboBox.setObjectName(_fromUtf8("avaliacaoComboBox"))
        self.horizontalLayout_2.addWidget(self.avaliacaoComboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        self.escalaAvaliacao = QtGui.QComboBox(Dialog)
        self.escalaAvaliacao.setObjectName(_fromUtf8("escalaAvaliacao"))
        self.escalaAvaliacao.addItem(_fromUtf8(""))
        self.escalaAvaliacao.addItem(_fromUtf8(""))
        self.escalaAvaliacao.addItem(_fromUtf8(""))
        self.escalaAvaliacao.addItem(_fromUtf8(""))
        self.escalaAvaliacao.addItem(_fromUtf8(""))
        self.escalaAvaliacao.addItem(_fromUtf8(""))
        self.escalaAvaliacao.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.escalaAvaliacao)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_4.addWidget(self.label_5)
        self.spinBox = QtGui.QSpinBox(Dialog)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.horizontalLayout_4.addWidget(self.spinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_5.addWidget(self.label_6)
        self.xy = QtGui.QCheckBox(Dialog)
        self.xy.setChecked(True)
        self.xy.setObjectName(_fromUtf8("xy"))
        self.horizontalLayout_5.addWidget(self.xy)
        self.z = QtGui.QCheckBox(Dialog)
        self.z.setObjectName(_fromUtf8("z"))
        self.horizontalLayout_5.addWidget(self.z)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.enter = QtGui.QDialogButtonBox(Dialog)
        self.enter.setOrientation(QtCore.Qt.Horizontal)
        self.enter.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.enter.setObjectName(_fromUtf8("enter"))
        self.verticalLayout.addWidget(self.enter)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.enter, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.enter, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Camada de referência", None))
        self.label_2.setText(_translate("Dialog", "Camada em avaliação", None))
        self.label_4.setText(_translate("Dialog", "Escala de avaliação", None))
        self.escalaAvaliacao.setItemText(0, _translate("Dialog", "1:250.000", None))
        self.escalaAvaliacao.setItemText(1, _translate("Dialog", "1:100.000", None))
        self.escalaAvaliacao.setItemText(2, _translate("Dialog", "1:50.000", None))
        self.escalaAvaliacao.setItemText(3, _translate("Dialog", "1:25.000", None))
        self.escalaAvaliacao.setItemText(4, _translate("Dialog", "1:10.000", None))
        self.escalaAvaliacao.setItemText(5, _translate("Dialog", "1:2.000", None))
        self.escalaAvaliacao.setItemText(6, _translate("Dialog", "1:1.000", None))
        self.label_5.setText(_translate("Dialog", "Raio", None))
        self.label_6.setText(_translate("Dialog", "Parâmetros", None))
        self.xy.setText(_translate("Dialog", "X/Y", None))
        self.z.setText(_translate("Dialog", "Z", None))

