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