from InquirerPy import prompt
from os import system

def menu_principal():
    from .user_menu import user_menu
    from .instituicao_menu import instituicao_menu
    system('clear')
    print('MENU PRINCIPAL')
    menu = [
        {
            'type': 'list',
            'message': 'Selecine abaixo',
            'choices': ['Usuários', 'Receitas', 'Despesas', 'Exibir', 'Sair'],
            'name': 'choice'
        },
    ]
    
    opt = prompt(menu)
    if opt['choice'] == 'Usuários':
        user_menu()
        
    if opt['choice'] == 'Receitas':
        instituicao_menu()
        
    if opt['choice'] == 'Despesas':
        'chave_menu'
        
    if opt['choice'] == 'Exibir':
        'epi_menu'
        
    if opt['choice'] == 'Sair':
        system('clear')
        return print('Sistema encerrado. \n-Volte sempre!')