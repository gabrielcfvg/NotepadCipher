# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\formMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 720))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 720))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: #242b2d;")
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(290, 0, 20, 721))
        self.widget.setStyleSheet("background-color: #000002;")
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(0, 60, 1281, 20))
        self.widget_2.setStyleSheet("background-color: rgb(0, 0, 2);")
        self.widget_2.setObjectName("widget_2")
        self.button_criar = QtWidgets.QPushButton(self.centralwidget)
        self.button_criar.setGeometry(QtCore.QRect(10, 10, 151, 41))
        self.button_criar.setStyleSheet("background-color: rgb(76, 84, 86);")
        self.button_criar.setDefault(False)
        self.button_criar.setFlat(False)
        self.button_criar.setObjectName("button_criar")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 90, 271, 621))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.name_view = QtWidgets.QLabel(self.centralwidget)
        self.name_view.setGeometry(QtCore.QRect(320, 10, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.name_view.setFont(font)
        self.name_view.setObjectName("name_view")
        self.name_label = QtWidgets.QLabel(self.centralwidget)
        self.name_label.setGeometry(QtCore.QRect(430, 10, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setUnderline(False)
        self.name_label.setFont(font)
        self.name_label.setObjectName("name_label")
        self.button_salvar = QtWidgets.QPushButton(self.centralwidget)
        self.button_salvar.setGeometry(QtCore.QRect(320, 90, 41, 621))
        self.button_salvar.setStyleSheet("background-color: rgb(76, 84, 86);")
        self.button_salvar.setObjectName("button_salvar")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(370, 90, 901, 621))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.textEdit.setObjectName("textEdit")
        self.button_this = QtWidgets.QPushButton(self.centralwidget)
        self.button_this.setGeometry(QtCore.QRect(170, 10, 51, 41))
        self.button_this.setStyleSheet("background-color: rgb(76, 84, 86);")
        self.button_this.setObjectName("button_this")
        self.button_excluir = QtWidgets.QPushButton(self.centralwidget)
        self.button_excluir.setGeometry(QtCore.QRect(700, 10, 51, 41))
        self.button_excluir.setStyleSheet("background-color: rgb(76, 84, 86);")
        self.button_excluir.setObjectName("button_excluir")
        self.text_estado = QtWidgets.QLabel(self.centralwidget)
        self.text_estado.setGeometry(QtCore.QRect(760, 10, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.text_estado.setFont(font)
        self.text_estado.setText("")
        self.text_estado.setAlignment(QtCore.Qt.AlignCenter)
        self.text_estado.setObjectName("text_estado")
        self.button_config = QtWidgets.QPushButton(self.centralwidget)
        self.button_config.setGeometry(QtCore.QRect(230, 10, 51, 41))
        self.button_config.setStyleSheet("background-color: rgb(76, 84, 86);")
        self.button_config.setObjectName("button_config")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_criar.setText(_translate("MainWindow", "Criar"))
        self.name_view.setText(_translate("MainWindow", "Arquivo:"))
        self.name_label.setText(_translate("MainWindow", "TextLabel"))
        self.button_salvar.setText(_translate("MainWindow", "salvar"))
        self.button_this.setText(_translate("MainWindow", "This"))
        self.button_excluir.setText(_translate("MainWindow", "exc"))
        self.button_config.setText(_translate("MainWindow", "Conf"))

