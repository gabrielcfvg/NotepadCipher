from PyQt5 import QtCore, QtGui, QtWidgets
from LoginWindow import Ui_LoginWindow
from MainWindow import Ui_MainWindow
from NewFileDialog import Ui_Dialog
from ConfirmDialog import Ui_Dialog as Ui_confirm

import dependencias.sqlite_crud as sqlite_crud
import dependencias.cipherdef as cipherdef
import pickle
import hashlib
from base64 import b64decode, b64encode
from random import randint, seed
from time import time

##################################################################################################################
#                                                                                                                #
#                                    Declaração de variaveis e constantes                                        #
#                                                                                                                #
##################################################################################################################

sqlite_crud.conectar("database.db")
NOME = ''
SENHA = ''
OBJETO_USUARIO = None
logado = False
TEXTOS = {}


##################################################################################################################
#                                                                                                                #
#                                             Funções e Classes                                                  #
#                                                                                                                #
##################################################################################################################

class User:

    def __init__(self):
        
        self.textos = {"exemplo": f"texto de exemplo!\n{randint(1, 999999999)}"}
    
    def salvar(self):

        sqlite_crud.atualizar(tabela="users", v1="binário", v2=(Funções.serializar(self, SENHA)), v3="nome", v4=NOME)


class Texto:

    def __init__(self, nome, texto):
        self.nome = nome
        self.texto = texto
        self.salvo = True

        if not nome in OBJETO_USUARIO.textos:
            OBJETO_USUARIO.textos[nome] = texto
    
    def atualizar(self, texto):
        self.texto = texto
    
    def salvar(self):

        OBJETO_USUARIO.textos[self.nome] = self.texto
        self.salvo = True
    
    def delete(self):

        del OBJETO_USUARIO.textos[self.nome]


class DialogNewWindow(Ui_Dialog):

    def __init__(self, Dialog):
        super().setupUi(Dialog)

        self.dia = Dialog
        self.button_cancelar.clicked.connect(self.dia.done)
        self.button_ok.clicked.connect(self.bt)

    def bt(self):

        cont = self.lineEdit.text()

        if len(cont) == 0:
            self.label_nomeemuso.setText("Campo vazio!")

        elif cont in TEXTOS:

            self.label_nomeemuso.setText("Nome em uso!")

        else:
            ui.criar_texto(cont)
            self.dia.done(0)


class ConfirmDialog(Ui_confirm):

    def __init__(self, Dialog, nome, func):
        super().setupUi(Dialog)

        self.func = func
        self.label_nome.setText(nome)
        seed(time())
        self.labe_num.setText(str(randint(100, 999)))
        self.dia = Dialog

        self.button_cancelar.clicked.connect(self.dia.done)
        self.button_ok.clicked.connect(self.bt)

    def bt(self):
        
        cont = self.lineEdit.text()

        if cont.isalnum():

            if int(cont) == int(self.labe_num.text()):
                self.func()
                self.dia.done(0)

            else:
                self.label_res.setText("Número errado!")

        else:
            self.label_res.setText("Número errado!")


class JanelaLogin(Ui_LoginWindow):

    def __init__(self, MainWindow):
        super().setupUi(MainWindow)

        self.radioButton_login.setChecked(True)
        self.button_login.clicked.connect(self.login)

    def login(self):

        if all([self.line_nome.text(), self.line_senha.text()]):
            nome = self.line_nome.text()
            senha = self.line_senha.text()
        else:
            self.label.setText("Dados inválidos!!!")
            return

        if self.radioButton_login.isChecked():
            res = Funções.login(nome, senha)

            if res == 0:
                global logado
                logado = True

                MainWindow.close()
            elif res == 1:
                self.label.setText("Senha incorreta!!!")
            elif res == 2:
                self.label.setText("Usuário não existente!!")
            
        else:
            
            res = Funções.cadastro(nome, senha)

            if res == 0:
                self.label.setText("Cadastrado com sucesso!!")
            elif res == 1:
                self.label.setText("Nome em uso!!!")


