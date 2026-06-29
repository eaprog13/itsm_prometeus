from modules.ligar_db import get_connection
from modules.categorias import Categoria


def criar_categoria(nome, descricao):
    """
    Cria uma nova categoria de tickets na base de dados.

    Args:
        nome (str): Nome da categoria, deve ser único.
        descricao (str): Descrição da categoria.

    Returns:
        None. Imprime uma mensagem de confirmação com o ID gerado.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO categorias (nome, descricao) VALUES (%s, %s) RETURNING categoria_id",
        (nome, descricao)
    )
    categoria_id = cursor.fetchone()[0]
    conn.commit()
    conn.close()
    print(f'| Categoria {nome} criada com sucesso! ID: {categoria_id}')


def listar_categorias():
    """
    Lista todas as categorias registadas na base de dados.

    Returns:
        list[Categoria]: Lista de objectos Categoria. Lista vazia se não houver nenhuma.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT categoria_id, nome, descricao, criado_em FROM categorias")
    rows = cursor.fetchall()
    conn.close()
    categorias = [Categoria(*row) for row in rows]
    if not categorias:
        print('| Não existem categorias registadas!')
    for c in categorias:
        c.mostrar()
    return categorias


def obter_categoria(categoria_id):
    """
    Procura uma categoria pelo seu ID.

    Args:
        categoria_id (int): ID da categoria a procurar.

    Returns:
        Categoria | None: O objecto Categoria se encontrado, ou None caso contrário.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT categoria_id, nome, descricao, criado_em FROM categorias WHERE categoria_id = %s", (categoria_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return Categoria(*row)
    print(f'| Categoria {categoria_id} não encontrada!')
    return None


def editar_categoria(categoria_id, nome, descricao):
    """
    Actualiza os dados de uma categoria existente.

    Args:
        categoria_id (int): ID da categoria a editar.
        nome (str): Novo nome.
        descricao (str): Nova descrição.

    Returns:
        None. Imprime uma mensagem de confirmação.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE categorias SET nome=%s, descricao=%s WHERE categoria_id=%s",
        (nome, descricao, categoria_id)
    )
    conn.commit()
    conn.close()
    print(f'| Categoria {categoria_id} actualizada com sucesso!')


def eliminar_categoria(categoria_id):
    """
    Elimina uma categoria da base de dados pelo seu ID.

    Args:
        categoria_id (int): ID da categoria a eliminar.

    Returns:
        None. Imprime uma mensagem de confirmação.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM categorias WHERE categoria_id = %s", (categoria_id,))
    conn.commit()
    conn.close()
    print(f'| Categoria {categoria_id} eliminada com sucesso!')