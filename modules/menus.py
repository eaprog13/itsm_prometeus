from modules.guardar_db import guardar_dados, carregar_dados
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
              guardar_dados()
              print('| Programa encerrado!')
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
        print('| Programa terminado! Caso queira fazer um novo pedido, execute novamente o programa...')
        break
      case _:
        print('Digita uma opção válida!')
    