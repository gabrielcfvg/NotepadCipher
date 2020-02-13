from cipherdef import cipher
from os import system
from sys import exit as sys_exit
from tkinter import filedialog as dialog
import os


local = r'/home/stalin/Desktop/projetos/Notepad_Cipher'
editor_de_texto = 'mousepad'

def clear():
    system('cls' if os.name == 'nt' else 'clear')

def select():

    if os.getcwd() != local:
        os.chdir(local)

    if not os.path.exists(local + "/arquivos"):
        print("Nenhum arquivo foi encontrado")
        return 1
        
    files = os.listdir(local + '/arquivos')

    if len(files) == 0:
        print("Nenhum arquivo encontrado")
        return 1

    n1 = 1
    print('\n', '-'*30, '\n', sep='')
    for A in files:
        print(f"{n1} = {A}")
        n1 += 1
    print('\n', '-'*30, sep='')
    
    escolha = int(input("\nDigite o número referente ao arquivo desejado:\n"))-1

    if escolha < 0 or escolha > n1:
        clear()
        print("Número invalido, tente novamente!")
        return select()
    
    else:

        return files[escolha]   

def abrir(file, senha):

    with open(local + "/arquivos/" + file, 'r', encoding='utf-8-sig') as arquivo:

        with open(local+"/temptxt.txt", 'w', encoding='utf-8') as saida:

            saida.write(cipher(arquivo.read(), senha, 2))

            saida.close()
            arquivo.close()

        system(f"{editor_de_texto} {local+'/temptxt.txt'}")

    with open(local+"/temptxt.txt", 'r', encoding='utf-8-sig') as arquivo:

        with open(local + "/arquivos/" + file, 'w', encoding='utf-8') as saida:

            saida.write(cipher(arquivo.read(), senha, 1,))

            arquivo.close()
            saida.close()

    os.remove(local+"/temptxt.txt")

#==========================================================================

while True:
    clear()

    print("="*20)
    print("="*2, " NOTEPAD CIPHER ", "="*2, sep='')
    print("="*20)

    print("\nOperações:\n\n",
        "1 = Visualizar arquivo\n", 
        "2 = Criar novo arquivo\n", 
        "3 = Importar novo arquivo\n", 
        "4 = Decriptar/Exportar arquivo existente\n",
        "5 = Excluir arquivo\n\n",
        "999 = Sair",
        sep='')

    operação = int(input("\nDigite a operação selecionada: "))
    clear()


    if operação == 1:

        saida = select()

        if saida == 1:
            pass

        else:
            clear()
            senha = input("Digite a senha que será utilizada para abrir o arquivo: ")
            abrir(saida, senha)

    elif operação == 2:
        clear()

        nome = input("Digite o nome do arquivo á ser criado: ")
        
        open(local+"/arquivos/"+nome+".txt", 'w', encoding='utf-8')

    elif operação == 3:
        clear()

        arq = dialog.askopenfile()
        arquivo = arq.name
        tipo = arq.encoding
        print(tipo)

        senha = input("Digite a senha que será usada para criptografar o arquivo; ")

        with open(f"{local}/arquivos/{arquivo.split('/')[-1]}.txt", 'w', encoding="utf-8") as saida:

            with open(arquivo, 'r', encoding=tipo) as entrada:

                saida.write(cipher(entrada.read(), senha, 1))

                saida.close()
                entrada.close()
        
    elif operação == 4:
        clear()

        alvo = dialog.askdirectory()
        arq = select()

        senha = input("Digite a senha que será usada para criptografar o arquivo; ")

        with open(local+"/arquivos/"+arq, 'r', encoding='utf-8-sig') as entrada:

            with open(alvo+"/"+arq, 'w', encoding='utf-8') as saida:

                saida.write(cipher(entrada.read(), senha, 2))

                saida.close()
                entrada.close()
    
    elif operação == 5:
        clear()

        from random import randint

        arq = select()
        con = randint(100, 1000)
        if int(input(f"Digite o número {con} para confirmar: ")) == con:
            os.remove(local+"/arquivos/"+arq)
        
        else:
            print("Não foi possivel deletar")


    if input("Deseja continuar?\n\n1 = Não\n2 = Sim\n\n") == '1':
        break
