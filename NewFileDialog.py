# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\dialog_newfile.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(361, 95)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(92, 10, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_nome = QtWidgets.QLabel(Dialog)
        self.label_nome.setGeometry(QtCore.QRect(10, 10, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_nome.setFont(font)
        self.label_nome.setAlignment(QtCore.Qt.AlignCenter)
        self.label_nome.setObjectName("label_nome")
        self.button_ok = QtWidgets.QPushButton(Dialog)
        self.button_ok.setGeometry(QtCore.QRect(264, 50, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_ok.setFont(font)
        self.button_ok.setObjectName("button_ok")
        self.button_cancelar = QtWidgets.QPushButton(Dialog)
        self.button_cancelar.setGeometry(QtCore.QRect(170, 50, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_cancelar.setFont(font)
        self.button_cancelar.setObjectName("button_cancelar")
        self.label_nomeemuso = QtWidgets.QLabel(Dialog)
        self.label_nomeemuso.setGeometry(QtCore.QRect(10, 60, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_nomeemuso.setFont(font)
        self.label_nomeemuso.setText("")
        self.label_nomeemuso.setAlignment(QtCore.Qt.AlignCenter)
        self.label_nomeemuso.setObjectName("label_nomeemuso")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_nome.setText(_translate("Dialog", "Nome:"))
        self.button_ok.setText(_translate("Dialog", "ok"))
        self.button_cancelar.setText(_translate("Dialog", "cancelar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
