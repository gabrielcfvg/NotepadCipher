# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\modelos\confirm_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(361, 211)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(50, 120, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 50, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.button_ok = QtWidgets.QPushButton(Dialog)
        self.button_ok.setGeometry(QtCore.QRect(260, 160, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_ok.setFont(font)
        self.button_ok.setObjectName("button_ok")
        self.button_cancelar = QtWidgets.QPushButton(Dialog)
        self.button_cancelar.setGeometry(QtCore.QRect(170, 160, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_cancelar.setFont(font)
        self.button_cancelar.setObjectName("button_cancelar")
        self.label_res = QtWidgets.QLabel(Dialog)
        self.label_res.setGeometry(QtCore.QRect(20, 170, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_res.setFont(font)
        self.label_res.setText("")
        self.label_res.setAlignment(QtCore.Qt.AlignCenter)
        self.label_res.setObjectName("label_res")
        self.labe_num = QtWidgets.QLabel(Dialog)
        self.labe_num.setGeometry(QtCore.QRect(150, 90, 47, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labe_num.setFont(font)
        self.labe_num.setStyleSheet("background-color: white;\n"
"border: 1px solid black")
        self.labe_num.setAlignment(QtCore.Qt.AlignCenter)
        self.labe_num.setObjectName("labe_num")
        self.label_nome = QtWidgets.QLabel(Dialog)
        self.label_nome.setGeometry(QtCore.QRect(10, 10, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_nome.setFont(font)
        self.label_nome.setText("")
        self.label_nome.setAlignment(QtCore.Qt.AlignCenter)
        self.label_nome.setObjectName("label_nome")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Digite o número para confirmar"))
        self.button_ok.setText(_translate("Dialog", "ok"))
        self.button_cancelar.setText(_translate("Dialog", "cancelar"))
        self.labe_num.setText(_translate("Dialog", "2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
