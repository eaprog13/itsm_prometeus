from modules.ligar_db import get_connection
from modules.departamentos import Departamento

def criar_departamento(nome, descricao):
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
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM departamentos WHERE departamento_id = %s", (departamento_id,))
    conn.commit()
    conn.close()
    print(f'| Departamento {departamento_id} eliminado com sucesso!')