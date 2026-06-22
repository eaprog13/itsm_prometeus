def input_inteiro(mensagem):
    """Pede um número ao utilizador até receber um valor válido."""
    while True:
        valor = input(mensagem)
        if valor.isdigit():
            return int(valor)
        print('| Erro: introduz um número válido!')


def confirmar(mensagem):
    """Pede confirmação sim/não ao utilizador."""
    resposta = input(mensagem)
    return resposta.strip().lower() == 'sim'


def executar(operacao):
    """
    Executa uma operação e apanha erros de validação (ValueError)
    ou erros inesperados, sem deixar o programa crashar.
    """
    try:
        return operacao()
    except ValueError as e:
        print(f'{e}')
    except Exception as e:
        print(f'| Erro inesperado: {e}')
    return None




