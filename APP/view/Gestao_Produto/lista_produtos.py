from datetime import date
from tkinter import *
from tkinter import Toplevel, Label, Entry, Button
from tkinter import ttk

from sqlalchemy import values

from models.DBClasses import Produto
from config.DBConnection import *
from tkinter.messagebox import showinfo
from models.DBClasses import Produto_estoque
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
        tree.insert("","end", values=(produto.cd_produto,produto.nm_produto, produto.ds_produto, produto.tp_embalagemproduto))


# Funcao para abrir a janela de listas de produtos
def lista_produtos():
    # Funcção para  a janela de lista de produtos
    lista_produtos = Toplevel()
    lista_produtos.title("Lista de Produtos")
    lista_produtos.geometry("1000x450")
    lista_produtos.configure(background="#dde")

    Label(lista_produtos, text="ID produto:", background='#dde', anchor=W).place(x=10, y=30, width=70, height=20)
    id_entry  = Entry(lista_produtos)
    id_entry.place(x=90, y=30, width=110, height=20)

    Label(lista_produtos, text="NR Lote:", background='#dde', anchor=W).place(x=250, y=30, width=70, height=20)
    nr_lote_entry = Entry(lista_produtos)
    nr_lote_entry.place(x=330, y=30, width=70, height=20)

    Label(lista_produtos, text="Quantidade:", background='#dde', anchor=W).place(x=450, y=30, width=70, height=20)
    qt_prod_entry  = Entry(lista_produtos)
    qt_prod_entry.place(x=530, y=30, width=40, height=20)

    Label(lista_produtos, text="Data de validade:", background='#dde', anchor=W).place(x=620, y=30, width=95, height=20)
    dt_validade_entry  = Entry(lista_produtos)
    dt_validade_entry.place(x=725, y=30, width=70, height=20)

    Label(lista_produtos, text="Locação:", background='#dde', anchor=W).place(x=845, y=30, width=60, height=20)
    locacao_entry  = Entry(lista_produtos)
    locacao_entry.place(x=915, y=30, width=40, height=20)

    # Criacao da TreeView para exibir os prodts
    tview = ttk.Treeview(lista_produtos, columns=("ID","Nome", "Descrição", "Embalagem"), show='headings')
    tview.heading("ID", text="ID")
    tview.heading("Nome", text="Nome")
    tview.heading("Descrição", text="Descrição")
    tview.heading("Embalagem", text="Embalagem")
    #Tam. colunas
    tview.column('ID', minwidth=0, width=5)
    tview.column('Nome', minwidth=0, width=200)
    tview.column('Descrição', minwidth=0, width=420)
    tview.column('Embalagem', minwidth=0, width=10)
    # Ocultando a primeira coluna
    tview.column("#0", width=0, stretch=NO)

    # Preencher tview com os dados dos produtos
    preencher_tv(tview) #Chama a função

    #Posicionar o Tview na janela PADX = MARGEM DE FORA ,IPADX = DENTRO
    tview.pack(padx=5, ipadx=120,ipady=240,pady=120, anchor='n')


    def add_produto_estoque():
        
        # Obter os valores dos campos de entrada
        id_produto = id_entry.get()
        numero_lote = nr_lote_entry.get()
        qt_produto = qt_prod_entry.get()
        data_validade = dt_validade_entry.get()
        locacao = locacao_entry.get()

        # Obter a data atual
        dt_prod_estoq = date.today()

        # Criar uma nova instância de Produto_estoque com os dados inseridos
        novo_prod_estoque = Produto_estoque(cd_produto=id_produto, cd_estoque=locacao, nr_lote=numero_lote, qt_produtoestoque= qt_produto, dt_validade=data_validade, dt_produtoestoque=dt_prod_estoq)

        try:
            session.add(novo_prod_estoque)
            session.commit()
            showinfo("Estoque", "Inserção realizada com sucesso!")
        except IntegrityError:
            session.rollback()
            showinfo("Estoque", "Erro: Ocorreu uma violação de integridade. Verifique os dados inseridos.")
        except Exception as e:
            session.rollback()
            showinfo("Estoque", f"Erro inesperado: {str(e)}")
        
        # Limpar os campos de entrada após a inserção
        id_entry.delete(0, END)
        nr_lote_entry.delete(0, END)
        qt_prod_entry.delete(0, END)
        dt_validade_entry.delete(0, END)
        locacao_entry.delete(0, END)

    btn_inserir_estoque = Button(lista_produtos,text="Abastecer estoque", command= add_produto_estoque)
    btn_inserir_estoque.place(x=450, y=70)
