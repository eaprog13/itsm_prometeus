import pytest
from modules.tickets import Ticket


def criar_ticket_valido(**overrides):
    """Função auxiliar — cria um Ticket válido, permitindo sobrepor campos específicos."""
    dados = {
        'ticket_id': 1,
        'user_id': 4,
        'tecnico_id': 2,
        'produto_id': 1,
        'categoria_id': 1,
        'prioridade': 'Alta',
        'descricao': 'Laptop não arranca',
        'estado': 'aberto',
        'observacao': None,
    }
    dados.update(overrides)
    return Ticket(**dados)


# ── TESTES DE CASOS VÁLIDOS ──────────────────────────

def test_criar_ticket_com_dados_validos():
    t = criar_ticket_valido()
    assert t.descricao == 'Laptop não arranca'
    assert t.estado == 'aberto'
    assert t.prioridade == 'Alta'


# ── TESTES DE ESTADO ─────────────────────────────────

def test_estado_invalido_levanta_erro():
    with pytest.raises(ValueError):
        criar_ticket_valido(estado='cancelado')

@pytest.mark.parametrize('estado_valido', ['aberto', 'fechado', 'devolvido'])
def test_estados_validos_sao_aceites(estado_valido):
    t = criar_ticket_valido(estado=estado_valido)
    assert t.estado == estado_valido


# ── TESTES DE PRIORIDADE ─────────────────────────────

def test_prioridade_invalida_levanta_erro():
    with pytest.raises(ValueError):
        criar_ticket_valido(prioridade='Urgente')

def test_prioridade_minuscula_levanta_erro():
    # confirma que o setter é sensível a maiúsculas/minúsculas
    with pytest.raises(ValueError):
        criar_ticket_valido(prioridade='alta')

@pytest.mark.parametrize('prioridade_valida', ['Alta', 'Média', 'Baixa'])
def test_prioridades_validas_sao_aceites(prioridade_valida):
    t = criar_ticket_valido(prioridade=prioridade_valida)
    assert t.prioridade == prioridade_valida


# ── TESTES DE EDIÇÃO (setter chamado depois de criado) ──

def test_editar_estado_para_invalido_levanta_erro():
    t = criar_ticket_valido()
    with pytest.raises(ValueError):
        t.estado = 'pendente'

def test_editar_estado_para_fechado_funciona():
    t = criar_ticket_valido()
    t.estado = 'fechado'
    assert t.estado == 'fechado'

def test_editar_prioridade_para_invalida_levanta_erro():
    t = criar_ticket_valido()
    with pytest.raises(ValueError):
        t.prioridade = 'Crítica'

def test_fluxo_devolver_ticket():
    """Testa o fluxo: ticket aberto → devolvido, com observação."""
    t = criar_ticket_valido(estado='aberto')
    t.estado = 'devolvido'
    t.observacao = 'Falta confirmar com o user'
    assert t.estado == 'devolvido'
    assert t.observacao == 'Falta confirmar com o user'
    
    
""" pytest tests/test_tickets.py -v """