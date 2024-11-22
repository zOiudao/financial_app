from InquirerPy import prompt
from sqlalchemy.orm.exc import NoResultFound
from database import Instituicao, session
from faker import Faker
from rich.table import Table
from rich import print

ftime = '%d/%m/%Y %H:%M:%S'

fake = Faker('pt_BR')
class InstituicaoCrud:
    def __init__(self) -> None:
        pass
    
    def create(self):
        nome = str(input('Digite o nome da instituição \n-(receita ou despesa): ')).strip().title()
        try:
            new = Instituicao(nome)
            session.add(new)
            session.commit()
            return print(f'{new.nome} -Cadastrado com sucesso!')
        except:
            return print(f'Não foi possível realizar o cadastro de {nome}')
        
        
    def read(self):
        tb = Table(show_lines=True, style='blue')
        tb_header = ['id', 'nome', 'hora']
        for i in range(len(tb_header)):
            tb.add_column(tb_header[i].upper(), style='green')
        for i in session.query(Instituicao).all():
            tb.add_row(str(i.id), i.nome, i.date.strftime(ftime))
        return print(tb)
    
    
    def update():
        pass
    
    
    def delete():
        pass