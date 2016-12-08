import requests
import json
from datetime import datetime
import hashlib
import time
from tkinter import *
from celery import Celery

#from funcoes.botao import *



print ("Ola mundo")
version="2016-12-07"

def bt_logar():
    #print(login.get())
    GetLogin=login.get()
    GetSenha=senha.get()
    #print ("Abaixo valor de senha")
    #print(senha.get())
    if (len(GetLogin) > 0 and len(GetSenha) > 0 and GetLogin.count('@')==1):
        print("Foi clicando o botao")
        lb["text"]="Autenticando"
        print ("Abaixo valor de login")
    
        try:
            doc_data={}
            query=json.dumps(doc_data)
            url="http://10.130.75.196:9200/tkinterchat/email/"
            url_completa=url+GetLogin
            resposta=requests.post(url_completa,data=query)
            #print(response)
            #print "criando documentos com a data de: "+data_time
        except:
            #print(resposta)
            lb["text"]="Erro na Conexao"
    else:
        print("Login ou senha invalidos")
        lb["text"]="Login e/ou senha invalidas"
        
def bt_cadastro():
    janelacadastro= Tk()
    janelacadastro.title("Novo cadastro")
    janelacadastro["bg"]="grey"
    janelacadastro["bg"]="grey"
    #Largura x Altura + espaço esquerdo + espaço topo
    janelacadastro.geometry("300x200")

    lb_nome=Label(janelacadastro, text="Nome completo")
    nomecompleto=Entry(janelacadastro,width=50)
    nomecompleto.place(x=10,y=100)
    lb_nome.pack()

    lb_email=Label(janelacadastro, text="email")
    lb_email.pack()
    emailcadastro=Entry(janelacadastro,width=50)
    emailcadastro.place(x=10,y=130)

    lb_senha=Label(janelacadastro, text="senha")
    lb_senha.pack()
    senhacadastro=Entry(janelacadastro,width=50,show="*")
    senhacadastro.place(x=10,y=160)

janela= Tk()
janela.title("Tkinter Chat Versão"+version)
janela["bg"]="grey"
janela["bg"]="grey"
#Largura x Altura + espaço esquerdo + espaço topo
janela.geometry("260x500")


login=Entry(janela,width=40)
login.place(x=10,y=100)
senha=Entry(janela,width=40)
senha.place(x=10,y=120)


lb=Label(janela, text="Aguardando autenticação ...")
lb.pack()

bt=Button(janela, width=10, text="OK",command=bt_logar)
bt.place(x=100 , y=150)

bt_cadastro=Button(janela, width=20, text="Cadastre-se",command=bt_cadastro)
bt_cadastro.place(x=60 , y=300)

#lb=Label(janela,text="Teste")
#lb.place(x=10, y=10)






janela.mainloop()