# Form implementation generated from reading ui file 'frame_login_usuario.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(597, 415)
        self.verticalLayout = QtWidgets.QVBoxLayout(Frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.relleno_izquierdo_2 = QtWidgets.QFrame(parent=Frame)
        self.relleno_izquierdo_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.relleno_izquierdo_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.relleno_izquierdo_2.setObjectName("relleno_izquierdo_2")
        self.gridLayout_2.addWidget(self.relleno_izquierdo_2, 1, 0, 1, 1)
        self.relleno_derecho_2 = QtWidgets.QFrame(parent=Frame)
        self.relleno_derecho_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.relleno_derecho_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.relleno_derecho_2.setObjectName("relleno_derecho_2")
        self.gridLayout_2.addWidget(self.relleno_derecho_2, 1, 4, 1, 1)
        self.label_7 = QtWidgets.QLabel(parent=Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMaximumSize(QtCore.QSize(300, 16777215))
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 2, 1, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(parent=Frame)
        self.lineEdit_6.setEnabled(True)
        self.lineEdit_6.setMaximumSize(QtCore.QSize(300, 26))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_2.addWidget(self.lineEdit_6, 1, 3, 1, 1)
        self.label_9 = QtWidgets.QLabel(parent=Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMaximumSize(QtCore.QSize(300, 16777215))
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 1, 1, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(parent=Frame)
        self.lineEdit_7.setEnabled(True)
        self.lineEdit_7.setMaximumSize(QtCore.QSize(300, 26))
        self.lineEdit_7.setFrame(True)
        self.lineEdit_7.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_2.addWidget(self.lineEdit_7, 2, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.buscar_3 = QtWidgets.QPushButton(parent=Frame)
        self.buscar_3.setMaximumSize(QtCore.QSize(150, 16777215))
        self.buscar_3.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.buscar_3.setObjectName("buscar_3")
        self.horizontalLayout_3.addWidget(self.buscar_3)
        self.actualizar_3 = QtWidgets.QPushButton(parent=Frame)
        self.actualizar_3.setMaximumSize(QtCore.QSize(150, 16777215))
        self.actualizar_3.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.actualizar_3.setObjectName("actualizar_3")
        self.horizontalLayout_3.addWidget(self.actualizar_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label_7.setText(_translate("Frame", "Password"))
        self.label_9.setText(_translate("Frame", "Login"))
        self.buscar_3.setText(_translate("Frame", "Iniciar Sesion"))
        self.actualizar_3.setText(_translate("Frame", "Cancelar"))