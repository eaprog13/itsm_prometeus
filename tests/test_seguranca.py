from modules.seguranca import e_hash, gerar_hash, verificar_password


def test_hash_nao_contem_a_password():
    h = gerar_hash('admin123')
    assert e_hash(h)
    assert 'admin123' not in h


def test_mesma_password_da_hashes_diferentes():
    assert gerar_hash('admin123') != gerar_hash('admin123')


def test_password_correcta_e_aceite():
    assert verificar_password('admin123', gerar_hash('admin123'))


def test_password_errada_e_rejeitada():
    assert not verificar_password('admin124', gerar_hash('admin123'))


def test_password_antiga_em_texto_simples_ainda_funciona():
    assert not e_hash('admin123')
    assert verificar_password('admin123', 'admin123')
    assert not verificar_password('outra', 'admin123')
