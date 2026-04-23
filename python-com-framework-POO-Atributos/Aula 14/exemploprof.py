# class Dados:
#     def __init__(self):
#         self.nome = 'Ana' # publico
#         self._cpf = '123146' # protegido
#         self.__conta = '1213' # privado


#     def display(self):
#         print(self.nome)
#         print(self._cpf)
#         print(self.__conta)


# class Dados2(Dados):
#     def __init__(self):
#         super().__init__()
#         self.x  =  10
        
#     def mostrar(self):
#         print(self._Dados__conta)



# # d = Dados()
# # d.display()
# # print(d._Dados__conta)        
# # print('cpf', d._cpf)


# d2  =  Dados2()
# d2.display()
# d2.mostrar()


class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.emprestado =  False
    def emprestar(self):
        if not self.emprestado:
            self.emprestado = True 


    def devolver(self):
        self.emprestado = False


    def __str__(self):
        return f'NOME: {self.titulo} AUTOR:{self.autor} ANO:{self.ano}'


livro = Livro('antifragil', 'taleb', 2015)


livro.emprestar()
livro.devolver()


print(livro) 


    