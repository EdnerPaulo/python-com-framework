
# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade

#     def exibir(self):
#         print(f"{self.nome} tem {self.idade} anos")

# # Uso
# p = Pessoa("Ana", 25)
# p.exibir()                     # o objeto sabe seu próprio estado

# Dados separados
# pessoas = []

# def criar_pessoa(nome, idade):
#     return {"nome": nome, "idade": idade}

# def adicionar_pessoa(lista, pessoa):
#     lista.append(pessoa)

# def exibir_pessoas(lista):
#     for p in lista:
#         print(f"{p['nome']} tem {p['idade']} anos")

# # Uso
# p = criar_pessoa("Ana", 25)
# p2 = criar_pessoa("Anaconda", 30)
# adicionar_pessoa(pessoas, p)
# adicionar_pessoa(pessoas, p2)
# exibir_pessoas(pessoas)

# class Carro:
#     def __init__(self, modelo):
#         self.modelo = modelo     # atributo de instância

# c1 = Carro("Uno")
# c2 = Carro("Gol")
# print(c1.modelo)  # Uno
# print(c2.modelo)  # Gol

# class Carro:
#     rodas = 4                 # atributo de classe 

#     def __init__(self, modelo):
#         self.modelo = modelo

# c1 = Carro("Uno")
# c2 = Carro("Gol")
# print(c1.rodas)  # 4
# print(Carro.rodas)  # 4
# Carro.rodas = 5
# print(c1.rodas)  # 5

# class Conta:
#     def __init__(self, saldo):
#         self.__saldo = saldo       # privado
#         self._titular = "João"     # protegido

#     def depositar(self, valor):
#         self.__saldo += valor

#     def get_saldo(self):
#         return self.__saldo

# c = Conta(100)
# c.depositar(50)
# print(c.get_saldo())      # 150
# print(c.__saldo)        # AttributeError
# print(c._Conta__saldo)    # 150 (não recomendado)

class Temperatura:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, valor):
        if valor < -273.15:
            raise ValueError("Abaixo do zero absoluto")
        self._celsius = valor

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

t = Temperatura(25)
print(t.celsius)       # 25
t.celsius = 30
print(t.fahrenheit)    # 86.0