from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
from app.config.database import db

Base = declarative_base()

class Usuario(Base):
    #Definindo Características da tabela no banco.
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(150))
    email = Column(String(150))
    senha = Column(String(150))

    def __init__(self, nome: str, email: str, senha: str):
        self.nome = self._verificar_nome_usuario(nome)
        self.email = self._verificar_email_usuario(email)
        self.senha = self._verificar_senha_usuario(senha)

    def _verificar_nome_usuario(self, nome):
        self._verificar_nome_invalido(nome)  # Verifica se o nome é inválido primeiro
        self._verificar_nome_vazio(nome)      # Depois verifica se está vazio
        return nome

    def _verificar_email_usuario(self, email):
        self._verificar_email_invalido(email)
        self._verificar_email_vazio(email)
        return email

    def _verificar_senha_usuario(self, senha):
        self._verificar_senha_vazio(senha)
        self._verificar_senha_invalido(senha)
        return senha

    def _verificar_nome_vazio(self, nome):
        if nome == "":
            raise ValueError("O que está sendo solicitado está vazio.")

    def _verificar_nome_invalido(self, nome):
        if not isinstance(nome, str):
            raise TypeError("O que está sendo solicitado está inválido.")

    def _verificar_email_vazio(self, email):
        if email == "":
            raise ValueError("O que está sendo solicitado está vazio.")

    def _verificar_email_invalido(self, email):
        if not isinstance(email, str):
            raise TypeError("O que está sendo solicitado está inválido.")

    def _verificar_senha_vazio(self, senha):
        if senha == "":
            raise ValueError("O que está sendo solicitado está vazio.")

    def _verificar_senha_invalido(self, senha):
        if not isinstance(senha, str):
            raise TypeError("O que está sendo solicitado está inválido.")

    #Definindo Características da Classe.;
    def __init__(self, nome:str, email:str, senha:str):
        self.nome = nome
        self.email = email
        self.senha = senha

    def __repr__(self):
        return f"Usuario: \nID: {self.id}\nNome: {self.nome}\nEmail: {self.email}"

Base.metadata.create_all(bind=db)


