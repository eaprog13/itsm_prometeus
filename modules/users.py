from datetime import datetime

class User:
    def __init__(self, user_id, nome, email, contacto, tipo, departamento_id, turno, password, criado_em=None):
        self.user_id = user_id
        self.nome = nome
        self.email = email
        self.contacto = contacto
        self.tipo = tipo
        self.departamento_id = departamento_id
        self.turno = turno
        self.password = password
        self.criado_em = criado_em or datetime.now()

    def mostrar(self):
        print('\n----------USER----------')
        print(f'| Id: {self.user_id}\n | Nome: {self.nome}\n | Email: {self.email}\n | Contacto: {self.contacto}\n | Tipo: {self.tipo}\n | Departamento: {self.departamento_id}\n | Turno: {self.turno}\n | Criado em: {self.criado_em:%d/%m/%Y %H:%M:%S}\n')