from tkinter import *
from tkinter import Toplevel, Label, Entry, Button

from models.DBClasses import Pessoa
from config.DBConnection import *
from tkinter.messagebox import showinfo

from sqlalchemy.exc import IntegrityError

#FUNCÕES DE "Cadastro de pessoa"

def cadastro_pessoa():
    # Função de cadastro de pessoa
    cadastro_pessoa = Toplevel()
    cadastro_pessoa.title("Cadastro de Pessoa")
    cadastro_pessoa.geometry("400x300")
    cadastro_pessoa.configure(background="#dde")

    # Campo Nome
    Label(cadastro_pessoa, text="Nome:", background="#dde", anchor="w").place(x=10, y=30, width=110, height=20)
    nome_entry = Entry(cadastro_pessoa)
    nome_entry.place(x=150, y=30, width=110, height=20)
    
    #Campo Endereço
    Label(cadastro_pessoa, text="Endereço:", background="#dde", anchor="w").place(x=10, y=60, width=110, height=20)
    endereco_entry = Entry(cadastro_pessoa)
    endereco_entry.place(x=150, y=60, width=110, height=20)
    
    #Campo Telefone
    Label(cadastro_pessoa, text="Telefone:", background="#dde", anchor="w").place(x=10, y=90, width=110, height=20)
    telefone_entry = Entry(cadastro_pessoa)
    telefone_entry.place(x=150, y=90, width=110, height=20)

    #Campo E-mail
    Label(cadastro_pessoa, text="E-mail:", background="#dde", anchor="w").place(x=10, y=120, width=110, height=20)
    email_entry = Entry(cadastro_pessoa)
    email_entry.place(x=150, y=120, width=110, height=20)

    def registro_pessoa_BD():
    # Obter os valores dos campos de entrada
        nome = nome_entry.get()
        endereco = endereco_entry.get()
        telefone = telefone_entry.get()
        email = email_entry.get()

        # Criar uma nova instância de Pessoa com os dados inseridos
        nova_pessoa = Pessoa(nm_pessoa=nome, cd_endereco= endereco, nr_telefone=telefone, nm_email=email)

        # Realizar a inserção no banco de dados
        try:
            session.add(nova_pessoa)
            session.commit()
            showinfo("Cadastro de Pessoa", "Cadastro realizado com sucesso!")
        except IntegrityError:
            session.rollback()
            showinfo("Cadastro de Pessoa", "Erro: Ocorreu uma violação de integridade. Verifique os dados inseridos.")
        except Exception as e:
            session.rollback()
            showinfo("Cadastro de Pessoa", f"Erro inesperado: {str(e)}")

        # Limpar os campos de entrada após a inserção
        nome_entry.delete(0, END)
        endereco_entry.delete(0, END)
        telefone_entry.delete(0, END)
        email_entry.delete(0, END)
    Register = Button(cadastro_pessoa, text="Registrar", width=30, command=registro_pessoa_BD)
    Register.place(x=100, y=225)