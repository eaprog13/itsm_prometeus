from modules.ligar_db import get_connection
from modules.users import User


def criar_user(nome, email, contacto, tipo, departamento_id, turno, password):
    """
    Cria um novo user na base de dados.

    Args:
        nome (str): Nome completo do user.
        email (str): Email do user, deve conter '@'.
        contacto (str): Número de contacto, só dígitos.
        tipo (str): Perfil do user — 'admin', 'tecnico' ou 'user'.
        departamento_id (int): ID do departamento ao qual o user pertence.
        turno (str): Turno de trabalho — 'Manhã', 'Tarde' ou 'Noite'.
        password (str): Password do user, mínimo 6 caracteres.

    Returns:
        None. Imprime uma mensagem de confirmação com o ID gerado.
    """
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
    """
    Lista todos os users registados na base de dados.

    Returns:
        list[User]: Lista de objectos User. Lista vazia se não houver nenhum.
    """
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
    """
    Procura um user pelo seu ID.

    Args:
        user_id (int): ID do user a procurar.

    Returns:
        User | None: O objecto User se encontrado, ou None caso contrário.
    """
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
    """
    Procura um user pelo seu email — usado principalmente no login.

    Args:
        email (str): Email do user a procurar.

    Returns:
        User | None: O objecto User se encontrado, ou None caso contrário.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT user_id, nome, email, contacto, tipo, departamento_id, turno, password, criado_em FROM users WHERE email = %s", (email,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return User(*row)
    return None


def editar_user(user_id, nome, email, contacto, tipo, departamento_id, turno, password):
    """
    Actualiza os dados de um user existente.

    Args:
        user_id (int): ID do user a editar.
        nome (str): Novo nome.
        email (str): Novo email.
        contacto (str): Novo contacto.
        tipo (str): Novo tipo ('admin', 'tecnico' ou 'user').
        departamento_id (int): Novo ID do departamento.
        turno (str): Novo turno.
        password (str): Nova password.

    Returns:
        None. Imprime uma mensagem de confirmação.
    """
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
    """
    Elimina um user da base de dados pelo seu ID.

    Args:
        user_id (int): ID do user a eliminar.

    Returns:
        None. Imprime uma mensagem de confirmação.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE user_id = %s", (user_id,))
    conn.commit()
    conn.close()
    print(f'| User {user_id} eliminado com sucesso!')