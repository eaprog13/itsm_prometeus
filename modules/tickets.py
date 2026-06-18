from datetime import datetime

class Ticket:
    def __init__(self, ticket_id, user_id, tecnico_id, produto_id, categoria_id, prioridade, descricao, estado='aberto', observacao=None, criado_em=None):
        self.ticket_id = ticket_id
        self.user_id = user_id
        self.tecnico_id = tecnico_id
        self.produto_id = produto_id
        self.categoria_id = categoria_id
        self.estado = estado
        self.prioridade = prioridade
        self.descricao = descricao
        self.observacao = observacao
        self.criado_em = criado_em or datetime.now()

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, valor):
        tipos_validos = ['aberto', 'fechado', 'devolvido']
        if valor not in tipos_validos:
            raise ValueError(f'| Estado inválido, escolha um de {tipos_validos}!')
        self.__estado = valor

    @property
    def prioridade(self):
        return self.__prioridade

    @prioridade.setter
    def prioridade(self, valor):
        tipos_validos = ['Alta', 'Média', 'Baixa']
        if valor not in tipos_validos:
            raise ValueError(f'| Prioridade inválida, escolha uma de {tipos_validos}!')
        self.__prioridade = valor

    def mostrar(self):
        print('\n----------TICKET----------')
        print(f'| Id: {self.ticket_id}\n | User: {self.user_id}\n | Técnico: {self.tecnico_id}\n | Produto: {self.produto_id}\n | Categoria: {self.categoria_id}\n | Estado: {self.estado}\n | Prioridade: {self.prioridade}\n | Descrição: {self.descricao}\n | Observação: {self.observacao}\n | Criado em: {self.criado_em:%d/%m/%Y %H:%M:%S}\n')