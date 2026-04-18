# # **1- Classe Pessoa**

# # Crie uma classe `Pessoa` com os atributos `nome` e `idade`. Adicione um método `apresentar()` que exiba `"Olá, meu nome é [nome] e tenho [idade] anos."` Crie duas pessoas diferentes e chame o método.

# class Pessoa:
#     def __init__(self):
#         self.nome = input('Qual o seu Nome: ')
#         self.idade = input('Qual a sua Idade: ')
#       
        
#     def apresentar(self):
#         print(f'Olá, meu nome é {self.nome} e tenho {self.idade} anos.')

# cadastro = Pessoa()
# cadastro.apresentar()
# cadastro2.apresentar()

# ### **2.Classe Retângulo**

# Crie uma classe `Retangulo` com os atributos `largura` e `altura`. Adicione métodos:

# - `calcular_area()` – retorna a área
# - `calcular_perimetro()` – retorna o perímetro
    
#     Crie um retângulo com largura 5 e altura 3 e exiba sua área e perímetro.

# class Retangulo:
#     def __init__(self):
#         self.largura = float(input('Qual a largura do seu Retangulo: '))
#         self.altura = float(input('Qual a altura do seu Retangulo: '))

#     def calcular_area(self):
#         calcular_area = self.altura * self.largura
#         print(f'Area equivalente à {calcular_area}')
    
#     def calcular_perimetro(self):
#         calcular_perimetro = 2*(self.altura + self.largura)
#         print(f'O Perimetro é equivalente à {calcular_perimetro}')
    
# calculadora = Retangulo()
# calculadora.calcular_area()
# calculadora.calcular_perimetro()
    
# ---

# ### **3.   Classe Conta Bancária**

# Crie uma classe `ContaBancaria` com:

# - Atributos: `titular`, `saldo` (inicial 0)
# - Métodos:
#     - `depositar(valor)`: acrescenta ao saldo
#     - `sacar(valor)`: se houver saldo suficiente, subtrai; senão, exibe `"Saldo insuficiente"`
#     - `exibir_saldo()`: mostra o saldo formatado
        
#         Crie uma conta, faça depósitos e saques e exiba o saldo.

# class ContaBancaria:
#     def __init__(self):
#         self.titular = input("Qual o nome do Titular da conta: ")
#         self.saldo = 0

#     def depositar(self):
#         deposito = float(input('Quanto quer depositar na conta:R$ '))
#         self.saldo += deposito
#         print(f"Depósito de R$ {deposito} realizado!")

#     def sacar(self):
#         saque = float(input("Quanto voçê quer sacar:R$ "))
#         if self.saldo < saque:
#             print("Saldo Insuficinete")
#         else:
#             self.saldo -= saque
#             print(f"Voçê sacou R$ {saque}")
    
#     def exibir_saldo(self):
#         exibir = input("Quer saber o saldo da sua conta (sim/não)").lower()
#         if exibir == 'sim':
#             print (f"óLa {self.titular} o seu saldo atual é {self.saldo}")
#         else:
#             print(f"Obrigado e volte sempre {self.titular}")

# conta = ContaBancaria()
# conta.depositar()
# conta.sacar()
# conta.exibir_saldo()    

# ---

# ### **4. Classe Produto**

# Crie uma classe `Produto` com:

# - Atributos: `nome`, `preco`, `quantidade_estoque`
# - Métodos:
#     - `total_estoque()`: retorna `preco * quantidade_estoque`
#     - `adicionar_estoque(quantidade)`: aumenta a quantidade
#     - `remover_estoque(quantidade)`: diminui, mas não permite ficar negativo
        
#         Crie um produto, altere o estoque e exiba o valor total.
# class Produto:
#     def __init__(self):
#         self.nomeProduto= input("Qual o nome do Produto: ")
#         self.precoProduto = float(input("Diga o valor do Produto: "))
#         self.quantidade_estoque = int(input("Diga quantos Produtos temos em estorque: "))
    
#     def total_estoque(self):
#         valor_estoque = self.precoProduto * self.quantidade_estoque
#         print(f"Valor total do estoque em R$ {valor_estoque:.2f}")
    
#     def adicionar_estoque(self):
#         adicionar_estoque= int(input("Quanta novas unidades quer adicionar no estoque: "))
#         self.quantidade_estoque += adicionar_estoque
#         print(f'Voce tem agora no estoque {self.quantidade_estoque}')
    
#     def remover_estoque(self):
#         remover_estoque = int(input("Quantos unidades quer retirar do estoque: "))
#         if self.quantidade_estoque < remover_estoque:
#             print(f"Não pode remover {remover_estoque}, pois não possuimos está quantidade.")
#         else:
#             self.quantidade_estoque -= remover_estoque
#             print(f'Voce tem agora no estoque {self.quantidade_estoque}')

# produto = Produto()
# produto.total_estoque()
# produto.adicionar_estoque()
# produto.remover_estoque()


# ---

# ### **5. Classe Aluno**

# Crie uma classe `Aluno` com:

# - Atributos: `nome`, `matricula`, `notas` (lista de floats)
# - Métodos:
#     - `adicionar_nota(nota)`: adiciona à lista
#     - `calcular_media()`: retorna a média das notas
#     - `situacao()`: retorna `"Aprovado"` se média >= 7, `"Recuperação"` se >= 5, `"Reprovado"` caso contrário
        
#         Crie um aluno, adicione 3 notas e exiba sua situação.

class Aluno:
    def __init__(self):
        self.nomeAluno = input("Qual o nome do Aluno: ")
        self.matriculaAluno = int(input("Qual o numero de Matricula do Aluno: "))
        self.notas = []
    
    def adicionar_nota(self):
        for i in range(1,4):
            nota = float(input(f"Digite a {i}ª nota do(a) Aluno(a) {self.nomeAluno}: "))
            self.notas.append(nota)
       
    
    def calcular_media(self):
        media = sum(self.notas)/ len(self.notas)
        return media 
    
    def situacao(self):
        media = self.calcular_media()
        print(f"A sua Media foi {media:.1f}")
        if media < 5 :
            print("Reprovado")
        elif 5 <= media < 7 :
            print("Recuperação")
        else:
            print("Aprovado")

notasAluno = Aluno()
notasAluno.adicionar_nota()
notasAluno.calcular_media()
notasAluno.situacao()
        