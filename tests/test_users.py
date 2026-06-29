import pytest
from modules.users import User


def criar_user_valido(**overrides):
    """Função auxiliar — cria um User válido, permitindo sobrepor campos específicos."""
    dados = {
        'user_id': 1,
        'nome': 'Ana Silva',
        'email': 'ana.silva@itsm.pt',
        'contacto': '910000005',
        'tipo': 'admin',
        'departamento_id': 1,
        'turno': 'manha',
        'password': 'password123',
    }
    dados.update(overrides)
    return User(**dados)


# ── TESTES DE CASOS VÁLIDOS ──────────────────────────

def test_criar_user_com_dados_validos():
    u = criar_user_valido()
    assert u.nome == 'Ana Silva'
    assert u.email == 'ana.silva@itsm.pt'
    assert u.tipo == 'admin'


# ── TESTES DE EMAIL ──────────────────────────────────

def test_email_sem_arroba_levanta_erro():
    with pytest.raises(ValueError):
        criar_user_valido(email='emailinvalido')

def test_email_vazio_levanta_erro():
    with pytest.raises(ValueError):
        criar_user_valido(email='')


# ── TESTES DE CONTACTO ───────────────────────────────

def test_contacto_com_letras_levanta_erro():
    with pytest.raises(ValueError):
        criar_user_valido(contacto='91abc5678')

def test_contacto_vazio_levanta_erro():
    with pytest.raises(ValueError):
        criar_user_valido(contacto='')


# ── TESTES DE TIPO ───────────────────────────────────

def test_tipo_invalido_levanta_erro():
    with pytest.raises(ValueError):
        criar_user_valido(tipo='gestor')

@pytest.mark.parametrize('tipo_valido', ['admin', 'tecnico', 'user'])
def test_tipos_validos_sao_aceites(tipo_valido):
    u = criar_user_valido(tipo=tipo_valido)
    assert u.tipo == tipo_valido


# ── TESTES DE TURNO ──────────────────────────────────

def test_turno_invalido_levanta_erro():
    with pytest.raises(ValueError):
        criar_user_valido(turno='Madrugada')

@pytest.mark.parametrize('turno_valido', ['manha', 'tarde', 'noite'])
def test_turnos_validos_sao_aceites(turno_valido):
    u = criar_user_valido(turno=turno_valido)
    assert u.turno == turno_valido


# ── TESTES DE PASSWORD ───────────────────────────────

def test_password_curta_levanta_erro():
    with pytest.raises(ValueError):
        criar_user_valido(password='123')

def test_password_com_6_caracteres_e_aceite():
    u = criar_user_valido(password='123456')
    assert u.password == '123456'


# ── TESTES DE EDIÇÃO (setter chamado depois de criado) ──

def test_editar_email_para_invalido_levanta_erro():
    u = criar_user_valido()
    with pytest.raises(ValueError):
        u.email = 'semarroba'

def test_editar_email_para_valido_funciona():
    u = criar_user_valido()
    u.email = 'novo.email@itsm.pt'
    assert u.email == 'novo.email@itsm.pt'
    
    
    """ pytest tests/test_users.py -v """