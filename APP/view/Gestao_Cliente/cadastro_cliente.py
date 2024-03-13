from tkinter import *
from tkinter import Toplevel, Label, Entry, Button

from models.DBClasses import Cliente
from config.DBConnection import *
from tkinter.messagebox import showinfo

from sqlalchemy.exc import IntegrityError

#FUNCÕES DE "Cadastro de pessoa"

def cadastro_cliente():
    # Função de cadastro de cliente
    cadastro_cliente = Toplevel()
    cadastro_cliente.title("Cadastro de Cliente")
    cadastro_cliente.geometry("400x300")
    cadastro_cliente.configure(background="#dde")

    # Codigo da Pessoa
    Label(cadastro_cliente, text="Codigo da Pessoa:", background="#dde", anchor="w").place(x=10, y=30, width=110, height=20)
    cd_pessoa_entry = Entry(cadastro_cliente)
    cd_pessoa_entry.place(x=150, y=30, width=110, height=20)
    
    #Campo CPF
    Label(cadastro_cliente, text="CPF:", background="#dde", anchor="w").place(x=10, y=60, width=110, height=20)
    cpf_entry = Entry(cadastro_cliente)
    cpf_entry.place(x=150, y=60, width=110, height=20)
    
    #Campo DT NASC
    Label(cadastro_cliente, text="Data de Nascimento:", background="#dde", anchor="w").place(x=10, y=90, width=110, height=20)
    dt_nasc_entry = Entry(cadastro_cliente)
    dt_nasc_entry.place(x=150, y=90, width=110, height=20)

    #Campo GENERO
    Label(cadastro_cliente, text="Gênero:", background="#dde", anchor="w").place(x=10, y=120, width=110, height=20)
    tp_genero_entry = Entry(cadastro_cliente)
    tp_genero_entry.place(x=150, y=120, width=110, height=20)

    def registro_cliente_BD():
    # Obter os valores dos campos de entrada
        cd_pessoa = cd_pessoa_entry.get()
        cpf = cpf_entry.get()
        dt_nasc = dt_nasc_entry.get()
        genero = tp_genero_entry.get()

        # Criar uma nova instância de Pessoa com os dados inseridos
        novo_cliente = Cliente(cd_cliente=cd_pessoa, nr_cpf=cpf, dt_nascimento=dt_nasc, tp_genero=genero)

        # Realizar a inserção no banco de dados
        try:
            session.add(novo_cliente)
            session.commit()
            showinfo("Cadastro de Pessoa", "Cadastro realizado com sucesso!")
        except IntegrityError:
            session.rollback()
            showinfo("Cadastro de Pessoa", "Erro: Ocorreu uma violação de integridade. Verifique os dados inseridos.")
        except Exception as e:
            session.rollback()
            showinfo("Cadastro de Pessoa", f"Erro inesperado: {str(e)}")

        # Limpar os campos de entrada após a inserção
        cd_pessoa_entry.delete(0, END)
        cpf_entry.delete(0, END)
        dt_nasc_entry.delete(0, END)
        tp_genero_entry.delete(0, END)
    Register = Button(cadastro_cliente, text="Registrar", width=30, command=registro_cliente_BD)
    Register.place(x=100, y=225)