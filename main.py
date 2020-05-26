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

        from random import randint
        
        self.textos = {"exemplo": f"texto de exemplo!\n{randint(1, 999999999)}"}
    
    def salvar(self):

        sqlite_crud.atualizar(tabela="users", v1="binário", v2=(Funções.serializar(self, SENHA)), v3="nome", v4=NOME)


class Texto:

    def __init__(self, nome, texto):
        self.nome = nome
        self.texto = texto
        self.salvo = True
    
    def atualizar(self, texto):
        self.texto = texto
    
    def salvar(self):

        OBJETO_USUARIO.textos[self.nome] = self.texto
        self.salvo = True
    
    def delete(self):

        del OBJETO_USUARIO.textos[self.nome]


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

        self.carregar_textos()
        self.textEdit.textChanged.connect(lambda: TEXTOS[self.activetext].atualizar(self.textEdit.toPlainText()))
        self.button_salvar.clicked.connect(lambda: TEXTOS[self.activetext].salvar())
        self.button_criar.clicked.connect(lambda: self.criar_texto())


    def carregar_textos(self):

        for A in TEXTOS:
            self.verticalLayout.addWidget(self.gerar_botão(A))
            
    def layout_click(self, botão):

        print("clicado", botão)
        self.activetext = botão
        self.name_label.setText(botão)
        self.textEdit.setText(TEXTOS[botão].texto)

    def gerar_botão(self, nome):

        sizepolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)

        bt = QtWidgets.QPushButton()
        bt.setText(nome)
        bt.setSizePolicy(sizepolicy)
        bt.setStyleSheet("background-color: rgb(76, 84, 86);")
        bt.clicked.connect(lambda: self.layout_click(nome))

        bt.id = nome
        return bt

    def criar_texto(self, nome="NovoTexto"):
        
        if nome in TEXTOS:

            print("nome em uso")
            return
        
        else:

            TEXTOS[nome] = Texto(nome, '')

            self.verticalLayout.addWidget(self.gerar_botão(nome))


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
        
        print(OBJETO_USUARIO.textos)
        OBJETO_USUARIO.salvar()




