from sqlalchemy import create_engine, Integer, String, Float, Column, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from datetime import datetime
import pytz

tmz = pytz.timezone('America/Sao_Paulo')

engine = create_engine('sqlite:///finance_db.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    nome = Column(String(80), nullable=False)
    cpf = Column(String(80), nullable=False, unique=True)
    email = Column(String(80), nullable=False, unique=True)
    senha = Column(String(80), nullable=False)
    date = Column(DateTime, default=datetime.now(tmz))
    receita = relationship('Receita')
    despesa = relationship('Despesa')
    
    def __init__(self, nome, cpf, email, senha):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.senha = senha
          

class Instituicao(Base):
    __tablename__ = 'instituicao'
    id = Column(Integer, primary_key=True)
    nome = Column(String(80), nullable=False)
    date = Column(DateTime, default=datetime.now(tmz))
    
    def __init__(self, nome):
        self.nome = nome


class Receita(Base):
    __tablename__ = 'receitas'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    fonte = Column(Integer, ForeignKey('instituicao.id'),nullable=False)
    valor = Column(Float, nullable=False)
    data = Column(DateTime, default=datetime.now(tmz))
    dono = relationship('User', back_populates='receita')
    
    def __init__(self, user_id, fonte, valor):
        self.user_id = user_id
        self.fonte = fonte
        self.valor = valor
        
        
class Despesa(Base):
    __tablename__ = 'despesas'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    fonte = Column(Integer, ForeignKey('instituicao.id'),nullable=False)
    descricao = Column(String(80), nullable=False)
    forma_pagamento = Column(String(80), nullable=False)
    parcelas = Column(Integer, nullable=True)
    valor = Column(Float, nullable=False)
    data = Column(DateTime, default=datetime.now(tmz))
    dono = relationship('User', back_populates='despesa')

Base.metadata.create_all(engine)