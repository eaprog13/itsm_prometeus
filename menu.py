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
  return input('| Digita uma opção númerica!|')

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

#def menu_produtos()

#def menu_ticket()


while True:
  op = menu_principal()
  match op:
    case '1':
      while True: 
        op_user = menu_users()
        match op_user:
          
          
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
                  nome = input('| Qual é o novo nome? ')                  
                case '2':
                  email = input('| Qual é o novo email? ')                 
                case '3':
                  contacto = input('| Qual é o novo contacto? ')                  
                case '4':
                  tipo = input('| Qual é o novo tipo? ')                 
                case '5':
                  horario = input('| Qual é o novo horario? ')                 
                case '0':
                  menu_principal()
                  break            
                case _:
                  print('Digitaste uma opção incorrecta! Tenta Novamente!')
            u.editar(nome, email, contacto, tipo, horario)
          
          
          case '3':
            User.consultar_lista()
            
          
          case '4':
            User.consultar_lista()
            
            u_id = int(input('| Indica o ID do User que queres eliminar: '))
            
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
            menu_principal()
          
          case _:
            print('Digita uma opção válida!')
          
          
    case '2':
      print('| Iniciar a opção de criar o ticket!!')      
    case '3':
      print('| Iniciar o pedido de consulta')
    case '4':
      print('| Programa terminado! Caso queira fazer um novo pedido, execute novamente o programa...')
      break
    case _:
      print('Digita uma opção válida!')
  