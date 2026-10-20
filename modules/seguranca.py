import hashlib
import hmac
import secrets

# PBKDF2-SHA256 da biblioteca padrão (sem dependências extra).
# 600 000 iterações é o mínimo recomendado pela OWASP para este algoritmo.
ALGORITMO = 'pbkdf2_sha256'
ITERACOES = 600_000


def gerar_hash(password):
    """
    Gera o hash de uma password para guardar na base de dados.

    Args:
        password (str): Password em texto simples.

    Returns:
        str: "pbkdf2_sha256$iteracoes$salt$hash" — o salt é aleatório,
        por isso a mesma password dá sempre um hash diferente.
    """
    salt = secrets.token_hex(16)
    digest = hashlib.pbkdf2_hmac('sha256', password.encode(), bytes.fromhex(salt), ITERACOES)
    return f'{ALGORITMO}${ITERACOES}${salt}${digest.hex()}'


def e_hash(valor):
    """Indica se o valor guardado já é um hash (e não uma password antiga em texto simples)."""
    return isinstance(valor, str) and valor.startswith(f'{ALGORITMO}$')


def verificar_password(password, guardado):
    """
    Compara a password introduzida com a que está guardada.

    Aceita também passwords antigas ainda em texto simples, para não
    bloquear contas criadas antes do hashing — o login actualiza-as.

    Args:
        password (str): Password introduzida pelo user.
        guardado (str): Valor guardado na base de dados.

    Returns:
        bool: True se a password estiver correcta.
    """
    if not e_hash(guardado):
        return hmac.compare_digest(password.encode(), str(guardado).encode())
    _, iteracoes, salt, esperado = guardado.split('$')
    digest = hashlib.pbkdf2_hmac('sha256', password.encode(), bytes.fromhex(salt), int(iteracoes))
    return hmac.compare_digest(digest.hex(), esperado)
