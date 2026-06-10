from repositorios import user_repo, produto_repo, ticket_repo
from modules.ligar_db import get_connection

def seed_categorias():
    conn = get_connection()
    cursor = conn.cursor()
    categorias = [
        ('Hardware', 'Problemas com equipamento físico'),
        ('Software', 'Problemas com aplicações e sistemas'),
        ('Rede', 'Problemas de conectividade e rede'),
        ('Acesso', 'Problemas de permissões e acessos'),
        ('Outro', 'Outros problemas não categorizados')
    ]
    for nome, descricao in categorias:
        cursor.execute(
            "INSERT INTO categorias (nome, descricao) VALUES (%s, %s) ON CONFLICT (nome) DO NOTHING",
            (nome, descricao)
        )
    conn.commit()
    conn.close()
    print('| Categorias inseridas!')

def seed_users():
    users = [
        ('Ana Silva',    'ana.silva@itsm.pt',    '912000001', 'admin',   'Segunda a Sexta'),
        ('Bruno Costa',  'bruno.costa@itsm.pt',  '912000002', 'tecnico', 'Segunda a Sexta'),
        ('Carla Mendes', 'carla.mendes@itsm.pt', '912000003', 'tecnico', 'Turnos'),
        ('David Lopes',  'david.lopes@itsm.pt',  '912000004', 'user',    'Segunda a Sexta'),
        ('Eva Martins',  'eva.martins@itsm.pt',  '912000005', 'user',    'Segunda a Sexta'),
    ]
    for nome, email, contacto, tipo, horario in users:
        user_repo.criar_user(nome, email, contacto, tipo, horario)
    print('| Users inseridos!')

def seed_produtos():
    produtos = [
        ('Laptop Dell XPS',    'Hardware', 'SN-DELL-001'),
        ('Monitor LG 27"',     'Hardware', 'SN-LG-001'),
        ('Office 365',         'Software', 'SN-OFF-001'),
        ('Switch Cisco 24P',   'Rede',     'SN-CISCO-001'),
        ('Teclado Logitech',   'Hardware', 'SN-LOG-001'),
    ]
    for nome, categoria, n_serie in produtos:
        produto_repo.criar_produto(nome, categoria, n_serie)
    print('| Produtos inseridos!')

def seed_tickets():
    tickets = [
        (4, 2, 1, 1, 'Alta',   'Laptop não arranca após actualização'),
        (5, 3, 3, 2, 'Média',  'Office 365 não abre no Windows 11'),
        (4, 2, 4, 3, 'Alta',   'Switch sem conectividade na porta 12'),
        (5, 3, 2, 4, 'Baixa',  'Sem acesso à pasta partilhada'),
        (4, 2, 5, 1, 'Baixa',  'Teclas do teclado coladas'),
    ]
    for user_id, tecnico_id, produto_id, categoria_id, prioridade, descricao in tickets:
        ticket_repo.abrir_ticket(user_id, tecnico_id, produto_id, categoria_id, prioridade, descricao)
    print('| Tickets inseridos!')


# CORRER O SEEDING
if __name__ == '__main__':
    print('| A iniciar seeding...')
    seed_categorias()
    seed_users()
    seed_produtos()
    seed_tickets()
    print('| Seeding concluído!')