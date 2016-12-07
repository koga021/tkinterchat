from tkinter import *

#from funcoes.botao import *



print ("Ola mundo")
version="2016-12-07"

def bt_click():
    print("Foi clicando o botao")
    lb["text"]="Autenticando"


janela= Tk()



lb=Label(janela, text="Aguardando autenticação ...")
bt=Button(janela, width=20, text="OK",command=bt_click)
bt.place(x=10 , y=100)

#lb=Label(janela,text="Teste")
#lb.place(x=10, y=10)

janela.title("Tkinter Chat Versão"+version)
janela["bg"]="grey"
janela["bg"]="grey"
#Largura x Altura + espaço esquerdo + espaço topo
janela.geometry("250x500")


lb.pack()

janela.mainloop()