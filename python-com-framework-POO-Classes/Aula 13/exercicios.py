# ### **1. Classe Livro**

# Crie uma classe `Livro` com:

# - Atributos: `titulo`, `autor`, `ano`, `disponivel` (booleano, padrão True)
# - Métodos:
#     - `emprestar()`: se disponível, marca como False e exibe `"Livro emprestado"`; senão, exibe `"Indisponível"`
#     - `devolver()`: marca como True e exibe `"Livro devolvido"`
#     - `info()`: mostra todas as informações do livro
        
#         Crie dois livros, faça empréstimos e devoluções.
# class Livro:

#     def __init__(self,titulo,autor,ano): 
#         self.titulo = titulo
#         self.autor = autor
#         self.ano = ano
#         self.disponivel = True
        
#     def emprestar(self):
   
#         if  self.disponivel:
#             self.disponivel = False
#             print('Livro emprestado\n')
#         else:
#             print('Indisponível\n')
    
#     def devolver(self):
#         self.disponivel = True
#         print('Livro Devolvido')

#     def info(self):
#         status = "Disponível" if self.disponivel else "Indisponível"
#         print(f"\nTítulo: {self.titulo}\nAutor: {self.autor}\nAno: {self.ano}\nStatus: {status}")
        
# livro = Livro("O Hobbit", "J. R. R. Tolkien", 1937)
# livro1 = Livro("Continnetum", "Edner Paulo", 2024)
# livro.info()
# livro.emprestar()
# livro.devolver()
# livro1.info()
# livro1.emprestar()
# livro1.devolver()


# # ---
#  self.titulo = input('Escolha o livro pelo Titulo: ')
#             self.autor = input('Qual o nome do Autor: ')
#             self.ano = int(input('Qual o ano de Publicação: '))
#             self.disponivel = input('O livro está desponivel(sim\não): ')
# ### **2. Classe Funcionário**

# Crie uma classe `Funcionario` com:

# - Atributos: `nome`, `cargo`, `salario_base`
# - Métodos:
#     - `aumentar_salario(percentual)`: aumenta o salário com base no percentual
#     - `calcular_bonus()`: retorna 10% do salário base
#     - `exibir_dados()`: exibe todas as informações
        
#         Crie um funcionário, aumente o salário e mostre os dados atualizados.
class Funcionario:
    def __init__(self):
        self.nome = input('Qual o Nome do Funcionario: ')
        self.cargo = input('Qual o Cargo do Funcionario: ')
        self.salario_base = float(input('Qual o Salario Base do Funcionario: '))

    def calcular_bonus(self):
        bonus =  self.salario_base * 0.10
        print(f'10% do salário base é {bonus}')

    def aumentar_salario(self):
        percentual = float(input(f"Quantos percento de aumento {self.nome} vai ganhar: % "))
        aumento = float(percentual/100)* self.salario_base
        print(f'O aumento foi de {aumento}')
        self.salario_base +=aumento
        return aumento
      
    
    def exibir_dados(self):
        novo_salario = self.salario_base
        print(f'o Funcionario {self.nome} no cargo de {self.cargo} com o salario atualizado de {novo_salario}')

colaborador = Funcionario()
colaborador.aumentar_salario()
colaborador.calcular_bonus()
colaborador.exibir_dados()


# ---

# ### **3./ Classe Calculadora (estática)**

# Crie uma classe `Calculadora` que **não precisa de atributos**. Apenas métodos de classe (use `@classmethod` ou métodos estáticos) para:

# - `somar(a, b)`
# - `subtrair(a, b)`
# - `multiplicar(a, b)`
# - `dividir(a, b)`
    
#     Teste os métodos sem criar objetos (chamando diretamente pela classe).
    

# ---

# ### **4. Classe Carro com Controle de Velocidade**

# Crie uma classe `Carro` com:

# - Atributos: `marca`, `modelo`, `velocidade` (inicial 0)
# - Métodos:
#     - `acelerar(valor)`: aumenta a velocidade (não pode ultrapassar 200 km/h)
#     - `frear(valor)`: diminui a velocidade (não pode ficar negativa)
#     - `velocidade_atual()`: exibe a velocidade
        
#         Crie um carro, acelere e freie até parar.
        

# ---

# ### **5. Classe Agenda**

# Crie uma classe `Agenda` que armazena contatos. Cada contato é um objeto da classe `Contato` (crie-a separada), com `nome`, `telefone` e `email`. A classe `Agenda` deve ter:

# - Atributo: `contatos` (lista)
# - Métodos:
#     - `adicionar_contato(contato)`: adiciona à lista
#     - `listar_contatos()`: exibe todos os contatos
#     - `buscar_contato(nome)`: exibe os dados do contato (se existir)
        
#         Crie alguns contatos, adicione-os à agenda e faça buscas.