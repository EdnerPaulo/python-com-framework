# 1
# Trate o TypeError -  Qual expressão deve ser gerada para ele aparecer?
# try:
#    y = input("Digite seu texto aqui: ")
#    x = 5
#    print(y+x)

# except TypeError as erro:
#      print("Erro de tipo:", erro)


# 2
# Trate o ValueError -  Crie em python o erro 
# try:
#    a = int(input("Digite seu texto aqui"))
#    b = 5

#    print(a+b)
# except ValueError as erro:
#     print(erro) 


# 3
# Exercício: Dada uma lista, solicite ao usuário um índice e imprima o 
# elemento correspondente,
# lidando com exceções caso o índice fornecido esteja fora dos limites da lista.
# try:

#     z = int(input("Digite seu texto aqui: "))
#     lista=(1,2,3,4,5)
#     print(lista[z])

# except IndexError as erro:   
#     print(erro)  

# 4
# Peça ao usuário para inserir um número inteiro, tente convertê-lo 
# para um número real,
# lidando com exceções caso a entrada não seja um número ou não 
# seja possível converter para real.
# try:
#     c = int(input("Digite seu texto aqui: "))
#     d = float(c)
#     print(f"{c:.2f}")

# except ValueError as erro:
#     print("Erro: valor inválido")
# except TypeError as erro:
#     print(erro)   

# 5
# Exercício: Peça ao usuário para inserir dois números afaça a divisão do primeiro  
# pelo segundo, lidando com exceções caso o segundo número 
# seja zero.
try:
   e = float(input("Digite seu texto aqui: "))
   f = float(input("Digite seu texto aqui: "))
   
   print( e/f )  

except ZeroDivisionError as erro:
     print("Erro de tipo:", erro)

except ValueError:
    print("Erro: digite apenas números")

