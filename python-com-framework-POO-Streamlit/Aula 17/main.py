# ## **Exercícios extra com Streamlit…**
import streamlit as st

# **Classe Livro** – crie uma classe com atributos título, autor, ano. Adicione um método `__str__`. Crie uma subclasse `LivroDigital` que adiciona atributo `formato` e sobrescreva `__str__`.
st.title('Biblioteca do Mundo')
class Livro:
    def __init__(self,titulo,autor,ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        
    def __str__(self):
        return f"{self.titulo} - {self.autor} ({self.ano})"
    
    def titulo(self):
        return 'Temos varios titulos renomados'
    
    def autor(self):
        return 'Temos autores achamados pelos criticos'
    
    def ano(self):
        return 'Temos livros seculares'

class LivroDigital(Livro):
    def __init__(self, titulo, autor, ano, formato):
        super().__init__(titulo, autor, ano)
        self.formato = formato
    
    def __str__(self):
        return f"{super().__str__()} [Formato: {self.formato}]"

    def formato(self):
        return 'Temos livros em pdf'

st.title('Titulo -- Autor -- Ano')
st.write('Escolha um ...')
opcao = st.selectbox(
    'Escolha o tema ',
    ['','Titulo','Autor', 'Ano']
)
if opcao == 'Titulo':
    Livro = titulo()
if opcao == 'Autor':
    Livro = autor()
elif opcao == 'Ano':
    Livro = ano()
elif opcao == 'LivroDigital':
    Livro = formato()

st.subheader('RESULTADO')
st.success(livro.executar())


# st.title('Doações -- Emprestimos -- Consulta')
# opcao2 = st.selectbox(
#     'Escolha a Linguagem ',
#     ['','Doações','Emprestimo', 'Consulta']
# )
# if opcao2 == '':
#     linguagem = Linguagem()
# if opcao2 == 'Python':
#     linguagem = Python()
# elif opcao2 == 'Go':
#     linguagem = Go()
# elif opcao2 == 'JavaScript':
#     linguagem = JavaScript()

# livro1 = Livro("Dom Casmurro", "Machado de Assis", 1899)
# livro2 = LivroDigital("O Guia do Mochileiro", "Douglas Adams", 1979, "PDF")

# print(livro1)
# print(livro2)



# **Classe Abstrata Veiculo** – defina uma classe abstrata com método `mover`. Implemente `Carro` e `Bicicleta` com comportamentos diferentes. Teste o polimorfismo.

# **Sobrecarga de operador** – crie uma classe `Vetor` com atributos x, y e implemente `__add__`, `__sub__`, `__mul__` (escalar).

# **Classe anônima** – use `type` para criar uma classe dinâmica com um método `saudacao`. Instancie-a.



