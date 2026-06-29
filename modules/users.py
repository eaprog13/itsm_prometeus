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

    # ── ENCAPSULAMENTO ──────────────────────────────

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, valor):
        if not valor or '@' not in valor:
            raise ValueError('| Erro: email inválido — deve conter @')
        self.__email = valor

    @property
    def contacto(self):
        return self.__contacto

    @contacto.setter
    def contacto(self, valor):
        if not valor or not valor.strip().isdigit():
            raise ValueError('| Erro: contacto inválido — deve conter só dígitos')
        self.__contacto = valor

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, valor):
        tipos_validos = ['admin', 'tecnico', 'user']
        if valor not in tipos_validos:
            raise ValueError(f'| Erro: tipo inválido — deve ser um de {tipos_validos}')
        self.__tipo = valor

    @property
    def turno(self):
        return self.__turno

    @turno.setter
    def turno(self, valor):
        turnos_validos = ['manha', 'tarde', 'noite']
        if valor not in turnos_validos:
            raise ValueError(f'| Erro: turno inválido — deve ser um de {turnos_validos}')
        self.__turno = valor

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, valor):
        if not valor or len(valor) < 6:
            raise ValueError('| Erro: password inválida — mínimo 6 caracteres')
        self.__password = valor

    # ── MOSTRAR ─────────────────────────────────────

    def mostrar(self):
        print('\n----------USER----------')
        print(f'| Id: {self.user_id}\n | Nome: {self.nome}\n | Email: {self.email}\n | Contacto: {self.contacto}\n | Tipo: {self.tipo}\n | Departamento: {self.departamento_id}\n | Turno: {self.turno}\n | Criado em: {self.criado_em:%d/%m/%Y %H:%M:%S}\n')
        