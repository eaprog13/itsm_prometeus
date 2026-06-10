from datetime import datetime

class Categoria:
    def __init__(self, categoria_id, nome, descricao=None, criado_em=None):
        self.categoria_id = categoria_id
        self.nome = nome
        self.descricao = descricao
        self.criado_em = criado_em or datetime.now()

    def mostrar(self):
        print('\n----------CATEGORIA----------')
        print(f'| Id: {self.categoria_id}\n | Nome: {self.nome}\n | Descrição: {self.descricao}\n | Criado em: {self.criado_em:%d/%m/%Y %H:%M:%S}\n')