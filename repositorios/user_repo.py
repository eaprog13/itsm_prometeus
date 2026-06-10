from modules.ligar_db import get_connection
from modules.users import User

def criar_user(nome, email, contacto, tipo, departamento_id, turno, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (nome, email, contacto, tipo, departamento_id, turno, password) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING user_id",
        (nome, email, contacto, tipo, departamento_id, turno, password)
    )
    user_id = cursor.fetchone()[0]
    conn.commit()
    conn.close()
    print(f'| User {nome} criado com sucesso! ID: {user_id}')

def listar_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT user_id, nome, email, contacto, tipo, departamento_id, turno, password, criado_em FROM users")
    rows = cursor.fetchall()
    conn.close()
    users = [User(*row) for row in rows]
    if not users:
        print('| Não existem users registados!')
    for u in users:
        u.mostrar()
    return users

def obter_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT user_id, nome, email, contacto, tipo, departamento_id, turno, password, criado_em FROM users WHERE user_id = %s", (user_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return User(*row)
    print(f'| User {user_id} não encontrado!')
    return None

def obter_user_por_email(email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT user_id, nome, email, contacto, tipo, departamento_id, turno, password, criado_em FROM users WHERE email = %s", (email,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return User(*row)
    return None

def editar_user(user_id, nome, email, contacto, tipo, departamento_id, turno, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE users SET nome=%s, email=%s, contacto=%s, tipo=%s, departamento_id=%s, turno=%s, password=%s WHERE user_id=%s",
        (nome, email, contacto, tipo, departamento_id, turno, password, user_id)
    )
    conn.commit()
    conn.close()
    print(f'| User {user_id} actualizado com sucesso!')

def eliminar_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE user_id = %s", (user_id,))
    conn.commit()
    conn.close()
    print(f'| User {user_id} eliminado com sucesso!')