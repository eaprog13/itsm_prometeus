from repositorios import user_repo


def login():
    print('\n|----------ITSM PROMETEUS----------|')
    print('|             LOGIN                |')
    print('|----------------------------------|')
    
    tentativas = 3
    
    while tentativas > 0:
        email = input('| Email: ')
        password = input('| Password: ')
        
        u = user_repo.obter_user_por_email(email)
        
        if u and u.password == password:
            print(f'| Bem-vindo/a, {u.nome}!')
            return u
        else:
            tentativas -= 1
            if tentativas >= 2:
                print(f'| Inseriste mal o email ou password! Tens apenas {tentativas} tentativas!')
            elif tentativas >= 1:
                print(f'| Inseriste mal o email ou password! Tens apenas {tentativas} tentativa!')
            else:
                print('| Número máximo de tentativas atingido! Conta Bloqueada!')
                print('| Contacta o suporte!')
                print('| Programa terminado...')
                return None