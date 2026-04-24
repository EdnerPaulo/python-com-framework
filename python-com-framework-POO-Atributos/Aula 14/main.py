# class Contador:
#     total_contadores  = 0
#     def __init__(self):
#         Contador.total_contadores += 1

#     def exibir_total(self):
#         print(Contador.total_contadores)


# c  =  Contador()
# c1 =  Contador()
# c2 =  Contador()

# c.exibir_total()



# class Produto:
#     def __init__(self, nome, quantidade, preco):
#         self._nome = nome
#         self._quantidade =  quantidade
#         self._preco = preco
    

#     @property
#     def preco(self):
#         return self._preco    

        
#     def aplicar_desconto(self, percentual):
#         desconto =  self._preco * (percentual /100) 
#         n_valor  = self._preco  - desconto  
#         if n_valor < 1:
#             return 'não pode ficar negativo'
#         else:
#             return n_valor

# p = Produto('x', 5, 100)
# print(p.aplicar_desconto(10))



# class ContaBancaria:
#     def __init__(self):
#         self.__saldo = 100

#     def depositar(self, valor):
#         self.__saldo += valor
#         return self.__saldo

#     def sacar(self, valor):
#         if self.__saldo < valor:
#             return 'Saldo insuficiente'
#         else:    
#             self.__saldo -= valor
#             return self.__saldo   

#     @property
#     def exibir_saldo(self):
#         return self.__saldo        
    
# c =  ContaBancaria()
# print(c.depositar(100))
# print(c.sacar(50))
# print(c.exibir_saldo)    

# class Aluno:
#     def __init__(self, nome, matricula):
#         self.nome = nome
#         self.matricula  =  matricula
#         self.__notas = []

#     def adicionar_nota(self, nota):
#         if nota >=0 and nota <=10:
#            self.__notas.append(nota)
#            return self.__notas
           
#         else:
#              return 'Adicione uma nota valida'


#     def calcula_media(self):
#         media  =  sum(self.__notas)/len(self.__notas) 
#         return  media  

#     def situacao(self):
#         media =  self.calcula_media()
#         if media >= 7:
#             return 'aprovado'
#         else:
#             return 'recuperação'  

# a = Aluno('joao', '1')
# print(a.adicionar_nota(6))
# print(a.adicionar_nota(11))
# print(a.adicionar_nota(10))
# print(a.calcula_media())
# print(a.situacao())        



# class Data:
#     def __init__(self, dia, mes, ano):
#         self.dia = dia
#         self.mes = mes
#         self.ano = ano

#     def verificar(self):
#         meses   =  [0,1,2,3,4,5,6,7,8,9,10,11,12]
#         dias_meses = [0,list(range(0,31)),
#                     list(range(0,29)),
#                     list(range(0,31)),
#                     list(range(0,30)),
#                     list(range(0,31)),
#                     list(range(0,30)),
#                     list(range(0,31)),
#                     list(range(0,31)),
#                     list(range(0,30)),
#                     list(range(0,31)),
#                     list(range(0,30)),
#                     list(range(0,31))
#                     ]



#         if (self.ano % 400 == 0 or self.ano % 4 == 0) or (self.ano % 100 ==0):
#             print('ano bissexto...')
#         else:
#             print('Não é bissexto...')

#         if self.mes in meses:
#             i =  meses.index(self.mes)
#             if self.dia in dias_meses[i]:
#                 print('data válida')
#         else:
#             print('Data invalida')



#     def __str__(self):
#         return self.dia, self.mes, self.ano     


# d = Data(1,11,1988)
# d.verificar()




# class Funcionario:
#     def __init__(self, nome, cargo, salario):
#         self._nome = nome
#         self._cargo =  cargo
#         self._salario = salario


#     def aumentar_salario(self, percentual):
#         n_sal =  self._salario * (percentual /100) 
#         return n_sal
    
#     def calcular_bonus(self):
#         x  =  self.aumentar_salario(10)
#         self._salario += self._salario * 0.10
#         v_total =  self._salario + x
#         return v_total
    

# p = Funcionario('kaio', 'dev', 5000)
# print(p.aumentar_salario(10))
# print(p.calcular_bonus())


# class Carro:
#     def __init__(self, marca, modelo):
#         self.marca =  marca
#         self.modelo =  modelo
#         self.__velocidade = 0

#     def aumenta_velocidade(self, valor):
#           for x in range(valor):
#               self.__velocidade += valor
#               return   self.__velocidade
          
   
#     def frear(self, valor):
        
#         for x in range(self.__velocidade, valor,-1):
#             self.__velocidade -= valor
#             return self.__velocidade


# c =  Carro('jeep', '2026')
# print(c.aumenta_velocidade(151))
# print(c.frear(50))



# class Estatistica: 
#        soma  =  0
#        contagem  =  0

#        @classmethod
#        def adcionar(cls, valor):
#               cls.soma += valor
#               cls.contagem += 1

#        @classmethod
#        def calcular_media(cls):
#               if cls.contagem ==  0:
#                      return 0
#               return cls.soma / cls.contagem

# Estatistica.adcionar(10)
# Estatistica.adcionar(5)
# Estatistica.adcionar(7)
# print(Estatistica.calcular_media())             


class Contatos:
    def __init__(self, nome, telefone, email):
        self.nome  = nome
        self.telefone = telefone
        self.email  = email
        



class Agenda:
    def __init__(self):
        self.__lista = []

    def add(self, contato):
        self.__lista.append(contato)
      

    def listar_contatos(self):
        return self.__lista
        
        

    def buscar(self,nome) :
        if nome in self.__lista:
            return nome
        else:
            return 'não existe...'   


c =  Contatos('a','132','a@gmail.com')
c2 =  Contatos('b','132','b@gmail.com')
c3 =  Contatos('b','132','b@gmail.com')
agenda = Agenda()



# agenda.add(c)
# agenda.add(c2)
# agenda.add(c3)
agenda.add(c.nome)
agenda.add(c.telefone)
agenda.add(c.email)
agenda.add(c2.nome)
agenda.add(c2.telefone)
agenda.add(c2.email)
print(agenda.listar_contatos())
print(agenda.buscar('a'))