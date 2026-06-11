from datetime import datetime

class Produto:
    def __init__(self, produto_id, nome, categoria, marca, n_serie, criado_em=None):
        self.produto_id = produto_id
        self.nome = nome
        self.categoria = categoria
        self.marca = marca
        self.n_serie = n_serie
        self.criado_em = criado_em or datetime.now()

    def mostrar(self):
        print('\n----------PRODUTO----------')
        print(f'Id: {self.produto_id}\n | Nome: {self.nome}\n | Categoria: {self.categoria}\n | Marca: {self.marca}\n | NºSérie: {self.n_serie}\n | Criado em: {self.criado_em:%d/%m/%Y %H:%M:%S}\n')