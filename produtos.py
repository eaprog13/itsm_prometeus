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
    
p = Produto("teclado", "hardware", "12345")
p1 = Produto("rato", "hardware", "67890")
p2 = Produto("office", "software", "1234130")
    
print(p1.nome, p1.tipo)
print(p2.nome, p2.tipo)
print(Produto.contador)    
    
  
  
  