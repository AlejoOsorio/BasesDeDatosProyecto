# Form implementation generated from reading ui file 'frame_reporte_empleados.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(778, 500)
        self.verticalLayout = QtWidgets.QVBoxLayout(Frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=Frame)
        self.label.setStyleSheet("QLabel {\n"
"    font-size: 26px;\n"
"    font-weight: bold;\n"
"    color: #333;\n"
"    text-align: center;\n"
"    qproperty-alignment: AlignCenter;\n"
"}")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(parent=Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.label_2.setStyleSheet("QLabel {\n"
"    padding: 10px;\n"
"    font-weight: bold;\n"
"    qproperty-alignment: AlignCenter;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.comboBox_4 = QtWidgets.QComboBox(parent=Frame)
        self.comboBox_4.setMaximumSize(QtCore.QSize(300, 16777215))
        self.comboBox_4.setObjectName("comboBox_4")
        self.gridLayout_2.addWidget(self.comboBox_4, 0, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(parent=Frame)
        self.comboBox.setMaximumSize(QtCore.QSize(300, 16777215))
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_2.addWidget(self.comboBox, 4, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QtCore.QSize(300, 16777215))
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMaximumSize(QtCore.QSize(300, 16777215))
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(parent=Frame)
        self.comboBox_2.setMaximumSize(QtCore.QSize(300, 16777215))
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout_2.addWidget(self.comboBox_2, 2, 1, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(parent=Frame)
        self.comboBox_3.setMaximumSize(QtCore.QSize(300, 16777215))
        self.comboBox_3.setObjectName("comboBox_3")
        self.gridLayout_2.addWidget(self.comboBox_3, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(parent=Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMaximumSize(QtCore.QSize(300, 16777215))
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 4, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMaximumSize(QtCore.QSize(300, 16777215))
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(parent=Frame)
        self.pushButton.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label.setText(_translate("Frame", "Informe Empleados"))
        self.label_2.setText(_translate("Frame", "Seleccione los datos que quiere de su reporte"))
        self.label_3.setText(_translate("Frame", "Sucursal"))
        self.label_5.setText(_translate("Frame", "Municipio"))
        self.label_6.setText(_translate("Frame", "Profesion"))
        self.label_4.setText(_translate("Frame", "Departamento"))
        self.pushButton.setText(_translate("Frame", "Generar Informe"))