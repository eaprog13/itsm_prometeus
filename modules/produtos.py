from datetime import datetime

class Produto:
  
  contador = 0
  lista_produtos = []
  
  def __init__ (self, nome, categoria, n_serie):
  
    Produto.contador += 1
    self.produto_id = Produto.contador
    self.nome = nome
    self.categoria = categoria
    self.n_serie = n_serie
    self.produto_criado_em = datetime.now()
  
  def mostrar_produto(self):
    print('\n----------PRODUTO----------')
    print(f'Id: {self.produto_id}\n | Nome: {self.nome} |\n | Categoria: {self.categoria} |\n | NºSérie: {self.n_serie} |\n | Criado me: {self.produto_criado_em:%d/%m/%Y %H:%M:%S}|\n')
    
  def editar(self, nome, categoria, n_serie):
    self.nome = nome
    self.categoria = categoria
    self.n_serie = n_serie
    print(f'| O produto {self.nome} foi actualizado!')
  
  def eliminar(self):
    Produto.lista_produtos.remove(self)
    print(f'| O produto {self.nome} foi eliminado!')
    
  #ENCAPSULAR
  
  @property
  def nome(self):
    return self.__nome

  @nome.setter
  def nome(self,valor):
    if not valor or valor.strip() == '':
      print('| Erro: o nome não pode estar vazio!')
    else:
      self.__nome = valor
  
  
  # métodos de classe
  @classmethod
  
  def criar(cls, nome, categoria, n_serie):
    p = cls(nome, categoria, n_serie)
    cls.lista_produtos.append(p)
    print(f'| O produto {nome} foi criado!')
    
  @classmethod    
  def consultar_lista(cls):
    if len(cls.lista_produtos) == 0:
      print(f'| Ainda não há produtos registados!')
    else:
      for p in cls.lista_produtos:
        p.mostrar_produto()   
    