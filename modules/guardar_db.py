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