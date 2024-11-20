from sqlalchemy import create_engine, Integer, String, Float, Column, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from datetime import datetime
import pytz

tmz=pytz.timezone('America/Sao_Paulo')

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
    
    def __init__(self, nome, cpf, email, senha):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.senha = senha
        

class Driver(Base):
    __tablename__ = 'drivers'
    id = Column(Integer, primary_key=True)
    nome = Column(String(80), nullable=False)
    cpf = Column(String(80), nullable=False, unique=True)
    transportadora = Column(String(80), nullable=False)
    placa = Column(String(80), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    date = Column(DateTime, default=datetime.now(tmz))
    
    def __init__(self, nome, cpf, trans, placa, user_id):
        self.nome = nome
        self.cpf = cpf
        self.transportadora = trans
        self.placa = placa
        self.user_id = user_id
        

class Worker(Base):
    __tablename__ = 'workers'
    id = Column(Integer, primary_key=True)
    nome = Column(String(80), nullable=False)
    funcional = Column(String(80), nullable=False, unique=True)
    

Base.metadata.create_all(engine)