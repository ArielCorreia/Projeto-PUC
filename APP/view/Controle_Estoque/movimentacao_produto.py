from datetime import datetime
from tkinter import messagebox, ttk
from tkinter import *
from tkinter import Toplevel, Label, Entry, Button
from config.DBConnection import *
from models.produto_estoque import Produto_estoque, Estoque, Produto



    
def consultar_movimentacao():
    global codigo_prod_entry

    janela_consulta_produto = Toplevel()
    janela_consulta_produto.title("Movimentação do Produto")
    janela_consulta_produto.geometry("900x400")
    janela_consulta_produto.configure(background="#dde")

    Label(janela_consulta_produto, text="Código do produto:", background="#dde", anchor="w").place(x=10, y=30, width=110, height=20)
    codigo_prod_entry = Entry(janela_consulta_produto)
    codigo_prod_entry.place(x=150, y=30, width=60, height=20)


    Label(janela_consulta_produto, text="Data inicio:", background="#dde", anchor="w").place(x=450, y=30, width=110, height=20)
    data_inicio_entry = Entry(janela_consulta_produto)
    data_inicio_entry.place(x=540, y=30, width=80, height=20)

    
    Label(janela_consulta_produto, text="Data fim:", background="#dde", anchor="w").place(x=670, y=30, width=110, height=20)
    data_fim_entry = Entry(janela_consulta_produto)
    data_fim_entry.place(x=750, y=30, width=80, height=20)

    ## Treeview
    tview = ttk.Treeview(janela_consulta_produto, columns=("ID", "Nome", "Quantidade", "Operação", "Data da operação"), show="headings")
    tview.heading("ID", text="ID")
    tview.heading("Nome", text="Nome")
    tview.heading("Quantidade", text="Quantidade")
    tview.heading("Operação", text="Operação")
    tview.heading("Data da operação", text="Data da operação")


    tview.column('ID', minwidth=0, width=5)
    tview.column('Nome', minwidth=0, width=200)
    tview.column('Quantidade', minwidth=0, width=35)
    tview.column('Operação', minwidth=0, width=35)
    tview.column('Data da operação', minwidth=0, width=70)


    # Ocultando a primeira coluna
    tview.column("#0", width=0, stretch=NO)

    tview.pack(padx=0, ipadx=190,ipady=240,pady=120, anchor='n')    

    def movimentacao_produto():
        try:
            cd_produto = codigo_prod_entry.get()
            data_inicio = datetime.strptime(data_inicio_entry.get(), '%d/%m/%Y')
            data_fim = datetime.strptime(data_fim_entry.get(), '%d/%m/%Y')

            # Consultar movimentação do produto no estoque
            movimentacoes = session.query(Produto_estoque, Produto).join(Produto).filter(
                Produto_estoque.cd_produto == cd_produto,
                Produto_estoque.dt_produtoestoque.between(data_inicio, data_fim)
            ).all()

            # Limpar Treeview 
            for i in tview.get_children():
                tview.delete(i)

            # Preencher o Treeview 
            for movimentacao, produto in movimentacoes:
                operacao = "Entrada" if movimentacao.qt_produtoestoque > 0 else "Saída"
                descricao = operacao
                
                
                if produto.nm_produto != movimentacao.Produto.nm_produto:
                    descricao = "Alterado nome"
                elif produto.vl_produto != movimentacao.Produto.vl_produto:
                    descricao = "Alterado valor"
                
                tview.insert("", "end", values=(
                    movimentacao.cd_produto,
                    produto.nm_produto,  # Nome do produto
                    descricao,  # Descrição da operação (entrada, saída, alteração de nome ou valor)
                    movimentacao.dt_produtoestoque.strftime("%d/%m/%Y")  # Data da movimentação
                ))
        except ValueError:
            messagebox.showerror("Erro", "Data inválida. Por favor, insira a data no formato DD/MM/AAAA.")
        except Exception as e:
            messagebox.showerror("Erro no banco de dados", f"Ocorreu um erro ao consultar o banco de dados: {str(e)}")

    btn_buscar = Button(janela_consulta_produto, text="Buscar Movimentação", command=movimentacao_produto)
    btn_buscar.place(x=30, y=60)

    janela_consulta_produto.mainloop()



