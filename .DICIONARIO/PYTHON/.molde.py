""" from datetime import datetime


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
    print(f'| O user {self.nome} foi eliminado da base de dados! |')
        

  
  # Métodos aplicados à classe logo não precisam de objectos criados
  
  @classmethod
  def criar(cls, nome, email, contacto, tipo, horario):
    u = User(nome, email, contacto, tipo, horario)
    cls.lista_users.append(u)
    print(f'| O user {nome} foi criado com sucesso!')
    
  
  @classmethod
  def consultar_lista(cls):
    if len(cls.lista_users) == 0:
      print('| Não existem user registados!')
    else:
      for u in cls.lista_users:
        u.mostrar()  




""" MENUS """
from modules.users import User
from modules.produtos import Produto
from modules.tickets import Ticket


def menu_principal():
  print('\n|----------ITSM PROMETEUS MENU----------|')
  print('| 1. Menu Users |')
  print('| 2. Menu Produtos |')
  print('| 3. Menu Tickets |')
  print('| 0. Sair |')
  print('|----------DIGITA A OPCAO----------|')
  return input('| Digita uma opção de 1 a 4!|')

def menu_users():
  print('\n|----------MENU USERS----------|')
  print('| 1. Criar User |')
  print('| 2. Editar User |')
  print('| 3. Consultar User |')
  print('| 4. Eliminar User |')
  print('| 0. Sair |')
  print('|----------DIGITA A OPCAO----------|')
  return input('| Digita uma opção númerica! ')

def menu_users_editar():
  print('\n|----------MENU EDITAR USER----------|')
  print('| 1. nome |')
  print('| 2. email |')
  print('| 3. contacto |')
  print('| 4. tipo |')
  print('| 5. horario |')
  print('| 0. Sair |')
  print('|----------DIGITA A OPCAO----------|')
  return input('| O que pretendes alterar?')

def menu_produtos():
  print('\n|----------MENU PRODUTOS----------|')
  print('| 1. Criar Produto |')
  print('| 2. Editar Produto |')
  print('| 3. Consultar Produto |')
  print('| 4. Eliminar Produto |')
  print('| 0. Sair |')
  print('|----------DIGITA A OPCAO----------|')
  return input('| Digita uma opção númerica! ')

def menu_produtos_editar():
  print('\n|----------MENU EDITAR PRODUTO----------|')
  print('| 1. nome |')
  print('| 2. categoria |')
  print('| 3. número de série|')
  print('| 0. Sair |')
  print('|----------DIGITA A OPCAO----------|')
  return input('| O que pretendes alterar?')

def menu_tickets():
  print('\n|----------MENU TICKETS----------|')
  print('| 1. Criar Ticket |')
  print('| 2. Editar Ticket |')
  print('| 3. Consultar Ticket |')
  print('| 4. Fechar Ticket |')
  print('| 5. Reabrir Ticket |')
  print('| 6. Eliminar Ticket |')
  print('| 0. Sair |')
  print('|----------DIGITA A OPCAO----------|')
  return input('| Digita uma opção númerica! ')

def menu_tickets_editar():
  print('\n|----------MENU EDITAR Ticket----------|')
  print('| 1. user_id |')
  print('| 2. Tecnico_id |')
  print('| 3. Produto_id |')
  print('| 4. Prioridade |')
  print('| 5. Descrição |')
  print('| 0. Sair |')
  print('|----------DIGITA A OPCAO----------|')
  return input('| O que pretendes alterar?')


#MENU PRINCIPAL
def arrancar():
  carregar_dados()

  while True:
    op = menu_principal()
    match op:
      # MENU USER
      case '1':
        while True: 
          op_user = menu_users()
          
          match op_user:
          #SUBMENU USER
            case '1':
              nome = input('| Digita o teu nome: ')
              email = input('| Digita o teu email: ')
              contacto = input('| Digita o teu contacto: ')
              tipo = input('| Digita o tipo user: ')
              horario = input('| Digita o teu horário: ')
              User.criar(nome, email, contacto, tipo, horario)
                      
            case '2':
              User.consultar_lista()
              user_id = int(input('| Qual é o ID do User?'))
              u = User.lista_users[user_id - 1]
              
              while True:
                op_editar = menu_users_editar()
                
                match op_editar:
                  case '1':
                    u.nome = input('| Qual é o novo nome? ')                  
                  case '2':
                    u.email = input('| Qual é o novo email? ') 
                    print(f'| O email do {u.nome} com o id {user_id} foi alterado com sucesso!')                
                  case '3':
                    u.contacto = input('| Qual é o novo contacto? ')                  
                  case '4':
                    u.tipo = input('| Qual é o novo tipo? ')                 
                  case '5':
                    u.horario = input('| Qual é o novo horario? ')                 
                  case '0':
                    break            
                  case _:
                    print('Digitaste uma opção incorrecta! Tenta Novamente!')
                      
            case '3':
              User.consultar_lista()                     
            case '4':
              User.consultar_lista()            
              u_id = int(input('| Indica o ID do User que queres eliminar: '))
              
              #CORRER A LISTA COM O USER_ID
              for user in User.lista_users:
                if user.user_id == u_id:
                  
                  op_eliminar = input(f'| Tens a certeza que queres eliminar o user:{user.user_id} nome:{user.nome}? (sim ou nao)-> ')
                  
                  if op_eliminar.lower() == 'sim':
                    user.eliminar()
                  else:
                    print(f'| O {user.nome} não foi eliminado!')
                  break                  
              else:
                print(f'| Opção não existente! Digita uma opção correcta! |')                            
            case '0':
              break
            case _:
              print('| Digita uma opção válida!')
          
      # MENU PRODUTOS   
      case '2':
        while True: 
          op_produto = menu_produtos()
          
          match op_produto:
          #SUBMENU PRODUTO
            case '1':
              nome = input('| Digita o teu nome: ')
              categoria = input('| Digita a categoria do produto: ')
              n_serie = input('| Digita o número de série: ')
              Produto.criar(nome, categoria, n_serie)
                      
            case '2':
              Produto.consultar_lista()
              produto_id = int(input('| Qual é o ID do Produto?'))
              p = Produto.lista_produtos[produto_id - 1]
              
              while True:
                op_editar = menu_produtos_editar()
                
                match op_editar:
                  case '1':
                    p.nome = input('| Qual é o novo nome? ')                  
                  case '2':
                    p.categoria = input('| Qual é a nova categoria do produto? ')                 
                  case '3':
                    p.n_serie = input('| Qual é o número de série correcto? ')                  
                  case '0':
                    break            
                  case _:
                    print('Digitaste uma opção incorrecta! Tenta Novamente!')
                      
            case '3':
              Produto.consultar_lista()     
                        
            case '4':
              Produto.consultar_lista()            
              p_id = int(input('| Indica o ID do User que queres eliminar: '))
              
              #CORRER A LISTA COM O PRODUTO_ID
              for produto in Produto.lista_produtos:
                if produto.produto_id == p_id:
                  
                  op_eliminar = input(f'| Tens a certeza que queres eliminar o user:{produto.produto_id} nome:{produto.nome}? (sim ou nao)-> ')
                  
                  if op_eliminar.lower() == 'sim':
                    produto.eliminar()
                  else:
                    print(f'| O {produto.nome} não foi eliminado!')
                  break                  
              else:
                print(f'| Opção não existente! Digita uma opção correcta! |')                            
            case '0':
              break
            case _:
              print('Digita uma opção válida!')
                  

      # MENU TICKETS
      case '3':
        while True: 
          op_ticket = menu_tickets()
          
          match op_ticket:
          #SUBMENU TICKET
            case '1':
              user_id = input('| Digita o user_id: ')
              tecnico_id = input('| Digita o ID do técnico : ')
              produto_id = input('| Digita o ID do produto: ')
              prioridade = input('| Indica a prioridade: ')
              descricao = input('| Descreve o problema de forma concisa e clara: ')
              
              Ticket.abrir(user_id, tecnico_id, produto_id, prioridade, descricao)
                      
            case '2':
              Ticket.consultar_lista()
              ticket_id = int(input('| Qual é o ID do ticket?'))
              t = Ticket.lista_tickets[ticket_id - 1]
              
              while True:
                op_editar = menu_tickets_editar()
                
                match op_editar:
                  case '1':
                    t.user_id = input('| Qual é o ID do user correcto? ')                  
                  case '2':
                    t.tecnico_id = input('| Qual é o ID do técnico correcto? ')                 
                  case '3':
                    t.produto_id= input('| Qual é o ID do produto correcto? ')                  
                  case '4':
                    t.prioridade= input('| Actualiza a prioridade: ')                  
                  case '5':
                    t.descricao= input('| Actualiza a descrição: ')                  
                  case '0':
                    break            
                  case _:
                    print('Digitaste uma opção incorrecta! Tenta Novamente!')
                      
            case '3':
              Ticket.consultar_lista()     
            
            case '4': 
              Ticket.consultar_lista()
              t_id = int(input('| Indica o ID do ticket a fechar:'))
              for ticket in Ticket.lista_tickets:
                if ticket.ticket_id == t_id:
                  ticket.fechar()
                  break
              else:
                print('Opção Inválida, o ticket ainda está aberto!')
                  
            case '5':
              Ticket.consultar_lista()
              t_id = int(input('| Indica o ID do ticket a fechar:'))
              for ticket in Ticket.lista_tickets:
                if ticket.ticket_id == t_id:
                  ticket.reabrir()
                  break
              else:
                print('Opção Inválida, o ticket ainda está fechado!')
                        
            case '6':
              Ticket.consultar_lista()            
              t_id = int(input('| Indica o ID do User que queres eliminar: '))
              
              #CORRER A LISTA COM O TICKET_ID
              for ticket in Ticket.lista_tickets:
                if ticket.ticket_id == t_id:
                  # duplicado com o método eliminar, não sei se faço a condição no menu ou se uso o método self para isso...
                  op_eliminar = input(f'| Tens a certeza que queres eliminar o user:{ticket.ticket_id}? (sim ou nao)-> ')
                  
                  if op_eliminar.lower() == 'sim':
                    ticket.eliminar()
                  else:
                    print(f'| O {ticket.ticket_id} não foi eliminado!')
                  break                  
              else:
                print(f'| Opção não existente! Digita uma opção correcta! |')                            
            case '0':
              break
            case _:
              print('Digitaste uma opção incorrecta! Tenta Novamente!')
      # SAIR
      case '0':
        guardar_dados()
        print('| Programa terminado! Caso queira fazer um novo pedido, execute novamente o programa...')
        break
      case _:
        print('Digita uma opção válida!')
    
    
    """ TICKETS """
    
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
        
        
        
        """ PRODUTOS """
        
        
        from datetime import datetime

class Produto:
  
  contador = 0
  lista_produtos = []
  
  def __init__ (self, nome, categoria, n_serie):
  
    Produto.contador += 1
    self.produto_id = Produto.contador
    self.nome = nome
    self.categoria = categoria
    self.n_serie = n_serie
    self.produto_criado_em = datetime.now()
  
  def mostrar_produto(self):
    print('\n----------PRODUTO----------')
    print(f'Id: {self.produto_id}\n | Nome: {self.nome} |\n | Categoria: {self.categoria} |\n | NºSérie: {self.n_serie} |\n | Criado me: {self.produto_criado_em:%d/%m/%Y %H:%M:%S}|\n')
    
  def editar(self, nome, categoria, n_serie):
    self.nome = nome
    self.categoria = categoria
    self.n_serie = n_serie
    print(f'| O produto {self.nome} foi actualizado!')
  
  def eliminar(self):
    Produto.lista_produtos.remove(self)
    print(f'| O produto {self.nome} foi eliminado!')
    
  #ENCAPSULAR
  
  @property
  def nome(self):
    return self.__nome

  @nome.setter
  def nome(self,valor):
    if not valor or valor.strip() == '':
      print('| Erro: o nome não pode estar vazio!')
    else:
      self.__nome = valor
  
  
  # métodos de classe
  @classmethod
  
  def criar(cls, nome, categoria, n_serie):
    p = cls(nome, categoria, n_serie)
    cls.lista_produtos.append(p)
    print(f'| O produto {nome} foi criado!')
    
  @classmethod    
  def consultar_lista(cls):
    if len(cls.lista_produtos) == 0:
      print(f'| Ainda não há produtos registados!')
    else:
      for p in cls.lista_produtos:
        p.mostrar_produto()   
    
    
    """ GUARDAR em json """
    
    import json
import os
from modules.users import User
from modules.produtos import Produto
from modules.tickets import Ticket

FICHEIRO = 'itsm_data.json'

def guardar_dados():
  dados = {
    'users': [
            {
                'user_id': u.user_id,
                'nome': u.nome,
                'email': u.email,
                'contacto': u.contacto,
                'tipo': u.tipo,
                'horario': u.horario
            }
            for u in User.lista_users
            
    ],
    'produtos': [
      {
        'produto_id': p.produto_id,
        'nome': p.nome,
        'categoria': p.categoria,
        'n_serie': p.n_serie
              
      }
      for p in Produto.lista_produtos
    ],
    
    'tickets': [
          {
                'ticket_id': t.ticket_id,
                'user_id': t.user_id,
                'tecnico_id': t.tecnico_id,
                'produto_id': t.produto_id,
                'estado': t.estado,
                'prioridade': t.prioridade,
                'descricao': t.descricao
            }
            for t in Ticket.lista_tickets
        ]    
  }
  
  with open(FICHEIRO, 'w', encoding='utf-8') as f:
    json.dump(dados, f, indent=2, ensure_ascii=False)
  print('| Dados guardados com sucesso!')
  
  
def carregar_dados():
    if not os.path.exists(FICHEIRO):
        return  # primeira vez, ficheiro ainda não existe

    with open(FICHEIRO, 'r', encoding='utf-8') as f:
        dados = json.load(f)

    # Carregar users
    for d in dados.get('users', []):
        u = User(d['nome'], d['email'], d['contacto'], d['tipo'], d['horario'])
        u.user_id = d['user_id']
        User.lista_users.append(u)
    if User.lista_users:
        User.contador = max(u.user_id for u in User.lista_users)

    # Carregar produtos
    for d in dados.get('produtos', []):
        p = Produto(d['nome'], d['categoria'], d['n_serie'])
        p.produto_id = d['produto_id']
        Produto.lista_produtos.append(p)
    if Produto.lista_produtos:
        Produto.contador = max(p.produto_id for p in Produto.lista_produtos)

    # Carregar tickets
    for d in dados.get('tickets', []):
        t = Ticket(d['user_id'], d['tecnico_id'], d['produto_id'], d['prioridade'], d['descricao'], d['estado'])
        t.ticket_id = d['ticket_id']
        Ticket.lista_tickets.append(t)
    if Ticket.lista_tickets:
        Ticket.contador = max(t.ticket_id for t in Ticket.lista_tickets)

    print('| Dados carregados com sucesso!')  
    
    """ DB PARA POSTGRES """
    
    import psycopg

def get_connection():
    return psycopg.connect(
        host="localhost",
        dbname="itsm_prometeus",
        user="postgres",
        password="postgres"
    )
    
    """ MAIN """
    
    from modules.menus import arrancar

arrancar()

""" LIGAR DB """
from modules.db import get_connection

conn = get_connection()
print("Conexão OK")
conn.close() """