from modules.ligar_db import get_connection
from modules.produtos import Produto

def criar_produto(nome, categoria, marca, n_serie):
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
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM produtos WHERE produto_id = %s", (produto_id,))
    conn.commit()
    conn.close()
    print(f'| Produto {produto_id} eliminado com sucesso!')