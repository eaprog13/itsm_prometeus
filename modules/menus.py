from repositorios import user_repo, produto_repo, ticket_repo, departamento_repo, categoria_repo
import os

def limpar_ecra():
    os.system('cls' if os.name == 'nt' else 'clear')

# ── MENUS DE NAVEGAÇÃO ──────────────────────────────────────────

def menu_principal_admin():
    limpar_ecra()
    print('\n|----------ITSM PROMETEUS - ADMIN----------|')
    print('| 1. Menu Users                            |')
    print('| 2. Menu Produtos                         |')
    print('| 3. Menu Tickets                          |')
    print('| 4. Menu Departamentos                    |')
    print('| 5. Menu Categorias                       |')
    print('| 0. Sair                                  |')
    print('|------------------------------------------|')
    return input('| Opção: ')

def menu_principal_tecnico():
    limpar_ecra()
    print('\n|----------ITSM PROMETEUS - TÉCNICO--------|')
    print('| 1. Menu Tickets                          |')
    print('| 0. Sair                                  |')
    print('|------------------------------------------|')
    return input('| Opção: ')

def menu_principal_user():
    limpar_ecra()
    print('\n|----------ITSM PROMETEUS - USER-----------|')
    print('| 1. Abrir Ticket                          |')
    print('| 2. Consultar os meus Tickets             |')
    print('| 0. Sair                                  |')
    print('|------------------------------------------|')
    return input('| Opção: ')

def menu_users():
    limpar_ecra()
    print('\n|----------MENU USERS----------|')
    print('| 1. Criar User                |')
    print('| 2. Editar User               |')
    print('| 3. Consultar Users           |')
    print('| 4. Eliminar User             |')
    print('| 0. Sair                      |')
    print('|------------------------------|')
    return input('| Opção: ')

def menu_users_editar():
    limpar_ecra()
    print('\n|----------EDITAR USER---------|')
    print('| 1. Nome                      |')
    print('| 2. Email                     |')
    print('| 3. Contacto                  |')
    print('| 4. Tipo                      |')
    print('| 5. Departamento              |')
    print('| 6. Turno                     |')
    print('| 7. Password                  |')
    print('| 0. Guardar e Sair            |')
    print('|------------------------------|')
    return input('| O que pretendes alterar? ')

def menu_produtos():
    limpar_ecra()
    print('\n|----------MENU PRODUTOS-------|')
    print('| 1. Criar Produto             |')
    print('| 2. Editar Produto            |')
    print('| 3. Consultar Produtos        |')
    print('| 4. Eliminar Produto          |')
    print('| 0. Sair                      |')
    print('|------------------------------|')
    return input('| Opção: ')

def menu_produtos_editar():
    limpar_ecra()
    print('\n|----------EDITAR PRODUTO------|')
    print('| 1. Nome                      |')
    print('| 2. Categoria                 |')
    print('| 3. Marca                     |')
    print('| 4. Número de série           |')
    print('| 0. Guardar e Sair            |')
    print('|------------------------------|')
    return input('| O que pretendes alterar? ')

def menu_tickets_admin():
    limpar_ecra()
    print('\n|----------MENU TICKETS--------|')
    print('| 1. Criar Ticket              |')
    print('| 2. Editar Ticket             |')
    print('| 3. Consultar Tickets         |')
    print('| 4. Fechar Ticket             |')
    print('| 5. Reabrir Ticket            |')
    print('| 6. Eliminar Ticket           |')
    print('| 0. Sair                      |')
    print('|------------------------------|')
    return input('| Opção: ')

def menu_tickets_tecnico():
    limpar_ecra()
    print('\n|----------MENU TICKETS--------|')
    print('| 1. Consultar Tickets         |')
    print('| 2. Editar Ticket             |')
    print('| 3. Fechar Ticket             |')
    print('| 4. Reabrir Ticket            |')
    print('| 5. Devolver Ticket           |')
    print('| 0. Sair                      |')
    print('|------------------------------|')
    return input('| Opção: ')

def menu_tickets_editar():
    limpar_ecra()
    print('\n|----------EDITAR TICKET-------|')
    print('| 1. Técnico                   |')
    print('| 2. Produto                   |')
    print('| 3. Categoria                 |')
    print('| 4. Prioridade                |')
    print('| 5. Descrição                 |')
    print('| 0. Guardar e Sair            |')
    print('|------------------------------|')
    return input('| O que pretendes alterar? ')

