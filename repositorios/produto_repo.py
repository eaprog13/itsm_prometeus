from modules.ligar_db import get_connection
from modules.produtos import Produto


def criar_produto(nome, categoria, marca, n_serie):
    """
    Cria um novo produto na base de dados.

    Args:
        nome (str): Nome do produto.
        categoria (str): Categoria do produto (ex: 'Hardware', 'Software').
        marca (str): Marca/fabricante do produto.
        n_serie (str): Número de série, deve ser único.

    Returns:
        None. Imprime uma mensagem de confirmação com o ID gerado.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO produtos (nome, categoria, marca, n_serie) VALUES (%s, %s, %s, %s) RETURNING produto_id",
        (nome, categoria, marca, n_serie)
    )
    produto_id = cursor.fetchone()[0]
    conn.commit()
    conn.close()
    print(f'| Produto {nome} criado com sucesso! ID: {produto_id}')


def listar_produtos():
    """
    Lista todos os produtos registados na base de dados.

    Returns:
        list[Produto]: Lista de objectos Produto. Lista vazia se não houver nenhum.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT produto_id, nome, categoria, marca, n_serie, criado_em FROM produtos")
    rows = cursor.fetchall()
    conn.close()
    produtos = [Produto(*row) for row in rows]
    if not produtos:
        print('| Não existem produtos registados!')
    for p in produtos:
        p.mostrar()
    return produtos


def obter_produto(produto_id):
    """
    Procura um produto pelo seu ID.

    Args:
        produto_id (int): ID do produto a procurar.

    Returns:
        Produto | None: O objecto Produto se encontrado, ou None caso contrário.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT produto_id, nome, categoria, marca, n_serie, criado_em FROM produtos WHERE produto_id = %s", (produto_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return Produto(*row)
    print(f'| Produto {produto_id} não encontrado!')
    return None


def editar_produto(produto_id, nome, categoria, marca, n_serie):
    """
    Actualiza os dados de um produto existente.

    Args:
        produto_id (int): ID do produto a editar.
        nome (str): Novo nome.
        categoria (str): Nova categoria.
        marca (str): Nova marca.
        n_serie (str): Novo número de série.

    Returns:
        None. Imprime uma mensagem de confirmação.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE produtos SET nome=%s, categoria=%s, marca=%s, n_serie=%s WHERE produto_id=%s",
        (nome, categoria, marca, n_serie, produto_id)
    )
    conn.commit()
    conn.close()
    print(f'| Produto {produto_id} actualizado com sucesso!')


def eliminar_produto(produto_id):
    """
    Elimina um produto da base de dados pelo seu ID.

    Args:
        produto_id (int): ID do produto a eliminar.

    Returns:
        None. Imprime uma mensagem de confirmação.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM produtos WHERE produto_id = %s", (produto_id,))
    conn.commit()
    conn.close()
    print(f'| Produto {produto_id} eliminado com sucesso!')