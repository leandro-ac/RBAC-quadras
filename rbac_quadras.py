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
    
# Classe que simula o sistema de agendamento de quadras
class SistemaQuadras:
    def __init__(self):
        # Inicializa o sistema com uma lista de usuários
        self.usuarios = []

    def adicionar_usuario(self, nome, papel):
        # Adiciona um novo usuário ao sistema
        usuario = Usuario(nome, papel)
        self.usuarios.append(usuario)
        print(f"Usuário {nome} adicionado como {papel}.")

    def verificar_acesso(self, nome_usuario, acao):
        # Verifica se um usuário tem permissão para realizar uma ação
        for usuario in self.usuarios:
            if usuario.nome == nome_usuario:
                if usuario.tem_permissao(acao):
                    print(f"{nome_usuario} Possui permissão para {acao}.")
                else:
                    print(f"{nome_usuario} Não Possui permissão para {acao}.")
                return
        print(f"Usuário {nome_usuario} Não encontrado.")