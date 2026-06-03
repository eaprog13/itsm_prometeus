from datetime import datetime
from users import user_id
from produtos import produto_id 


class Ticket:
  
  contador = 0
  lista_tickets = []
  
  def __init__(self, user_id, tecnico_id, produto_id, estado, prioridade, descricao):
    
    Ticket.contador += 1
    self.ticket_id = Ticket.contador
    self.user_id = user_id
    self.tecnico_id = tecnico_id
    self.produto_id = produto_id
    self.estado = estado
    self.prioridade = prioridade
    self.descricao = descricao
    self.ticket_criado_em = datetime.now()
    
  def mostrar(self):
    print('\n----------TICKET----------')
    print(f'Id: {self.ticket_id}\n | Criado por: {self.user_id} |\n | Atribuído a: {self.tecnico_id} |\n | Produto impactado: {self.produto_id} |\n \n | Estado: {self.estado} |\n | Prioridade: {self.prioridade} |\n | Descrição: {self.descricao} |\n | Criado me: {self.ticket_criado_em:%d/%m/%Y %H:%M:%S}|\n')
  
  def editar(self, user_id, tecnico_id, produto_id, estado, prioridade, descricao):
    self.user_id = user_id
    self.tecnico_id = tecnico_id
    self.produto_id = produto_id
    self.estado = estado
    self.prioridade = prioridade
    self.descricao = descricao
    print(f'O ticket {self.ticket_id} foi editado por {self.user_id} ou {self.tecnico_id}!')
    
  def eliminar(self):
    Ticket.lista_tickets.remove(self)
    print(f'O {self.ticket_id} foi eliminado por {self.user_id} ou {self.ticket_id}!')
    
    
  # MÉTODO DE CLASSE
  
  @classmethod
  def criar(cls, user_id, tecnico_id, produto_id, estado, prioridade, descricao ):
    t = Ticket(user_id, tecnico_id, produto_id, estado, prioridade, descricao)
    cls.lista_tickets.append(t)
    print(f'O ticket {cls.ticket_id} foi editado por {cls.user_id} ou {cls.tecnico_id}!')
  
  @classmethod
  def listar(cls):
    t = Ticket.criar()
  
    
  