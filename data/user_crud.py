from InquirerPy import prompt
from sqlalchemy.orm.exc import NoResultFound
from .database import User, session
from faker import Faker
from rich.table import Table
from rich import print

ftime = '%d/%m/%Y %H:%M:%S'

fake = Faker('pt_BR')
class UserCrud:
    def __init__(self) -> None:
        pass
    
    def del_conf(self, nome):
        msg = f'Deseja deletar o cadastro {nome}?'
        menu = [
            {
                'type': 'list',
                'message': msg,
                'choices': ['Sim', 'Não'],
                'name': 'c'
            },
        ]
    
        opt = prompt(menu)
        return opt['c']            
    
    def create(self):
        new_user = []
        nome = str(input('Digite o nome completo: ')).strip().title()
        cpf = str(input('Digite o numero do cpf: ')).strip().title()
        email = str(input('Digite o email: ')).strip().lower()
        senha = str(input('Digite a senha: ')).strip()
        try:
            new_user.append(User(nome, cpf, email, senha))
        except Exception as e:
            return print(f'Não foi possível realizar o cadastro de: {nome} \n-{type(e)} \n-Erro: {e}')
        session.bulk_save_objects(new_user)
        session.commit()
        return print(f'O usuário: {nome} foi cadastrado com sucesso!')
        
    def read(self):
        tb = Table(show_lines=True, style='blue')
        tb_header = ['id', 'nome', 'cpf', 'email', 'hora']
        for i in range(len(tb_header)):
            tb.add_column(tb_header[i].upper(), style='green')
        for i in session.query(User).all():
            tb.add_row(str(i.id).zfill(2), i.nome, i.cpf, i.email, i.date.strftime(ftime))
        return print(tb)
    
    def update(self):
        self.read()
        
        try:
            _id = int(input('Digite o ID que deseja atualizar: '))
        except ValueError:
            return print('O valor digitado é inválido')
        except:
            return print('Usuário não encontrado!')
        
        try:
            update = session.query(User).filter_by(id=_id).one()
            if update:
                nome = str(input('Digite o novo nome: ')).strip().title()
                if nome:
                    update.nome = nome
                cpf = str(input('Digite o novo CPF: ')).strip()
                if cpf:
                    update.cpf = cpf
                email = str(input('Digite o novo email: ')).strip().lower()
                if email:
                    update.email = email
            session.add(update)
            session.commit()
            return print(f'{update.nome} atualizado com sucesso!')
        except NoResultFound:
            return print('Usuário não encontrado!')
        except Exception as e:
            return print(f'{type(e)} \n -(Erro: {e})')
            
    def delete(self):
        self.read()
        
        try:
            _id = int(input('Digite o ID que deseja deletar: '))
        except ValueError:
            return print('O valor digitado é inválido')
        except:
            return print('Usuário não encontrado!')
        
        try:
            de = session.query(User).filter_by(id=_id).one()
            deletar = self.del_conf(de.nome)
            if deletar == 'Sim':
                session.delete(de)
                session.commit()
                return print('Cadastro deletado com sucesso!')
            else:
                return print('Operação cancelada!')
        except NoResultFound:
            return print('Usuário não encontrado!')
        except Exception as e:
            return print(f'{type(e)} \n -(Erro: {e})')
        
        