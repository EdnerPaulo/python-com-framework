
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

### **6. Sequência de Fibonacci**

# Gere os primeiros N termos da sequência de Fibonacci, onde N é informado pelo usuário. Use `for` ou `while` para iterar.

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

### **7. Soma de Dígitos**

# Peça um número inteiro positivo e calcule a soma de seus dígitos. Use `while` para extrair os dígitos um a um.

# numero1 = int(input("Digite um número inteiro: "))
# soma = 0
# while numero1 > 0:
   
#     digito = numero1 % 10 # retorna o último dígito quando vc nao tem comparador 
#     soma += digito
#     print(soma)
#     numero1 = numero1 // 10 # Isso remove o último dígito pra poder retonar o loop, Repete até acabar os numeros
# print("Soma dos dígitos:", soma)


import datetime
### **8 Menu Interativo**

# Crie um menu que permaneça ativo até que o usuário escolha a opção `"Sair"`. As opções podem ser:

# - `1` – Exibir mensagem "Olá!"
# - `2` – Exibir a data/hora atual (use `import datetime`)
# - `3` – Sair

# Use `while True` e `break` para sair.
# print("Bem-vindo ao Sistema LoKo!")
# confirmacao= input('Gostaria de entrar no sistema LoKo? s/n ').lower()
# confirmado = confirmacao == 's' 
# if confirmado:
#     nome = input('Por favor, digite seu nome: ')
#     while True:
#             dados = { 1 :  "Olá! ",
#                 2 : "data/hora atual: ",
#                 3 : "Sair"}
#             print(dados)
#             escolha = int(input("Escolha as opções: "))

#             if escolha == 1:
#                 print(f" {dados[1]} {nome} voce esta no sistema LoKo escolha uma opção abaixo")
#             elif escolha == 2:
#                 data = datetime.datetime.now()
#                 print(f"{dados[2]} {data} ,agora no Brasil")
#             elif escolha == 3:
#                 print("Saindo...")
#                 print("Até logo do Sistema LoKo!")
#                 break
                
# else:
#     print("Até logo do Sistema LoKo!")



# ---

# ### **9 Simulador de Lançamento de Dados**

# Simule 100 lançamentos de um dado de 6 faces. Conte quantas vezes cada face foi sorteada e exiba o resultado. Use `for` e `random.randint(1,6)`. (Importe `random`.)

import random

# # contador para cada face do dado (1 a 6)
# contagem = {
#     1: 0,
#     2: 0,
#     3: 0,
#     4: 0,
#     5: 0,
#     6: 0
# }

# # simular 100 lançamentos
# for i in range(100):
#     dado = random.randint(1, 6)  # sorteia número de 1 a 6
#     contagem[dado] += 1          # soma +1 na face sorteada

# # mostrar resultado
# print("Resultado dos lançamentos:\n")

# for face in contagem:
#     print(f"Face {face}: {contagem[face]} vezes")
