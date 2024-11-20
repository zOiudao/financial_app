from data.user_crud import UserCrud
from InquirerPy import prompt


user = UserCrud()
def user_menu():
    from .menu_principal import menu_principal
    menu = [
        {
            'type': 'list',
            'message': 'Menu de Usuários',
            'choices': ['Cadastrar', 'Exibir', 'Editar', 'Deletar', 'Retornar'],
            'name': 'users'
        },
    ]
    
    opt = prompt(menu)
    user.create() if opt['users'] == 'Cadastrar' else ...
    user.read() if opt['users'] == 'Exibir' else ...
    user.update() if opt['users'] == 'Editar' else ...
    user.delete() if opt['users'] == 'Deletar' else ...
    menu_principal() if opt['users'] == 'Retornar' else ...