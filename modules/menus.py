from repositorios import user_repo, produto_repo, ticket_repo

#PRINT OPCOES MENUS COM RETURN PARA A LÓGICA
def menu_principal():
  print('\n|----------ITSM PROMETEUS MENU----------|')
  print('| 1. Menu Users |')
  print('| 2. Menu Produtos |')
  print('| 3. Menu Tickets |')
  print('| 0. Sair |')
  print('|----------DIGITA A OPCAO----------|')
  return input('| Digita uma opção de 1 a 4: ')

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
  print('| 5. turno |')
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
  print('| 1. Tecnico_id |')
  print('| 2. Produto_id |')
  print('| 3. Categoria_id |')
  print('| 4. Prioridade |')
  print('| 5. Descrição |')
  print('| 0. Sair |')
  print('|----------DIGITA A OPCAO----------|')
  return input('| O que pretendes alterar?')


def arrancar():

  while True:
    op = menu_principal()
    match op:

      # MENU USER
      case '1':
        while True:
          op_user = menu_users()
          match op_user:

            case '1':
              nome = input('| Digita o teu nome: ')
              email = input('| Digita o teu email: ')
              contacto = input('| Digita o teu contacto: ')
              tipo = input('| Digita o tipo user: ')
              turno = input('| Digita o teu turno: ')
              user_repo.criar_user(nome, email, contacto, tipo, turno)

            case '2':
              user_repo.listar_users()
              user_id = int(input('| Qual é o ID do User? '))
              u = user_repo.obter_user(user_id)

              if u:
                while True:
                  op_editar = menu_users_editar()
                  match op_editar:
                    case '1':
                      u.nome = input('| Qual é o novo nome? ')
                    case '2':
                      u.email = input('| Qual é o novo email? ')
                    case '3':
                      u.contacto = input('| Qual é o novo contacto? ')
                    case '4':
                      u.tipo = input('| Qual é o novo tipo? ')
                    case '5':
                      u.turno = input('| Qual é o novo turno? ')
                    case '0':
                      user_repo.editar_user(user_id, u.nome, u.email, u.contacto, u.tipo, u.turno)
                      break
                    case _:
                      print('| Digitaste uma opção incorrecta! Tenta Novamente!')

            case '3':
              user_repo.listar_users()

            case '4':
              user_repo.listar_users()
              u_id = int(input('| Indica o ID do User que queres eliminar: '))
              op_eliminar = input(f'| Tens a certeza que queres eliminar o user {u_id}? (sim ou nao)-> ')
              if op_eliminar.lower() == 'sim':
                user_repo.eliminar_user(u_id)
              else:
                print(f'| O user {u_id} não foi eliminado!')

            case '0':
              break
            case _:
              print('| Digita uma opção válida!')

      # MENU PRODUTOS
      case '2':
        while True:
          op_produto = menu_produtos()
          match op_produto:

            case '1':
              nome = input('| Digita o nome do produto: ')
              categoria = input('| Digita a categoria do produto: ')
              n_serie = input('| Digita o número de série: ')
              produto_repo.criar_produto(nome, categoria, n_serie)

            case '2':
              produto_repo.listar_produtos()
              produto_id = int(input('| Qual é o ID do Produto? '))
              p = produto_repo.obter_produto(produto_id)

              if p:
                while True:
                  op_editar = menu_produtos_editar()
                  match op_editar:
                    case '1':
                      p.nome = input('| Qual é o novo nome? ')
                    case '2':
                      p.categoria = input('| Qual é a nova categoria? ')
                    case '3':
                      p.n_serie = input('| Qual é o número de série correcto? ')
                    case '0':
                      produto_repo.editar_produto(produto_id, p.nome, p.categoria, p.n_serie)
                      break
                    case _:
                      print('| Digitaste uma opção incorrecta! Tenta Novamente!')

            case '3':
              produto_repo.listar_produtos()

            case '4':
              produto_repo.listar_produtos()
              p_id = int(input('| Indica o ID do produto que queres eliminar: '))
              op_eliminar = input(f'| Tens a certeza que queres eliminar o produto {p_id}? (sim ou nao)-> ')
              if op_eliminar.lower() == 'sim':
                produto_repo.eliminar_produto(p_id)
              else:
                print(f'| O produto {p_id} não foi eliminado!')

            case '0':
              break
            case _:
              print('| Digita uma opção válida!')

      # MENU TICKETS
      case '3':
        while True:
          op_ticket = menu_tickets()
          match op_ticket:

            case '1':
              user_id = int(input('| Digita o user_id: '))
              tecnico_id = int(input('| Digita o ID do técnico: '))
              produto_id = int(input('| Digita o ID do produto: '))
              categoria_id = int(input('| Digita o ID da categoria: '))
              prioridade = input('| Indica a prioridade (Alta/Média/Baixa): ')
              descricao = input('| Descreve o problema: ')
              ticket_repo.abrir_ticket(user_id, tecnico_id, produto_id, categoria_id, prioridade, descricao)

            case '2':
              ticket_repo.listar_tickets()
              ticket_id = int(input('| Qual é o ID do ticket? '))
              t = ticket_repo.obter_ticket(ticket_id)

              if t:
                while True:
                  op_editar = menu_tickets_editar()
                  match op_editar:
                    case '1':
                      t.tecnico_id = int(input('| Qual é o ID do técnico correcto? '))
                    case '2':
                      t.produto_id = int(input('| Qual é o ID do produto correcto? '))
                    case '3':
                      t.categoria_id = int(input('| Qual é o ID da categoria correcta? '))
                    case '4':
                      t.prioridade = input('| Actualiza a prioridade: ')
                    case '5':
                      t.descricao = input('| Actualiza a descrição: ')
                    case '0':
                      ticket_repo.editar_ticket(ticket_id, t.tecnico_id, t.produto_id, t.categoria_id, t.prioridade, t.descricao)
                      break
                    case _:
                      print('| Digitaste uma opção incorrecta! Tenta Novamente!')

            case '3':
              ticket_repo.listar_tickets()

            case '4':
              ticket_repo.listar_tickets()
              t_id = int(input('| Indica o ID do ticket a fechar: '))
              ticket_repo.fechar_ticket(t_id)

            case '5':
              ticket_repo.listar_tickets()
              t_id = int(input('| Indica o ID do ticket a reabrir: '))
              ticket_repo.reabrir_ticket(t_id)

            case '6':
              ticket_repo.listar_tickets()
              t_id = int(input('| Indica o ID do ticket a eliminar: '))
              op_eliminar = input(f'| Tens a certeza que queres eliminar o ticket {t_id}? (sim ou nao)-> ')
              if op_eliminar.lower() == 'sim':
                ticket_repo.eliminar_ticket(t_id)
              else:
                print(f'| O ticket {t_id} não foi eliminado!')

            case '0':
              break
            case _:
              print('| Digitaste uma opção incorrecta! Tenta Novamente!')

      # SAIR
      case '0':
        guardar_dados()
        print('| Programa terminado! Caso queira fazer um novo pedido, execute novamente o programa...')
        break
      case _:
        print('| Digita uma opção válida!')