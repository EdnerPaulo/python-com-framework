# ### **1. Classe Livro**

# Crie uma classe `Livro` com:

# - Atributos: `titulo`, `autor`, `ano`, `disponivel` (booleano, padrão True)
# - Métodos:
#     - `emprestar()`: se disponível, marca como False e exibe `"Livro emprestado"`; senão, exibe `"Indisponível"`
#     - `devolver()`: marca como True e exibe `"Livro devolvido"`
#     - `info()`: mostra todas as informações do livro
        
#         Crie dois livros, faça empréstimos e devoluções.
class Livro:

         titulo`, `autor`, `ano`, `disponivel

# ---

# ### **2. Classe Funcionário**

# Crie uma classe `Funcionario` com:

# - Atributos: `nome`, `cargo`, `salario_base`
# - Métodos:
#     - `aumentar_salario(percentual)`: aumenta o salário com base no percentual
#     - `calcular_bonus()`: retorna 10% do salário base
#     - `exibir_dados()`: exibe todas as informações
        
#         Crie um funcionário, aumente o salário e mostre os dados atualizados.
        

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