from modules.ligar_db import get_connection
from modules.departamentos import Departamento


def criar_departamento(nome, descricao):
    """
    Cria um novo departamento na base de dados.

    Args:
        nome (str): Nome do departamento, deve ser único.
        descricao (str): Descrição do departamento.

    Returns:
        None. Imprime uma mensagem de confirmação com o ID gerado.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO departamentos (nome, descricao) VALUES (%s, %s) RETURNING departamento_id",
        (nome, descricao)
    )
    departamento_id = cursor.fetchone()[0]
    conn.commit()
    conn.close()
    print(f'| Departamento {nome} criado com sucesso! ID: {departamento_id}')


def listar_departamentos():
    """
    Lista todos os departamentos registados na base de dados.

    Returns:
        list[Departamento]: Lista de objectos Departamento. Lista vazia se não houver nenhum.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT departamento_id, nome, descricao FROM departamentos")
    rows = cursor.fetchall()
    conn.close()
    departamentos = [Departamento(*row) for row in rows]
    if not departamentos:
        print('| Não existem departamentos registados!')
    for d in departamentos:
        d.mostrar()
    return departamentos


def obter_departamento(departamento_id):
    """
    Procura um departamento pelo seu ID.

    Args:
        departamento_id (int): ID do departamento a procurar.

    Returns:
        Departamento | None: O objecto Departamento se encontrado, ou None caso contrário.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT departamento_id, nome, descricao FROM departamentos WHERE departamento_id = %s", (departamento_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return Departamento(*row)
    print(f'| Departamento {departamento_id} não encontrado!')
    return None


def editar_departamento(departamento_id, nome, descricao):
    """
    Actualiza os dados de um departamento existente.

    Args:
        departamento_id (int): ID do departamento a editar.
        nome (str): Novo nome.
        descricao (str): Nova descrição.

    Returns:
        None. Imprime uma mensagem de confirmação.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE departamentos SET nome=%s, descricao=%s WHERE departamento_id=%s",
        (nome, descricao, departamento_id)
    )
    conn.commit()
    conn.close()
    print(f'| Departamento {departamento_id} actualizado com sucesso!')


def eliminar_departamento(departamento_id):
    """
    Elimina um departamento da base de dados pelo seu ID.

    Args:
        departamento_id (int): ID do departamento a eliminar.

    Returns:
        None. Imprime uma mensagem de confirmação.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM departamentos WHERE departamento_id = %s", (departamento_id,))
    conn.commit()
    conn.close()
    print(f'| Departamento {departamento_id} eliminado com sucesso!')