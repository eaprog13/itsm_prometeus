from datetime import datetime


class User:
  
  contador = 0
  users = []
  def __init__(self, nome, email, contacto, tipo, horario):
   
    User.contador += 1  
    self.user_id = User.contador
    self.nome = nome
    self.email = email
    self.contacto = contacto
    self.tipo = tipo
    self.horario = horario
    self.user_criado_em = datetime.now()

j = User("Joao", "Joao@exemplo.pt", "910000004", "User", "Manha")
i = User("Andre", "Andre@exemplo.pt", "910000002", "Admin", "Tarde")
k = User("Ana", "ana@exemplo.pt,", "910000001", "User", "Noite")


print(j.nome)
print(j.user_id)
print(j.email)
print(j.contacto)
print(j.horario)
print(j.tipo)
print(j.user_criado_em)

print(f"{k.email}")
print(f"{i.email}")
print(j.user_id, j.nome)
print(i.user_id, i.nome)
print(k.user_id, k.nome)

users = []
users.append(i)   # adiciona o objeto completo
users.append(j)
users.append(k)

for u in users:
  print(u.user_id, u.nome)
  
print(len(users))
  