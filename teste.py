class Carro:
  
  def __init__(self, marca, cor, modelo):
    self.marca = marca
    self.cor = cor
    self.modelo = modelo
  
  def start(self):  
    return (f"O {self.marca} {self.modelo} vai ligar!")
  
  def stop(self):  
    return (f"O {self.marca} {self.modelo} vai desligar!")
  
meu_carro = Carro("Toyota", "Cor" , "Corola")
print(meu_carro.marca)
print(meu_carro.cor)
print(meu_carro.start())
print(meu_carro.stop())


class Book:
  def __init__(self, titulo, author="Unknown"):
    self.titulo = titulo
    self.author = author
  
  def details(self):
    return f"'{self.titulo}' por {self.author}"
   
meu_livro = Book("O primeiro titulo", "Joao")
autor = Book("Unknown...")

print(meu_livro.details())
print(autor.details())
    


class Estudante:
  def __init__(self, nome, escolaridade):
    self.nome = nome
    self.escolaridade = escolaridade
    
  def saudacao(self):
    return f'O meu nome é {self.nome}, e tenho {self.escolaridade}.'
  
  
estudante1 = Estudante("Ana", "10th")
estudante2 = Estudante("Joao", "12th")

print(estudante1.saudacao())
print(estudante2.saudacao())




class Cadela:
    especie = "Canina familia"
    
    def __init__(self, nome, idade):
      self.nome = nome
      self.idade = idade
      
      
cadela1 = Cadela("Bobby", 5)
cadela2 = Cadela("Bibo", 7)

    
print(cadela1.nome)    
print(cadela2.idade)
print(cadela1.especie)


class Conta_Bancaria:
  def __init__(self, user, saldo):
    self.user = user
    self.saldo = saldo
    
    
  def deposito(self, valor):
    self.saldo += valor
    self.ultimo_deposito = valor
    return f'O seu saldo é {self.saldo}€.'
  
user1 = Conta_Bancaria("Joao", 1000)


print(user1.deposito(50))




class Pessoa:
  contador = 0
  
  def __init__(self, name):
    self.name = name
    Pessoa.contador += 1
    
    
p1 = Pessoa("Joao")
p2 = Pessoa("Ana")
p3 = Pessoa("Nano")


print(p1.name)
print(p2.name)
print(Pessoa.contador)


class Pessoas:
  contador = 0
  
  def __init__(self, idade):
    self.idade = idade
    Pessoas.contador += 1
    
  @classmethod
  
  def get_contador(cls):
    return cls.contador

p4 = Pessoas("Andre")
p5 = Pessoas("Ana")
p6 = Pessoas("Vitor")
  
  
print(Pessoas.get_contador())
   


class Temperatura:
  def __init__(self, grau):
    self.grau = grau
    
    
  def farhen(self):
    tempero = (self.grau - 32) * 5 / 9
    return tempero

  def celsius(self):
    return f"{self.grau} celsius!"




temp = Temperatura(100).farhen()
temp_celc = Temperatura(50).celsius()

print(temp)
print(temp_celc)