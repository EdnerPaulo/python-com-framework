class Celular:
    def __init__(self, modelo='IPHONE 6', cor='Preto', tipo='PRO'):
        self.modelo = modelo
        self.cor = cor
        self.tipo = tipo

    def display(self):
        print(f'Celular -  {self.modelo}| Cor - {self.cor}| Pro - {self.tipo}')

c = Celular()
c2 = Celular('XAIOME','Azul', 'Max')
c3 = Celular('SANSUNG','Prata','X')
c4 = Celular('MOTOROLA', 'Branco', 'Beta' )




c.display()
c2.display()
c3.display()
c4.display()
