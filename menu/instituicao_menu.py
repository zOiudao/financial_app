from InquirerPy import prompt
from data.instituicao_crud import InstituicaoCrud
from .menu_principal import menu_principal

def instituicao_menu():
    inst = InstituicaoCrud()
    menu = [
        {
            'type': 'list',
            'message': 'Menu de Usuários',
            'choices': ['Cadastrar', 'Exibir', 'Editar', 'Deletar', 'Retornar'],
            'name': 'insts'
        },
    ]
    
    opt = prompt(menu)
    inst.create() if opt['insts'] == 'Cadastrar' else ...
    inst.read() if opt['insts'] == 'Exibir' else ...
    inst.update() if opt['insts'] == 'Editar' else ...
    inst.delete() if opt['insts'] == 'Deletar' else ...
    menu_principal() if opt['insts'] == 'Retornar' else ...
