from .database import Driver, session, User
from sqlalchemy.orm.exc import NoResultFound
from InquirerPy import prompt
from rich import print
from rich.table import Table
ftime = '%d/%m/%Y %H:%M:%S'

class DriverCrud:
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
        create = []
        user_id = ''
        nome = str(input('Nome do motorista: ')).strip().title()
        cpf = str(input('CPF: ')).strip()
        trans = str(input('Transportadora: ')).strip().title()
        placa = str(input('Placa: ')).strip().upper()
        nome_user = str(input('Nome usuário: ')).strip().title()
        
        while True:
            try:
                user_id = session.query(User).filter(User.nome.like(f'%{nome_user}%')).first()
                if user_id:
                    user_id = user_id.id
                    break
            except:
                print('Usuário não encontrado')
                
        try:
            create.append(Driver(nome, cpf, trans, placa, user_id))
        except:
            return print('Erro!')
        
        session.bulk_save_objects(create)
        session.commit()
        return print(f'O cadastro do motorista: {nome} foi realizado com sucesso!')
    
    
    def read(self):
        tb = Table(show_lines=True, style='blue')
        tb_header = ['id', 'nome', 'cpf', 'transportadora', 'placa', 'hora']
        for i in range(len(tb_header)):
            tb.add_column(tb_header[i].upper(), style='green')
        for i in session.query(Driver).all():
            tb.add_row(str(i.id).zfill(2), i.nome, i.cpf, i.transportadora, i.placa, i.date.strftime(ftime))
        return print(tb)
    
    
    def update(self):
        self.read()
        while True:
            try:
                _id = int(input('Digite o ID do motorista que pretende editar: '))
                update = session.query(Driver).filter_by(id=_id).one()
                if update:
                    nome = str(input('Digite nome atualizado: ')).strip().title()
                    if nome:
                        update.nome = nome
                    cpf = str(input('Digite o CPF: ')).strip()
                    if cpf:
                        update.cpf = cpf
                    trans = str(input('Digite transportadora: ')).strip().title()
                    if trans:
                        update.transportadora = trans
                    placa = str(input('Digite a placa: ')).strip().upper()
                    if placa:
                        update.placa = placa
                break
            except TypeError:
                print('Valor digitado inválido!')
                
        session.add(update)
        session.commit()
        return print(f'{nome} atualizado com sucesso!')
    
    
    def delete(self):
        self.read()
        try:
            _id = int(input('Digite o ID do motorista que pretende deletar: '))
            de = session.query(Driver).filter_by(id=_id).one()
            if de:
                conf = self.del_conf(de.nome)
                if conf == 'Sim':
                    session.delete(de)
                    session.commit()
                    return print('Cadastro deletado com sucesso!')
                else:
                    return print('Operação cancelada')   
        except NoResultFound:
            return print('Motorista não encontrado!')
        except Exception as e:
            return print(f'{type(e)} \n -(Erro: {e})')
        