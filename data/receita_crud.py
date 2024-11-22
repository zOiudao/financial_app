from InquirerPy import prompt
from sqlalchemy.orm.exc import NoResultFound
from database import Receita, User, Instituicao, session
from faker import Faker
from rich.table import Table
from rich import print

ftime = '%d/%m/%Y %H:%M:%S'
fake = Faker('pt_BR')


class ReceitaCrud:
    def __init__(self) -> None:
        pass
    
    def create(self):
        new = []
        nome = str(input('Digite seu nome: ')).strip()
        inst = str(input('Digite a insituição: ')).strip()
        valor = str(input('Digite o valor: ')).strip().replace(',', '.')
        try:
            u = session.query(User).filter(User.nome.like(f'%{nome}%')).one()
            i = session.query(Instituicao).filter(Instituicao.nome.like(f'%{inst}%')).one()
        except NoResultFound:
            return print('Usuário não encontrado!')
        user_id = u.id if u else print('Usuário não encontrado!')
        fonte = i.id if i else print('Instituição não encontrada!')
        valor = float(valor) if valor.isnumeric() else print('Valor digitado não é número')
        
        try:
            new.append(Receita(user_id, fonte, valor))
        except:
            return print(f'Não foi possível realizar o cadastro de: {nome} \n-{type(e)} \n-Erro: {e}')
        session.bulk_save_objects(new)
        session.commit()
        return print('Receita cadastrada com sucesso!')
    
    
    def read(self):
        tb = Table(show_lines=True, style='blue')
        tb_header = ['id', 'nome', 'instituição', 'valor']
        for i in range(len(tb_header)):
            tb.add_column(tb_header[i].upper())
        for i in session.query(Receita).all():
            tb.add_row(str(i.id), i.dono.nome, i.fonte.nome, f'{i.valor:2.f}')
        return print(tb)