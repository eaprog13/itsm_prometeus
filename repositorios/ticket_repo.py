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
    cursor.execute("SELECT ticket_id, user_id, tecnico_id, produto_id, categoria_id, prioridade, descricao, estado, criado_em FROM tickets")
    rows = cursor.fetchall()
    conn.close()
    tickets = [Ticket(*row) for row in rows]
    if not tickets:
        print('| Não existem tickets registados!')
    for t in tickets:
        t.mostrar()
    return tickets

def obter_ticket(ticket_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT ticket_id, user_id, tecnico_id, produto_id, categoria_id, prioridade, descricao, estado, criado_em FROM tickets WHERE ticket_id = %s", (ticket_id,))
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