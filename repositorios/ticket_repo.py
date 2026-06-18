from modules.ligar_db import get_connection
from modules.tickets import Ticket

def abrir_ticket(user_id, tecnico_id, produto_id, categoria_id, prioridade, descricao):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tickets (user_id, tecnico_id, produto_id, categoria_id, prioridade, descricao) VALUES (%s, %s, %s, %s, %s, %s) RETURNING ticket_id",
        (user_id, tecnico_id, produto_id, categoria_id, prioridade, descricao)
    )
    ticket_id = cursor.fetchone()[0]
    conn.commit()
    conn.close()
    print(f'| Ticket {ticket_id} aberto com sucesso!')

def listar_tickets():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT 
            t.ticket_id,
            u.nome AS user_nome,
            tec.nome AS tecnico_nome,
            p.nome AS produto_nome,
            c.nome AS categoria_nome,
            t.prioridade,
            t.descricao,
            t.estado,
            t.observacao,
            t.criado_em
        FROM tickets t
        LEFT JOIN users u ON t.user_id = u.user_id
        LEFT JOIN users tec ON t.tecnico_id = tec.user_id
        LEFT JOIN produtos p ON t.produto_id = p.produto_id
        LEFT JOIN categorias c ON t.categoria_id = c.categoria_id
    """)
    rows = cursor.fetchall()
    conn.close()
    if not rows:
        print('| Não existem tickets registados!')
        return []
    for row in rows:
        print('\n----------TICKET----------')
        print(f'| Id: {row[0]}\n | User: {row[1]}\n | Técnico: {row[2]}\n | Produto: {row[3]}\n | Categoria: {row[4]}\n | Prioridade: {row[5]}\n | Descrição: {row[6]}\n | Estado: {row[7]}\n | Observação: {row[8]}\n | Criado em: {row[9]:%d/%m/%Y %H:%M:%S}\n')
    return rows

def obter_ticket(ticket_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT ticket_id, user_id, tecnico_id, produto_id, categoria_id, prioridade, descricao, estado, observacao, criado_em FROM tickets WHERE ticket_id = %s", (ticket_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return Ticket(*row)
    print(f'| Ticket {ticket_id} não encontrado!')
    return None

def editar_ticket(ticket_id, tecnico_id, produto_id, categoria_id, prioridade, descricao):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE tickets SET tecnico_id=%s, produto_id=%s, categoria_id=%s, prioridade=%s, descricao=%s WHERE ticket_id=%s",
        (tecnico_id, produto_id, categoria_id, prioridade, descricao, ticket_id)
    )
    conn.commit()
    conn.close()
    print(f'| Ticket {ticket_id} actualizado com sucesso!')

def fechar_ticket(ticket_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE tickets SET estado='fechado' WHERE ticket_id=%s", (ticket_id,))
    conn.commit()
    conn.close()
    print(f'| Ticket {ticket_id} fechado com sucesso!')

def reabrir_ticket(ticket_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE tickets SET estado='aberto' WHERE ticket_id=%s", (ticket_id,))
    conn.commit()
    conn.close()
    print(f'| Ticket {ticket_id} reaberto com sucesso!')

def eliminar_ticket(ticket_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tickets WHERE ticket_id=%s", (ticket_id,))
    conn.commit()
    conn.close()
    print(f'| Ticket {ticket_id} eliminado com sucesso!')
    
def devolver_ticket(ticket_id, observacao):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE tickets SET estado='devolvido', observacao=%s WHERE ticket_id=%s",
        (observacao, ticket_id)
    )
    conn.commit()
    conn.close()
    print(f'| Ticket {ticket_id} devolvido com sucesso!')

def listar_tickets_por_user(user_id):
    print(f'| A procurar tickets do user_id: {user_id}')  # ← debug temporário
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT 
            t.ticket_id,
            u.nome AS user_nome,
            tec.nome AS tecnico_nome,
            p.nome AS produto_nome,
            c.nome AS categoria_nome,
            t.prioridade,
            t.descricao,
            t.estado,
            t.observacao,
            t.criado_em
        FROM tickets t
        LEFT JOIN users u ON t.user_id = u.user_id
        LEFT JOIN users tec ON t.tecnico_id = tec.user_id
        LEFT JOIN produtos p ON t.produto_id = p.produto_id
        LEFT JOIN categorias c ON t.categoria_id = c.categoria_id
        WHERE t.user_id = %s
    """, (user_id,))
    rows = cursor.fetchall()
    print(f'| Tickets encontrados: {len(rows)}')  # ← debug temporário
    conn.close()
    if not rows:
        print('| Não tens tickets registados!')
        return []
    for row in rows:
        print('\n----------TICKET----------')
        print(f'| Id: {row[0]}\n | User: {row[1]}\n | Técnico: {row[2]}\n | Produto: {row[3]}\n | Categoria: {row[4]}\n | Prioridade: {row[5]}\n | Descrição: {row[6]}\n | Estado: {row[7]}\n | Observação: {row[8]}\n | Criado em: {row[9]:%d/%m/%Y %H:%M:%S}\n')
    return rows

def obter_tecnico_disponivel():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT u.user_id, u.nome, COUNT(t.ticket_id) AS total_tickets
        FROM users u
        LEFT JOIN tickets t 
            ON u.user_id = t.tecnico_id 
            AND t.estado IN ('aberto', 'devolvido')
        WHERE u.tipo = 'tecnico'
        GROUP BY u.user_id, u.nome
        ORDER BY total_tickets ASC
        LIMIT 1
    """)
    row = cursor.fetchone()
    conn.close()
    if row:
        print(f'| Técnico atribuído: {row[1]} (tickets activos: {row[2]})')
        return row[0]
    print('| Não há técnicos disponíveis!')
    return None

def listar_tickets_por_tecnico(tecnico_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT 
            t.ticket_id,
            u.nome AS user_nome,
            p.nome AS produto_nome,
            c.nome AS categoria_nome,
            t.prioridade,
            t.descricao,
            t.estado,
            t.observacao,
            t.criado_em
        FROM tickets t
        LEFT JOIN users u ON t.user_id = u.user_id
        LEFT JOIN produtos p ON t.produto_id = p.produto_id
        LEFT JOIN categorias c ON t.categoria_id = c.categoria_id
        WHERE t.tecnico_id = %s
        AND t.estado IN ('aberto', 'devolvido')
        ORDER BY 
            CASE t.prioridade
                WHEN 'Alta'  THEN 1
                WHEN 'Média' THEN 2
                WHEN 'Baixa' THEN 3
            END ASC,
            t.criado_em ASC
    """, (tecnico_id,))
    rows = cursor.fetchall()
    conn.close()
    if not rows:
        print('| Não tens tickets na fila!')
        return []
    for row in rows:
        print('\n----------TICKET----------')
        print(f'| Id: {row[0]}\n | User: {row[1]}\n | Produto: {row[2]}\n | Categoria: {row[3]}\n | Prioridade: {row[4]}\n | Descrição: {row[5]}\n | Estado: {row[6]}\n | Observação: {row[7]}\n | Criado em: {row[8]:%d/%m/%Y %H:%M:%S}\n')
    return rows