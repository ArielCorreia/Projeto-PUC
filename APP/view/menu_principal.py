import sys
sys.path.append ("D:\Programa de desenvolvimneto gti\Banco de dados\APP")

from config.DBConnection import *

from view.Atendimento.registro_pedido import *
from view.Atendimento.consulta_pedido import *

from view.Controle_Estoque.lista_estoque import lista_produtos_estoque
from view.Controle_Estoque.consultar_produto import consultar_produto_estoque
from view.Controle_Estoque.alterar_locacao import lista_prod_locacao

from view.Cadastros.cadastro_produto import cadastro_produto
from view.Cadastros.cadastro_cliente import cadastro_cliente_PF,cadastro_cliente_PJ

from view.Gestao.produto.atualizacao_produto import atualiza_produto
from view.Gestao.produto.lista_produtos import *
from view.Gestao.produto.remover_produto import remover_produto

from view.Gestao.cliente.lista_clientes import lista_pessoas
from view.Gestao.cliente.remover_cliente import remover_cliente_fisico, remover_cliente_juridico

from tkinter import *


#Janela PRINCIPAL = app
app = Tk()
app.title("App Controle de Estoque")
app.geometry("800x500")
app.configure(background="#dde")

app.attributes('-fullscreen', True)

## Menu ##

# Atendimento
Barra_menu = Menu(app)

atendimento = Menu(Barra_menu, tearoff=0)
atendimento.add_command(label="Registrar Pedido",command= None)
atendimento.add_command(label="Atender Pedido",command= None)
Barra_menu.add_cascade(label="Atendimento",menu=atendimento)


# Controle de estoque
controle_est = Menu(Barra_menu, tearoff=0)
controle_est.add_command(label="Produtos em Estoque",command= lista_produtos_estoque)
controle_est.add_separator()
controle_est.add_command(label="Consultar Produto",command= consultar_produto_estoque)
controle_est.add_separator()
controle_est.add_command(label="Alterar Locação",command= lista_prod_locacao)
Barra_menu.add_cascade(label="Controle de Estoque",menu=controle_est)

# Gestão de produtos 
gestao_prod = Menu(Barra_menu, tearoff=0)
gestao_prod.add_command(label="Atualização de Produto",command= atualiza_produto)
gestao_prod.add_command(label="Remoção de Produto",command= remover_produto)
gestao_prod.add_separator()
gestao_prod.add_command(label="Lista de Produtos",command= lista_produtos)
Barra_menu.add_cascade(label="Gestão de Produtos",menu=gestao_prod)

# Gestão de  Clientes
gestao_cliente = Menu(Barra_menu, tearoff=0)
gestao_cliente.add_command(label="Atualização de Pessoa Física",command= None)
gestao_cliente.add_command(label="Atualização de Pessoa Jurídica",command= None)
gestao_cliente.add_separator()
gestao_cliente.add_command(label="Remoção de Pessoa Física",command= remover_cliente_fisico)
gestao_cliente.add_command(label="Remoção de Pessoa Jurídica",command= remover_cliente_juridico)
gestao_cliente.add_separator()
gestao_cliente.add_command(label="Lista de clientes",command= lista_pessoas)
Barra_menu.add_cascade(label="Gestão de Clientes",menu=gestao_cliente)


# Cadastros
cadastros = Menu(Barra_menu, tearoff=0)
cadastros.add_command(label="Cadastro de Pessoa Física",command=cadastro_cliente_PF)
cadastros.add_command(label="Cadastro de Pessoa Jurídica",command=cadastro_cliente_PJ)
cadastros.add_separator()
cadastros.add_command(label="Cadastro de Produto",command=cadastro_produto)
Barra_menu.add_cascade(label="Cadastros",menu=cadastros)

# Sistema - Fechar
menu_fechar = Menu(Barra_menu, tearoff=0)
menu_fechar.add_command(label="Fechar",command= app.quit)
Barra_menu.add_cascade(label="Sistema",menu=menu_fechar)


app.config(menu=Barra_menu)
app.mainloop()