class JanelaPrincipal(Ui_MainWindow):

    def __init__(self, MainWindow):
        super().setupUi(MainWindow)


        self.activetext = ''
        self.text_estado.setText("")
        
        self.carregar_textos()
        self.textEdit.textChanged.connect(self.digitado)
        
        self.button_salvar.clicked.connect(self.salvar)
        self.button_criar.clicked.connect(self.criar_texto_dialog)
        self.button_excluir.clicked.connect(self.deletar_botao_dialog)
        self.clear()

    #ok
    def digitado(self):

        if self.activetext != None:
            TEXTOS[self.activetext].atualizar(self.textEdit.toPlainText())
            TEXTOS[self.activetext].salvo = False
            self.text_estado.setText("Não salvo!")

    #ok
    def salvar(self):

        if self.activetext != None:
            TEXTOS[self.activetext].salvo = True
            self.text_estado.setText("Salvo")
            
            TEXTOS[self.activetext].atualizar(self.textEdit.toPlainText())
            TEXTOS[self.activetext].salvar()
            
            open(f"./saves/{self.activetext}.txt", 'w', encoding="utf-8").write(cipherdef.cipher(self.textEdit.toPlainText(), SENHA, 1))

    #ok
    def carregar_textos(self):

        for A in TEXTOS:
            self.verticalLayout.addWidget(self.gerar_botão(A))

    #ok
    def layout_click(self, botão):

        self.activetext = None
        self.name_label.setText(botão)
        self.textEdit.setText(TEXTOS[botão].texto)
        self.textEdit.setReadOnly(False)
        
        self.text_estado.setText("Salvo" if TEXTOS[botão].salvo == True else "Não salvo!")
        self.activetext = botão

    #ok
    def gerar_botão(self, nome):

        sizepolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)

        bt = QtWidgets.QPushButton()
        bt.setText(nome)
        bt.setSizePolicy(sizepolicy)
        bt.setStyleSheet("background-color: rgb(76, 84, 86);")
        bt.clicked.connect(lambda: self.layout_click(nome))

        bt.id = nome
        return bt

    def criar_texto_dialog(self):
        
        Dialog = QtWidgets.QDialog(MainWindow)
        ui3 = DialogNewWindow(Dialog)
        Dialog.exec()
        
        del Dialog, ui3

    #ok?
    def criar_texto(self, nome="NovoTexto"):

            TEXTOS[nome] = Texto(nome, '')
            self.verticalLayout.addWidget(self.gerar_botão(nome))

    def deletar_botao_dialog(self):

        Dialog = QtWidgets.QDialog(MainWindow)
        ui3 = ConfirmDialog(Dialog, "Confirmar exlusão", self.deletar_botão)
        Dialog.exec()
        
        del Dialog, ui3

    def deletar_botão(self):

        for A in range(self.verticalLayout.count()):
                    
            if not self.verticalLayout.itemAt(A): continue

            if self.activetext == self.verticalLayout.itemAt(A).widget().id:
                self.verticalLayout.takeAt(A).widget().deleteLater()

                TEXTOS[self.activetext].delete()
                del TEXTOS[self.activetext]

                if A > 0:
                    self.layout_click(self.verticalLayout.itemAt(A-1).widget().id)
                
                elif self.verticalLayout.count()>0:
                    self.layout_click(self.verticalLayout.itemAt(A).widget().id)
               
                else:
                    self.clear()

    #ok
    def clear(self):

        self.activetext = None
        self.name_label.setText("")
        self.textEdit.clear()
        self.textEdit.setReadOnly(True)
        self.text_estado.setText("")


class Funções:

    @staticmethod
    def login(nome, senha):

        data = sqlite_crud.selecionar(tabela="users", v1='hash', v2="nome", v3=nome)

        if data:

            senha_hash = str(hashlib.sha256(bytes(senha, "utf-8")).hexdigest())

            if senha_hash == data:
            
                global SENHA, OBJETO_USUARIO, NOME

                NOME = nome
                SENHA = senha
                #OBJETO_USUARIO = pickle.loads(b64decode(cipherdef.cipher(b64decode(sqlite_crud.selecionar(tabela='users', v1='binário', v2='nome', v3=nome)),senha, 2)))
                OBJETO_USUARIO = Funções.deserializar(sqlite_crud.selecionar(tabela='users', v1='binário', v2='nome', v3=nome), senha)
                return 0

            else:
                return 1 #senha incorreta

        else:
            return 2 #usuário não existente

    @staticmethod
    def cadastro(nome, senha):

        data = sqlite_crud.selecionar(tabela="users", v1='nome', v2="nome", v3=nome)

        if data:
            return 1 # nome em uso

        else:

            senha_hash = hashlib.sha256(bytes(senha, "utf-8")).hexdigest()

            obj = User()
            obj = Funções.serializar(obj, senha)

            sqlite_crud.inserir(tabela='users', valores=[nome, senha_hash, obj])

            return 0

    @staticmethod
    def carregar_textos():

        for A, B in OBJETO_USUARIO.textos.items():

            TEXTOS[A] = Texto(A, B)

    @staticmethod
    def serializar(obj, senha):
        
        obj = pickle.dumps(obj)
        obj = b64encode(obj).decode("utf-8")
        obj = cipherdef.cipher(obj, senha, 1)
        obj = bytes(obj, 'utf-8')
        obj = b64encode(obj).decode("utf-8")
        return obj
        

    @staticmethod
    def deserializar(obj, senha):
        
        obj = b64decode(obj).decode('utf-8')
        obj = cipherdef.cipher(obj, senha, 2)
        obj = b64decode(obj)
        obj = pickle.loads(obj)
        return obj



##################################################################################################################
#                                                                                                                #
#                                             Programa principal                                                 #
#                                                                                                                #
##################################################################################################################


if __name__ == "__main__":
    import types
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = JanelaLogin(MainWindow)
    #MainWindow.closeEvent = types.MethodType(saida, MainWindow)
    MainWindow.show()
    app.exec_()
    

    if logado:

        Funções.carregar_textos()

        app2 = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = JanelaPrincipal(MainWindow)
        MainWindow.show()
        app2.exec_()
        
        OBJETO_USUARIO.salvar()