def menu_departamentos():
    limpar_ecra()
    print('\n|----------MENU DEPARTAMENTOS--|')
    print('| 1. Criar Departamento        |')
    print('| 2. Editar Departamento       |')
    print('| 3. Consultar Departamentos   |')
    print('| 4. Eliminar Departamento     |')
    print('| 0. Sair                      |')
    print('|------------------------------|')
    return input('| Opção: ')

def menu_categorias():
    limpar_ecra()
    print('\n|----------MENU CATEGORIAS-----|')
    print('| 1. Criar Categoria           |')
    print('| 2. Editar Categoria          |')
    print('| 3. Consultar Categorias      |')
    print('| 4. Eliminar Categoria        |')
    print('| 0. Sair                      |')
    print('|------------------------------|')
    return input('| Opção: ')




# ── LÓGICA DOS SUBMENUS ─────────────────────────────────────────

def submenu_users():
    while True:
        op = menu_users()
        match op:
            case '1':
                nome = input('| Nome: ')
                email = input('| Email: ')
                contacto = input('| Contacto: ')
                tipo = input('| Tipo (admin/tecnico/user): ')
                departamento_repo.listar_departamentos()
                departamento_id = int(input('| ID do departamento: '))
                turno = input('| Turno (Manha/Tarde/Noite): ')
                password = input('| Password: ')
                user_repo.criar_user(nome, email, contacto, tipo, departamento_id, turno, password)

            case '2':
                user_repo.listar_users()
                user_id = int(input('| ID do User a editar: '))
                u = user_repo.obter_user(user_id)
                if u:
                    while True:
                        op_editar = menu_users_editar()
                        match op_editar:
                            case '1':
                                u.nome = input('| Novo nome: ')
                            case '2':
                                u.email = input('| Novo email: ')
                            case '3':
                                u.contacto = input('| Novo contacto: ')
                            case '4':
                                u.tipo = input('| Novo tipo (admin/tecnico/user): ')
                            case '5':
                                departamento_repo.listar_departamentos()
                                u.departamento_id = int(input('| Novo ID do departamento: '))
                            case '6':
                                u.turno = input('| Novo turno (Manhã/Tarde/Noite): ')
                            case '7':
                                u.password = input('| Nova password: ')
                            case '0':
                                user_repo.editar_user(user_id, u.nome, u.email, u.contacto, u.tipo, u.departamento_id, u.turno, u.password)
                                break
                            case _:
                                print('| Opção incorrecta!')

            case '3':
                user_repo.listar_users()

            case '4':
                user_repo.listar_users()
                u_id = int(input('| ID do User a eliminar: '))
                op_eliminar = input(f'| Tens a certeza? (sim/nao): ')
                if op_eliminar.lower() == 'sim':
                    user_repo.eliminar_user(u_id)
                else:
                    print(f'| User {u_id} não foi eliminado!')

            case '0':
                break
            case _:
                print('| Opção inválida!')

def submenu_produtos():
    while True:
        op = menu_produtos()
        match op:
            case '1':
                nome = input('| Nome do produto: ')
                categoria = input('| Categoria: ')
                marca = input('| Marca: ')
                n_serie = input('| Número de série: ')
                produto_repo.criar_produto(nome, categoria, marca, n_serie)

            case '2':
                produto_repo.listar_produtos()
                produto_id = int(input('| ID do Produto a editar: '))
                p = produto_repo.obter_produto(produto_id)
                if p:
                    while True:
                        op_editar = menu_produtos_editar()
                        match op_editar:
                            case '1':
                                p.nome = input('| Novo nome: ')
                            case '2':
                                p.categoria = input('| Nova categoria: ')
                            case '3':
                                p.marca = input('| Nova marca: ')
                            case '4':
                                p.n_serie = input('| Novo número de série: ')
                            case '0':
                                produto_repo.editar_produto(produto_id, p.nome, p.categoria, p.marca, p.n_serie)
                                break
                            case _:
                                print('| Opção incorrecta!')

            case '3':
                produto_repo.listar_produtos()

            case '4':
                produto_repo.listar_produtos()
                p_id = int(input('| ID do produto a eliminar: '))
                op_eliminar = input(f'| Tens a certeza? (sim/nao): ')
                if op_eliminar.lower() == 'sim':
                    produto_repo.eliminar_produto(p_id)
                else:
                    print(f'| Produto {p_id} não foi eliminado!')

            case '0':
                break
            case _:
                print('| Opção inválida!')

