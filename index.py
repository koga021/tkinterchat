from tkinter import *

#from funcoes.botao import *



print ("Ola mundo")
version="2016-12-07"

def bt_click():
    print("Foi clicando o botao")
    lb["text"]="Autenticando"


janela= Tk()

login=Entry(janela)
login.place(x=75,y=100)
senha=Entry(janela)
senha.place(x=75,y=120)


lb=Label(janela, text="Aguardando autenticação ...")
bt=Button(janela, width=10, text="OK",command=bt_click)
bt.place(x=100 , y=150)

#lb=Label(janela,text="Teste")
#lb.place(x=10, y=10)

janela.title("Tkinter Chat Versão"+version)
janela["bg"]="grey"
janela["bg"]="grey"
#Largura x Altura + espaço esquerdo + espaço topo
janela.geometry("250x500")


lb.pack()

janela.mainloop()