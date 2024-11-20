from data.user_crud import UserCrud
from InquirerPy import prompt
from os import system

user = UserCrud()

def user_menu():
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
        