def submenu_tickets_admin():
    while True:
        op = menu_tickets_admin()
        match op:
            case '1':
                user_repo.listar_users()
                user_id = int(input('| ID do user: '))
                tecnico_id = int(input('| ID do técnico: '))
                produto_repo.listar_produtos()
                produto_id = int(input('| ID do produto: '))
                categoria_repo.listar_categorias()
                categoria_id = int(input('| ID da categoria: '))
                prioridade = input('| Prioridade (Alta/Média/Baixa): ')
                descricao = input('| Descrição do problema: ')
                ticket_repo.abrir_ticket(user_id, tecnico_id, produto_id, categoria_id, prioridade, descricao)

            case '2':
                ticket_repo.listar_tickets()
                ticket_id = int(input('| ID do ticket a editar: '))
                t = ticket_repo.obter_ticket(ticket_id)
                if t:
                    while True:
                        op_editar = menu_tickets_editar()
                        match op_editar:
                            case '1':
                                t.tecnico_id = int(input('| Novo ID do técnico: '))
                            case '2':
                                t.produto_id = int(input('| Novo ID do produto: '))
                            case '3':
                                t.categoria_id = int(input('| Novo ID da categoria: '))
                            case '4':
                                t.prioridade = input('| Nova prioridade: ')
                            case '5':
                                t.descricao = input('| Nova descrição: ')
                            case '0':
                                ticket_repo.editar_ticket(ticket_id, t.tecnico_id, t.produto_id, t.categoria_id, t.prioridade, t.descricao)
                                break
                            case _:
                                print('| Opção incorrecta!')

            case '3':
                ticket_repo.listar_tickets()

            case '4':
                ticket_repo.listar_tickets()
                t_id = int(input('| ID do ticket a fechar: '))
                ticket_repo.fechar_ticket(t_id)

            case '5':
                ticket_repo.listar_tickets()
                t_id = int(input('| ID do ticket a reabrir: '))
                ticket_repo.reabrir_ticket(t_id)

            case '6':
                ticket_repo.listar_tickets()
                t_id = int(input('| ID do ticket a eliminar: '))
                op_eliminar = input(f'| Tens a certeza? (sim/nao): ')
                if op_eliminar.lower() == 'sim':
                    ticket_repo.eliminar_ticket(t_id)
                else:
                    print(f'| Ticket {t_id} não foi eliminado!')

            case '0':
                break
            case _:
                print('| Opção inválida!')

def submenu_tickets_tecnico(user_logado):
    while True:
        op = menu_tickets_tecnico()
        match op:
            case '1':
                ticket_repo.listar_tickets()

            case '2':
                ticket_repo.listar_tickets()
                ticket_id = int(input('| ID do ticket a editar: '))
                t = ticket_repo.obter_ticket(ticket_id)
                if t:
                    while True:
                        op_editar = menu_tickets_editar()
                        match op_editar:
                            case '1':
                                t.tecnico_id = int(input('| Novo ID do técnico: '))
                            case '2':
                                t.produto_id = int(input('| Novo ID do produto: '))
                            case '3':
                                t.categoria_id = int(input('| Novo ID da categoria: '))
                            case '4':
                                t.prioridade = input('| Nova prioridade: ')
                            case '5':
                                t.descricao = input('| Nova descrição: ')
                            case '0':
                                ticket_repo.editar_ticket(ticket_id, t.tecnico_id, t.produto_id, t.categoria_id, t.prioridade, t.descricao)
                                break
                            case _:
                                print('| Opção incorrecta!')

            case '3':
                ticket_repo.listar_tickets()
                t_id = int(input('| ID do ticket a fechar: '))
                ticket_repo.fechar_ticket(t_id)

            case '4':
                ticket_repo.listar_tickets()
                t_id = int(input('| ID do ticket a reabrir: '))
                ticket_repo.reabrir_ticket(t_id)

            case '5':
                ticket_repo.listar_tickets()
                t_id = int(input('| ID do ticket a devolver: '))
                observacao = input('| Observação para o user: ')
                ticket_repo.devolver_ticket(t_id, observacao)

            case '0':
                break
            case _:
                print('| Opção inválida!')

