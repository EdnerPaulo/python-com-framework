#  Exercícios**

# 1. Tabuada Personalizada**
# Peça ao usuário um número inteiro positivo. Use `for` para exibir a tabuada desse número de 1 a 10.
# Exemplo:
# `Digite um número: 7` → exibe 7 x 1 = 7, 7 x 2 = 14, ..., 7 x 10 = 70.
# numero = int(input('Digite um número: '))

# for i in range(11):
#     x = numero * i
#     print(f"{numero} X {i} = {x}")

# ---

#2. Contagem Regressiva com Pausa**
# Peça um número inteiro positivo. Use `while` para fazer uma contagem regressiva até 0, exibindo cada número. Após o término, exiba `"Fogo!"`.
# contador = int(input('Digite um número positivo pra contagem regressiva: '))

# while contador >= 0:
#     print(contador)
#     contador -= 1

# print("Fogo!")
# ---

# ### **3. Média de Notas com `while`**
# Peça notas até que o usuário digite `-1`. Calcule e exiba a média das notas válidas (0 a 10). Ignore entradas inválidas e use `continue` quando necessário.
# soma = 0
# quantidade = 0

# while 1:
#     nota = float(input("Digite uma nota: "))

#     if nota == -1:
#         break

#     if nota < 0 or nota > 10:
#         print("Nota inválida! Digite valores entre 0 e 10.")
#         continue

#     soma += nota
#     quantidade += 1

# if quantidade > 0:
#     media = soma / quantidade
#     print(f"Média: {media:.2f}")
# else:
#     print("Nenhuma nota válida foi digitada.")

# ---

# ### **4. Validação de Senha com Limite de Tentativas**

# Defina uma senha fixa (ex: `"python123"`). Dê ao usuário 3 tentativas usando `while`. Se acertar, exiba `"Acesso liberado"` e encerre. Se errar todas, exiba `"Conta bloqueada"`.
# tentativa = 3
# senha = "python123"
# while tentativa > 0:
#     nova_senha = input("Digite sua senha: ")
#     if senha == nova_senha:
#         print ("Acesso liberado")
#         break
#     else:
#         print(f"Senha incorreta! Tentativas restantes: {tentativa-1}")
#         tentativa -= 1
        
# if tentativa == 0:
#     print("Conta bloqueada")

# ---
# ### **5. Números Primos**
# Peça um número inteiro positivo e determine se ele é primo. Use `for` com `range` e `break` para otimizar.
# numero = int(input("Digite um número inteiro positivo: "))

# if numero <= 1:
#     print("Não é primo")
# else:
#     primo = True

#     for i in range(2, numero):
#         if numero % i == 0:
#             primo = False
#             break

#     if primo:
#         print(f"{numero} é um número primo")
#     else:
#         print(f"{numero} não é um número primo")

# Crie um programa com a sequência de Fibonacci e depois comparar com um número digitado pelo usuário

# numero = int(input("Digite um número: "))

# a = 0
# b = 1

# while a <= numero:
#     if a == numero:
#         print(f"{numero} pertence à sequência de Fibonacci")
#         break

#     a, b = b, a + b
#     c=   a, b = b, a + b

# else:
#     print(f"{numero} NÃO pertence à sequência de Fibonacci")

# print(c)