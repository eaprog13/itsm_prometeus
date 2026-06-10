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
            if tentativas > 0:
                print(f'| Inseriste mal o email ou password! Tens apenas {tentativas} tentativa!')
            else:
                print('| Número máximo de tentativas atingido. A sair...')
                return None