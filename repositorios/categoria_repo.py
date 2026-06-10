from modules.ligar_db import get_connection
from modules.categorias import Categoria

def criar_categoria(nome, descricao):
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
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM categorias WHERE categoria_id = %s", (categoria_id,))
    conn.commit()
    conn.close()
    print(f'| Categoria {categoria_id} eliminada com sucesso!')