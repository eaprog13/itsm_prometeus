from datetime import datetime

class Ticket:
    def __init__(self, ticket_id, user_id, tecnico_id, produto_id, categoria_id, prioridade, descricao, estado='aberto', observacao=None, criado_em=None):
        self.ticket_id = ticket_id
        self.user_id = user_id
        self.tecnico_id = tecnico_id
        self.produto_id = produto_id
        self.categoria_id = categoria_id
        self.__estado = estado
        self.__prioridade = prioridade
        self.descricao = descricao
        self.observacao = observacao
        self.criado_em = criado_em or datetime.now()

    @property
    def estado(self):
        return self.__estado
    
    @estado.setter
    def estado(self, valor):
        tipo_estado = ['aberto', 'fechado']
        if not valor in tipo_estado:
            raise ValueError(f'| Estado inválido, escolha 1 dos {tipo_estado} disponíveis!')
        return self.__estado
    
    
    @property
    def prioridade(self):
        return self.__prioridade
    
    @prioridade.setter
    def prioridade(self, valor):
        tipo_prioridade = ['alta', 'média', 'baixa']
        if valor not in tipo_prioridade:
            raise ValueError(f'| Prioridade inválida, escolhe uma das {tipo_prioridade} disponíveis!')
        return self.__prioridade
    
    
    def mostrar(self):
        print('\n----------TICKET----------')
        print(f'Id: {self.ticket_id}\n | User: {self.user_id}\n | Técnico: {self.tecnico_id}\n | Produto: {self.produto_id}\n | Categoria: {self.categoria_id}\n | Estado: {self.estado}\n | Prioridade: {self.prioridade}\n | Descrição: {self.descricao}\n | Observação: {self.observacao}\n | Criado em: {self.criado_em:%d/%m/%Y %H:%M:%S}\n')