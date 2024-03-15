from tkinter import *
from tkinter import Toplevel, Label, Entry, Button
from tkinter import ttk

from sqlalchemy import values

from models.DBClasses import Produto
from config.DBConnection import *
from tkinter.messagebox import showinfo

from sqlalchemy.exc import IntegrityError


# Função para preencher o treeview 
def preencher_tv(tree):
    # for para limpar os dados do treeview, necessario em casos de buscas
    for i in tree.get_children():
        tree.delete(i)

    # Consultar os produtos do Banco de dados
    produtos = session.query(Produto).all()

    # adicionar os dados do produtos no TreeV    
    for produto in produtos:
        tree.insert("","end", values=(produto.nm_produto, produto.ds_produto, produto.tp_embalagemproduto))

# Funcao para abrir a janela de listas de produtos
def lista_produtos():
    # Funcção para  a janela de lista de produtos
    lista_produtos = Toplevel()
    lista_produtos.title("Lista de Produtos")
    lista_produtos.geometry("1000x600")
    lista_produtos.configure(background="#dde")

    # Criacao da TreeView para exibir os prodts
    tview = ttk.Treeview(lista_produtos, columns=("Nome", "Descrição", "Embalagem"))
    tview.heading("Nome", text="Nome")
    tview.heading("Descrição", text="Descrição")
    tview.heading("Embalagem", text="Embalagem")

    # Ocultando a primeira coluna
    tview.column("#0", width=0, stretch=NO)

    # Preencher tview com os dados dos produtos
    preencher_tv(tview) #Chama a função

    #Posicionar o Tview na janela
    tview.place(relx=0, rely=0, relwidth=1, relheight=1)


    