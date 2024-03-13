import sys
sys.path.append ("D:\Programa de desenvolvimneto gti\Banco de dados\APP")

from config.DBConnection import *

from Atendimento.registro_pedido import *
from Atendimento.consulta_pedido import *
from view.Cadastro_Pessoa.cadastro_pessoa import *
from view.Gestao_Cliente.cadastro_cliente import *
from view.Gestao_Produto.cadastro_produto import *

from tkinter import *
from tkinter import Tk



#Criação da Janela PRINCIPAL = app
app = Tk()
app.title("App Controle de Estoque")
app.geometry("635x300")
app.configure(background="#dde")

## Menu ##

# Atendimento
Barra_menu = Menu(app)

atendimento = Menu(Barra_menu, tearoff=0)
atendimento.add_command(label="Registrar Pedido",command= registrar_pedido)
atendimento.add_command(label="Consultar Pedidos",command= consultar_pedido)
Barra_menu.add_cascade(label="Atendimento",menu=atendimento)


# Controle de estoque
controle_est = Menu(Barra_menu, tearoff=0)
controle_est.add_command(label="Consulta de Estoque",command= None)
controle_est.add_command(label="Registro de Entrada",command= None)
controle_est.add_command(label="Registro de Saída",command= None)
Barra_menu.add_cascade(label="Controle de Estoque",menu=controle_est)

# Gestão de produtos 
gestao_prod = Menu(Barra_menu, tearoff=0)
gestao_prod.add_command(label="Cadastro de Produto",command= cadastro_produto)
gestao_prod.add_command(label="Atualização de Produto",command= None)
gestao_prod.add_command(label="Remoção de Produto",command= None)
Barra_menu.add_cascade(label="Gestão de Produtos",menu=gestao_prod)

# Gestão de clientes 
gestao_cliente = Menu(Barra_menu, tearoff=0)
gestao_cliente.add_command(label="Cadastro de Cliente",command= cadastro_cliente)
gestao_cliente.add_command(label="Atualização de Cliente",command= None)
gestao_cliente.add_command(label="Remoção de Cliente",command= None)
Barra_menu.add_cascade(label="Gestão de Clientes",menu=gestao_cliente)

# Gestão de fornecedores 
gestao_fornecedor = Menu(Barra_menu, tearoff=0)
gestao_fornecedor.add_command(label="Cadastro de Fornecedor",command= None)
gestao_fornecedor.add_command(label="Atualização de Fornecedor",command= None)
gestao_fornecedor.add_command(label="Remoção de Fornecedor",command= None)
Barra_menu.add_cascade(label="Gestão de Fornecedores",menu=gestao_fornecedor)

# Cadastro Pessoa
gestao_pessoa = Menu(Barra_menu, tearoff=0)
gestao_pessoa.add_command(label="Cadastro de Pessoa",command= cadastro_pessoa)
Barra_menu.add_cascade(label="Cadastro de Pessoa",menu=gestao_pessoa)

# Sistema - Fechar
menu_fechar = Menu(Barra_menu, tearoff=0)
menu_fechar.add_command(label="Fechar",command= app.quit)
Barra_menu.add_cascade(label="Sistema",menu=menu_fechar)


app.config(menu=Barra_menu)
app.mainloop()

