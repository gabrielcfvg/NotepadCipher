from PyQt5 import QtCore, QtGui, QtWidgets
from LoginWindow import Ui_LoginWindow
from MainWindow import Ui_MainWindow

import dependencias.sqlite_crud as sqlite_crud
import dependencias.cipherdef as cipherdef
import pickle
import hashlib
from base64 import b64decode, b64encode

##################################################################################################################
#                                                                                                                #
#                                    Declaração de variaveis e constantes                                        #
#                                                                                                                #
##################################################################################################################

sqlite_crud.conectar("database.db")
SENHA = ''
OBJETO_USUARIO = None
logado = False

##################################################################################################################
#                                                                                                                #
#                                             Funções e Classes                                                  #
#                                                                                                                #
##################################################################################################################

class User:

    def __init__(self):

        from random import randint

        self.textos = {"exemplo": f"texto de exemplo!\n{randint(1, 999999999)}"}


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

        self.button_salvar.clicked.connect(lambda: print(OBJETO_USUARIO.textos))

   ''' 
    def add_button(self):

    
    def load(self):

        for A in OBJETO_USUARIO.textos:'''




class Funções:

    @staticmethod
    def login(nome, senha):

        data = sqlite_crud.selecionar(tabela="users", v1='hash', v2="nome", v3=nome)

        if data:

            senha_hash = str(hashlib.sha256(bytes(senha, "utf-8")).hexdigest())

            if senha_hash == data:
            
                global SENHA, OBJETO_USUARIO

                SENHA = senha
                OBJETO_USUARIO = pickle.loads(b64decode(cipherdef.cipher(sqlite_crud.selecionar(tabela='users', v1='binário', v2='nome', v3=nome),senha, 2)))
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
            obj = cipherdef.cipher(b64encode(pickle.dumps(obj)).decode("utf-8"), senha, 1)

            sqlite_crud.inserir(tabela='users', valores=[nome, senha_hash, obj])

            return 0

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
        app2 = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = JanelaPrincipal(MainWindow)
        MainWindow.show()
        app2.exec_()


