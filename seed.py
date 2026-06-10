from repositorios import user_repo, produto_repo, ticket_repo, departamento_repo, categoria_repo


def seed_departamentos():
    departamentos = [
        ('IT',         'Departamento de Tecnologias de Informação'),
        ('Suporte',    'Helpdesk e suporte técnico'),
        ('Financeiro', 'Departamento Financeiro'),
        ('RH',         'Recursos Humanos'),
        ('Gestão',     'Gestão e Administração'),
    ]
    for nome, descricao in departamentos:
        departamento_repo.criar_departamento(nome, descricao)
    print('| Departamentos inseridos!')

def seed_categorias():
    categorias = [
        ('Hardware', 'Problemas com equipamento físico'),
        ('Software', 'Problemas com aplicações e sistemas'),
        ('Rede',     'Problemas de conectividade e rede'),
        ('Acesso',   'Problemas de permissões e acessos'),
        ('Outro',    'Outros problemas não categorizados'),
    ]
    for nome, descricao in categorias:
        categoria_repo.criar_categoria(nome, descricao)
    print('| Categorias inseridas!')

def seed_users():
    users = [
        ('Ana Silva',    'ana.silva@itsm.pt',    '912000001', 'admin',   1, 'Manhã', 'admin123'),
        ('Bruno Costa',  'bruno.costa@itsm.pt',  '912000002', 'tecnico', 2, 'Manhã', 'tecnico123'),
        ('Carla Mendes', 'carla.mendes@itsm.pt', '912000003', 'tecnico', 2, 'Tarde', 'tecnico456'),
        ('David Lopes',  'david.lopes@itsm.pt',  '912000004', 'user',    3, 'Manhã', 'user123'),
        ('Eva Martins',  'eva.martins@itsm.pt',  '912000005', 'user',    4, 'Manhã', 'user456'),
    ]
    for nome, email, contacto, tipo, departamento_id, turno, password in users:
        user_repo.criar_user(nome, email, contacto, tipo, departamento_id, turno, password)
    print('| Users inseridos!')

def seed_produtos():
    produtos = [
        ('Laptop Dell XPS',  'Hardware', 'Dell',      'SN-DELL-001'),
        ('Monitor LG 27"',   'Hardware', 'LG',        'SN-LG-001'),
        ('Office 365',       'Software', 'Microsoft', 'SN-OFF-001'),
        ('Switch Cisco 24P', 'Rede',     'Cisco',     'SN-CISCO-001'),
        ('Teclado Logitech', 'Hardware', 'Logitech',  'SN-LOG-001'),
    ]
    for nome, categoria, marca, n_serie in produtos:
        produto_repo.criar_produto(nome, categoria, marca, n_serie)
    print('| Produtos inseridos!')

def seed_tickets():
    tickets = [
        (4, 2, 1, 1, 'Alta',  'Laptop não arranca após actualização'),
        (5, 3, 3, 2, 'Média', 'Office 365 não abre no Windows 11'),
        (4, 2, 4, 3, 'Alta',  'Switch sem conectividade na porta 12'),
        (5, 3, 2, 4, 'Baixa', 'Sem acesso à pasta partilhada'),
        (4, 2, 5, 1, 'Baixa', 'Teclas do teclado coladas'),
    ]
    for user_id, tecnico_id, produto_id, categoria_id, prioridade, descricao in tickets:
        ticket_repo.abrir_ticket(user_id, tecnico_id, produto_id, categoria_id, prioridade, descricao)
    print('| Tickets inseridos!')


if __name__ == '__main__':
    print('| A iniciar seeding...')
    seed_departamentos()
    seed_categorias()
    seed_users()
    seed_produtos()
    seed_tickets()
    print('| Seeding concluído!')