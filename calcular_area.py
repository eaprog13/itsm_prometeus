def calcular_area(largura, comprimento):
  return largura * comprimento

largura = 10
comprimento = 20
area = largura * comprimento
print(area)

area2 = calcular_area(10, 20)  
print(area2)


print(calcular_area(10,20))


class Retangulo:
  def __init__(self, r_largura, r_comprimento):
    self.r_largura = r_largura
    self.r_comprimento = r_comprimento
    
  def calcular_retangulo(self):
    return self.r_largura * self.r_comprimento


r = Retangulo(10, 20)
area_2 = r.calcular_retangulo()

print(f'Area = {area_2}')

print(f'A área de um retangulo com {r.r_largura} de largura e {r.r_comprimento} de comprimento é:{r.calcular_retangulo()}')


class Cao:
  def __init__(self, nome, raca, idade):
    self.nome = nome
    self.raca = raca
    self.idade = idade
    
  def ladrar(self):
    return f'{self.nome} está a ladrar - Woof Woof!'
  

meu_cao = Cao("Bobby", "Laborador", "10")
print(meu_cao.ladrar())


class Circulo:
  def __init__(self, radio):
    self.radio = radio
    
  def area(self):
    return 3.14 * self.radio ** 2
  
meu_circulo = Circulo(5)

print(f'A área do meu círculo é de:{meu_circulo.area()}')
