from InquirerPy import prompt
from os import system

def menu_principal():
    from .user_menu import user_menu
    from .driver_menu import driver_menu
    system('clear')
    print('MENU PRINCIPAL')
    menu = [
        {
            'type': 'list',
            'message': 'Selecine abaixo',
            'choices': ['Usuários', 'Motoristas', 'Chaves', 'EPIs', 'Sair'],
            'name': 'choice'
        },
    ]
    
    opt = prompt(menu)
    if opt['choice'] == 'Usuários':
        user_menu()
        
    if opt['choice'] == 'Motoristas':
        driver_menu()
        
    if opt['choice'] == 'Chaves':
        'chave_menu'
        
    if opt['choice'] == 'EPIs':
        'epi_menu'
        
    if opt['choice'] == 'Sair':
        system('clear')
        return print('Sistema encerrado. \n-Volte sempre!')