class Departamento:
    def __init__(self, departamento_id, nome, descricao=None):
        self.departamento_id = departamento_id
        self.nome = nome
        self.descricao = descricao

    def mostrar(self):
        print('\n----------DEPARTAMENTO----------')
        print(f'| Id: {self.departamento_id}\n | Nome: {self.nome}\n | Descrição: {self.descricao}\n')