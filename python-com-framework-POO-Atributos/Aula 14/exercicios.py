
### **Exercício 1 – Livro**

# Crie uma classe `Livro` com atributos de instância: `titulo`, `autor`, `ano`, `emprestado` (booleano, padrão `False`). Métodos:

# - `emprestar()` – se disponível, muda `emprestado` para `True`.
# - `devolver()` – muda `emprestado` para `False`.
# - `__str__()` – retorna uma string com as informações.
    
#     Teste com dois livros.
    

# # ---
# class Livro:
#     def __init__(self, titulo, autor, ano):
#         self.titulo = titulo
#         self.autor = autor
#         self.ano = ano
#         self.emprestado =  False
#     def emprestar(self):
#         if not self.emprestado:
#             self.emprestado = True 


#     def devolver(self):
#         self.emprestado = False


#     def __str__(self):
#         return f'NOME: {self.titulo} AUTOR:{self.autor} ANO:{self.ano}'


# livro = Livro('antifragil', 'taleb', 2015)


# livro.emprestar()
# livro.devolver()


# print(livro) 


# ### **Exercício 2 – Contador com Atributo de Classe**

# Crie uma classe `Contador` que tenha um atributo de classe `total_contadores` que conta quantas instâncias foram criadas. Cada vez que um novo objeto é criado, esse contador deve ser incrementado. Adicione um método `exibir_total()` que exibe o total de contadores criados.

# class Contador:
    
#     total_contadores = 0  # atributo da classe se cria fora do contructor 
    
#     def __init__(self):
#         Contador.total_contadores += 1 
#         #sempre que algo novo acontece ele vai somar mais 1 (for criado)

#     def exibir_total(self):
#      print(f"Total de instâncias criadas: {Contador.total_contadores}")

# # Criamos 3 objetos diferentes
# obj1 = Contador()
# obj2 = Contador()
# obj3 = Contador()

# # Qualquer um deles vai mostrar o valor 3, pois o atributo é compartilhado com todos
# obj1.exibir_total()

# ---
# ### **Exercício 3 – Produto com Desconto**

# Classe `Produto` com atributos privados `_nome`, `_preco`, `_quantidade`. Use propriedades (`@property`) para acessar esses atributos. Crie um método `aplicar_desconto(percentual)` que reduz o preço. O preço não pode ficar negativo. Teste criando produtos e aplicando descontos.

# class Produto:
#     def __init__(self,nome, preco, quantidade):
#         self._nome = nome # chama todos os atributos como privado graças ao "_" Usa um underscore `_`.
#         self._preco = preco
#         self._quantidade = quantidade

#     @property # permite a visualizaçao dos atributos mesmo eles estando privados 
#     def nome(self):
#         return self._nome 

#     @property
#     def preco(self):
#         return self._preco 
    
#     @property
#     def quant(self):
#         return self._quantidade 

#     def aplicar_desconto(self, percentual):
#         valor_desconto = self._preco * (percentual / 100)
#         novo_preco = self._preco - valor_desconto
#         if novo_preco >= 0 and self._quantidade > 0 : # para que a preço nao seja menos que 0 e quantidade tbm 
#             self._preco = novo_preco
#         else:
#             print("Erro, preço abaixo de 0")# se o preço for menor que 0

# p1 = Produto("Notebook", 3000, 5)
# print(f"Produto: {p1.nome} Preço original: R$ {p1.preco}") # Acessa como se não fosse método graças ao @property o chamando 
# p1.aplicar_desconto(22) # Aplica desconto chamando a def
# print(f"Preço com desconto: R$ {p1.preco}")
# # ---

# ### **Exercício 4 – Banco com Saldo Privado**

# Classe `ContaBancaria` com atributo privado `__saldo`. Métodos:

# - `depositar(valor)` – aumenta saldo.
# - `sacar(valor)` – reduz saldo se houver saldo suficiente; senão, exibe mensagem.
# - `exibir_saldo()` – retorna o saldo (use propriedade `saldo` apenas para leitura).
    
