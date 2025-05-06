## Implementação de um RBAC simples para um sistema de agendamento de quadras esportivas ##

# Dicionário que define os papéis e suas permissões
RBAC_ROLES = {
    'Jogador': {
        'visualizar_quadras_disponiveis': True,
        'agendar_quadra': True,
        'cancelar_proprio_agendamento': True,
        'gerenciar_agendamentos': False,
        'gerenciar_manutencao': False,
        'gerenciar_usuarios': False
    },
    'Secretario': {
        'visualizar_quadras_disponiveis': True,
        'agendar_quadra': False,
        'cancelar_proprio_agendamento': False,
        'gerenciar_agendamentos': True,
        'gerenciar_manutencao': True,
        'gerenciar_usuarios': False
    },
    'Administrador': {
        'visualizar_quadras_disponiveis': True,
        'agendar_quadra': True,
        'cancelar_proprio_agendamento': True,
        'gerenciar_agendamentos': True,
        'gerenciar_manutencao': True,
        'gerenciar_usuarios': True
    }
}

# Classe que representa um usuário no sistema
class Usuario:
    def __init__(self, nome, papel):
        # Inicializa o usuário com um nome e um papel
        self.nome = nome
        self.papel = papel

    def tem_permissao(self, acao):
        # Verifica se o usuário tem permissão para realizar uma ação específica
        return RBAC_ROLES[self.papel].get(acao, False)