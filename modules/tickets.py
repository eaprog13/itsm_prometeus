from datetime import datetime
""" from users import user_id
from produtos import produto_id  """


class Ticket:
  
  contador = 0
  lista_tickets = []
  
  def __init__(self, user_id, tecnico_id, produto_id, prioridade, descricao, estado= "aberto"):
    
    Ticket.contador += 1
    self.ticket_id = Ticket.contador
    self.user_id = user_id
    self.tecnico_id = tecnico_id
    self.produto_id = produto_id
    self.estado = estado
    self.prioridade = prioridade
    self.descricao = descricao
    self.ticket_criado_em = datetime.now()
    
  def mostrar_obj(self):
    print('\n|----------TICKET----------')
    print(f'| Id: {self.ticket_id}\n | Criado por: {self.user_id} |\n | Atribuído a: {self.tecnico_id} |\n | Produto impactado: {self.produto_id} |\n | Estado: {self.estado} |\n | Prioridade: {self.prioridade} |\n | Descrição: {self.descricao} |\n | Criado me: {self.ticket_criado_em:%d/%m/%Y %H:%M:%S} |\n')
  
  def editar(self, prioridade, descricao):
    self.prioridade = prioridade
    self.descricao = descricao
    print(f'| O ticket {self.ticket_id} foi editado por {self.user_id} ou {self.tecnico_id}!')
    
  def eliminar(self):
    e = input(f'| Tem a certeza que quer eliminar o {self.ticket_id}? (Digite sim ou nao)')
    if e == "sim":
      Ticket.lista_tickets.remove(self)
      print(f'| O {self.ticket_id} foi eliminado por {self.user_id} ou {self.tecnico_id}!')
    else:
      print(f'| Não foi possível alterar o {self.ticket_id}! Escolha novamente a opção caso queira alterar!')
    
  def fechar(self):
    self.estado = 'Fechado'
    print(f'| O ticket {self.ticket_id} foi fechado com sucesso!')
      
  def reabrir(self):
    self.estado = 'aberto'
    print(f'| O ticket {self.ticket_id} foi reaberto por {self.user_id} com sucesso!')
  
  # MÉTODO DE CLASSE
  
  @classmethod
  def abrir(cls, user_id, tecnico_id, produto_id, prioridade, descricao ):

    t = cls(user_id, tecnico_id, produto_id, prioridade, descricao)
    cls.lista_tickets.append(t)
    print(f'| O ticket {t.ticket_id} foi aberto por {t.user_id}!')


  @classmethod
  def consultar_lista(cls):
    if len(cls.lista_tickets) == 0:
      print(f'| Não existem tickets na lista!')
    else:
      for t in cls.lista_tickets:
        t.mostrar_obj()
        