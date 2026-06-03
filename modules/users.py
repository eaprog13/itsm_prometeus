from datetime import datetime


class User:
  
  contador = 0
  lista_users = []
  
  
  #método inicializador do objecto
  def __init__(self, nome, email, contacto, tipo, horario):
   
    User.contador += 1  
    self.user_id = User.contador
    self.nome = nome
    self.email = email
    self.contacto = contacto
    self.tipo = tipo
    self.horario = horario
    self.user_criado_em = datetime.now()
    
  
  # Métodos aplicados ao objecto directo
  def mostrar(self):
    print('\n----------USER----------')
    print(f'Id: {self.user_id}\n | Nome: {self.nome} |\n | Email: {self.email} |\n | Contacto: {self.contacto} |\n | Tipo: {self.tipo} |\n | Horário: {self.horario} |\n | Criado me: {self.user_criado_em:%d/%m/%Y %H:%M:%S}|\n')
  
  def editar(self, nome, email, contacto, tipo, horario):
    self.nome = nome
    self.email = email
    self.contacto = contacto
    self.tipo = tipo
    self.horario = horario
    print(f'O user {self.nome} foi actualizado!')
  
  def eliminar(self):
    User.lista_users.remove(self)
    print(f'O user {self.nome} foi eliminado da base de dados!')
        

  
  # Métodos aplicados à classe logo não precisam de objectos criados
  
  @classmethod
  def criar(cls, nome, email, contacto, tipo, horario):
    u = User(nome, email, contacto, tipo, horario)
    cls.lista_users.append(u)
    print(f'O user {nome} foi criado com sucesso!')
    
  
  @classmethod
  def listar(cls):
    if len(cls.lista_users) == 0:
      print('Não existem user registados!')
    else:
      for u in cls.lista_users:
        u.mostrar()  
