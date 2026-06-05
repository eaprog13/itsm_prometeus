from datetime import datetime

class Produto:
  
  contador = 0
  lista_produtos = []
  
  def __init__ (self, nome, tipo, n_serie):
  
    Produto.contador += 1
    self.produto_id = Produto.contador
    self.nome = nome
    self.tipo = tipo
    self.n_serie = n_serie
    self.produto_criado_em = datetime.now()
  
  def mostrar_obj(self):
    print('\n----------PRODUTO----------')
    print(f'Id: {self.produto_id}\n | Nome: {self.nome} |\n | Tipo: {self.tipo} |\n | NºSérie: {self.n_serie} |\n | Criado me: {self.produto_criado_em:%d/%m/%Y %H:%M:%S}|\n')
    
  def editar(self, nome, tipo, n_serie):
    self.nome = nome
    self.tipo = tipo
    self.n_serie = n_serie
    print(f'O produto {self.nome} foi actualizado!')
  
  def eliminar(self):
    Produto.lista_produtos.remove(self)
    print(f'O produto {self.nome} foi eliminado!')
    
    
  # métodos de classe
  @classmethod
  
  def criar(cls, nome, tipo, n_serie):
    p = cls(nome, tipo, n_serie)
    cls.lista_produtos.append(p)
    print(f'O produto {nome} foi criado!')
    
  @classmethod    
  def mostrar_lista(cls):
    if len(cls.lista_produtos) == 0:
      print(f'Ainda não há produtos registados!')
    else:
      for p in cls.lista_produtos:
        p.mostrar()   
    