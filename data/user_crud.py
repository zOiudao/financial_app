from .database import User, session
from faker import Faker
from rich.table import Table
from rich import print

ftime = '%d/%m/%Y %H:%M:%S'

fake = Faker('pt_BR')
class UserCrud:
    def __init__(self) -> None:
        pass
    
    def create(self, num=5):
        new_user = []
        for _ in range(num):
            nome = fake.name()
            cpf = fake.cpf()
            email = fake.free_email()
            senha = fake.password()
            try:
                new_user.append(User(nome, cpf, email, senha))
            except Exception as e:
                print(e)
        session.bulk_save_objects(new_user)
        session.commit()
        
    def read(self):
        tb = Table(show_lines=True, style='blue')
        tb_header = ['id', 'nome', 'cpf', 'email', 'hora']
        for i in range(len(tb_header)):
            tb.add_column(tb_header[i].upper(), style='green')
        for i in session.query(User).all():
            tb.add_row(str(i.id).zfill(2), i.nome, i.cpf, i.email, i.date.strftime(ftime))
        return print(tb)
        