#     Crie uma conta, realize operações e exiba o saldo.

class ContaBancaria:
    def __init__(self, deposito, sacar):
        self.valor_deposito = deposito
        self.valor_sacar = sacar
        self.__saldo = 50   # atributo privado com Usa um underscore `__`.

    def depositar(self):
        self.__saldo += self.valor_deposito # cria um novo saldo com o deposito 
        print(f'O valor depositado foi R$: {self.valor_deposito}')

    def sacar(self):
        if  self.__saldo > self.valor_sacar  : # verifica que tem saldo suficiente
            self.__saldo -= self.valor_sacar # se tiver efetua o saque
            print(f'o valor sacado foi R$: {self.valor_sacar}')
        else:
            print(f'Saque indisponivel, Saldo Insuficiente')

    def mostrar_saldo(self):
        novo_saldo = self.__saldo # mostra o nova saldo atualizado 
        print(f'Seu saldo atual é de R$: {novo_saldo}')
        

c = ContaBancaria(1000,500)
c.depositar()
c.sacar()
c.mostrar_saldo()

# ---

# ### **Exercício 5 – Aluno com Notas**

# Classe `Aluno` com atributos: `nome`, `matricula` e uma lista privada `__notas`. Métodos:

# - `adicionar_nota(nota)` – adiciona à lista (valida de 0 a 10).
# - `calcular_media()` – retorna a média.
# - `situacao()` – retorna "Aprovado" se média >= 7, "Recuperação" se >= 5, "Reprovado" caso contrário.
    
#     Teste com um aluno e algumas notas.
    

# ---

# ### **Exercício 6 – Data (validação)**

# Crie uma classe `Data` com atributos `dia`, `mes`, `ano`. No `__init__`, valide se a data é válida (considere meses com 30/31 dias e ano bissexto para fevereiro). Use propriedades para garantir que alterações futuras também sejam validadas. Adicione um método `__str__` que retorna a data no formato `dd/mm/aaaa`.

# ---

# ### **Exercício 7 – Funcionário com Aumento**

# Classe `Funcionario` com atributos: `nome`, `cargo`, `salario_base` (privado). Métodos:

# - `aumentar_salario(percentual)` – aumenta o salário.
# - `calcular_bonus()` – retorna 10% do salário base.
# - Propriedade `salario` para leitura.
    
#     Teste criando um funcionário, aumente o salário e mostre o novo valor.
    

# ---

# ### **Exercício 8 – Carro com Velocidade (Encapsulamento)**

# Classe `Carro` com atributos `marca`, `modelo` e `__velocidade` (inicial 0). Métodos:

# - `acelerar(valor)` – aumenta velocidade até no máximo 200.
# - `frear(valor)` – reduz velocidade até no mínimo 0.
# - Propriedade `velocidade` para leitura.
    
#     Teste acelerando e freando.
    

# ---

# ### **Exercício 9 – Estatísticas (Atributos de Classe)**

# Classe `Estatistica` com atributos de classe `soma` e `contagem`. Métodos de classe:

# - `adicionar(valor)` – atualiza soma e contagem.
# - `calcular_media()` – retorna a média (ou 0 se nenhum valor adicionado).
    
#     Use `@classmethod` e não crie instâncias. Teste adicionando números e exibindo a média.
    

# ---

# ### **Exercício 10 – Agenda com Contatos (Composição)**

# Crie uma classe `Contato` com atributos `nome`, `telefone`, `email`. Crie uma classe `Agenda` que possui uma lista privada de contatos. Métodos:

# - `adicionar_contato(contato)` – adiciona à lista.
# - `listar_contatos()` – exibe todos os contatos.
# - `buscar_contato(nome)` – exibe os dados do primeiro contato com aquele nome.
    
#     Teste adicionando vários contatos e fazendo buscas. 