def submenu_tickets_user(user_logado):
    while True:
        op = menu_principal_user()
        match op:
            case '1':
                produto_repo.listar_produtos()
                produto_id = int(input('| ID do produto: '))
                categoria_repo.listar_categorias()
                categoria_id = int(input('| ID da categoria: '))
                prioridade = input('| Prioridade (Alta/Média/Baixa): ')
                descricao = input('| Descrição do problema: ')
                ticket_repo.abrir_ticket(user_logado.user_id, None, produto_id, categoria_id, prioridade, descricao)

            case '2':
                ticket_repo.listar_tickets_por_user(user_logado.user_id)

            case '0':
                print('Programa terminado, assim que possível o ticket será resolvido!')
                break
            case _:
                print('| Opção inválida!')

def submenu_departamentos():
    while True:
        op = menu_departamentos()
        match op:
            case '1':
                nome = input('| Nome do departamento: ')
                descricao = input('| Descrição: ')
                departamento_repo.criar_departamento(nome, descricao)

            case '2':
                departamento_repo.listar_departamentos()
                d_id = int(input('| ID do departamento a editar: '))
                d = departamento_repo.obter_departamento(d_id)
                if d:
                    d.nome = input('| Novo nome: ')
                    d.descricao = input('| Nova descrição: ')
                    departamento_repo.editar_departamento(d_id, d.nome, d.descricao)

            case '3':
                departamento_repo.listar_departamentos()

            case '4':
                departamento_repo.listar_departamentos()
                d_id = int(input('| ID do departamento a eliminar: '))
                op_eliminar = input(f'| Tens a certeza? (sim/nao): ')
                if op_eliminar.lower() == 'sim':
                    departamento_repo.eliminar_departamento(d_id)
                else:
                    print(f'| Departamento {d_id} não foi eliminado!')

            case '0':
                break
            case _:
                print('| Opção inválida!')

def submenu_categorias():
    while True:
        op = menu_categorias()
        match op:
            case '1':
                nome = input('| Nome da categoria: ')
                descricao = input('| Descrição: ')
                categoria_repo.criar_categoria(nome, descricao)

            case '2':
                categoria_repo.listar_categorias()
                c_id = int(input('| ID da categoria a editar: '))
                c = categoria_repo.obter_categoria(c_id)
                if c:
                    c.nome = input('| Novo nome: ')
                    c.descricao = input('| Nova descrição: ')
                    categoria_repo.editar_categoria(c_id, c.nome, c.descricao)

            case '3':
                categoria_repo.listar_categorias()

            case '4':
                categoria_repo.listar_categorias()
                c_id = int(input('| ID da categoria a eliminar: '))
                op_eliminar = input(f'| Tens a certeza? (sim/nao): ')
                if op_eliminar.lower() == 'sim':
                    categoria_repo.eliminar_categoria(c_id)
                else:
                    print(f'| Categoria {c_id} não foi eliminada!')

            case '0':
                break
            case _:
                print('| Opção inválida!')


# MENU DE ARRANQUE DO PROGRAMA

def arrancar(user_logado):
    print(f'\n| Bem-vindo/a, {user_logado.nome}! Perfil: {user_logado.tipo}')

    while True:
        if user_logado.tipo == 'admin':
            op = menu_principal_admin()
            match op:
                case '1':
                    submenu_users()
                case '2':
                    submenu_produtos()
                case '3':
                    submenu_tickets_admin()
                case '4':
                    submenu_departamentos()
                case '5':
                    submenu_categorias()
                case '0':
                    print('| Programa terminado!')
                    print('| Caso queiras alterar, inicia o programa novamente, até breve!')                    
                    break
                case _:
                    print('| Opção inválida!')

        elif user_logado.tipo == 'tecnico':
            op = menu_principal_tecnico()
            match op:
                case '1':
                    submenu_tickets_tecnico(user_logado)
                case '0':
                    print('| Programa terminado!')
                    print('| Caso queiras alterar, inicia o programa novamente, até breve!')
                    break
                case _:
                    print('| Opção inválida!')

        elif user_logado.tipo == 'user':
            submenu_tickets_user(user_logado)
            break