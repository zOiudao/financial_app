from data.driver_crud import DriverCrud
from InquirerPy import prompt


motorista = DriverCrud()
def driver_menu():
    from .menu_principal import menu_principal
    menu = [
        {
            'type': 'list',
            'message': 'Menu de Motoristas',
            'choices': ['Cadastrar', 'Exibir', 'Editar', 'Deletar', 'Retornar'],
            'name': 'moto'
        },
    ]
    
    opt = prompt(menu)
    motorista.create() if opt['moto'] == 'Cadastrar' else ...
    motorista.read() if opt['moto'] == 'Exibir' else ...
    motorista.update() if opt['moto'] == 'Editar' else ...
    motorista.delete() if opt['moto'] == 'Deletar' else ...
    menu_principal() if opt['moto'] == 'Retornar' else ...