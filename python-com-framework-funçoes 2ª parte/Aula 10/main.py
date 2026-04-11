# ### **Validador de CPF (simplificado)**

# Crie uma função `validar_cpf(cpf)` que recebe uma string com 11 dígitos e retorna `True` se for válido (use o algoritmo básico de validação de CPF). Em seguida, teste a função com alguns CPFs.

# def validar_cpf(cpf):
#     if len(cpf) == 11: 
#         return True
#     else:
#         print("Quantidade de numeros incorreta!")
#         return False
#     # --- VALIDAÇÃO DO PRIMEIRO DÍGITO ---
#     soma_1 = 0
#     # Multiplica os 9 primeiros dígitos por 10, 9, 8... até 2
#     for i in range(9):
#         soma_1 += int(cpf[i]) * (10 - i)

# # --- VALIDAÇÃO DO SEGUNDO DÍGITO ---
#     soma_2 = 0
#     # Agora considera os 10 primeiros dígitos (incluindo o que acabamos de validar)
#     # Multiplica por 11, 10, 9... até 2
#     for i in range(10):
#         soma_2 += int(cpf[i]) * (11 - i)
        
#     resto_2 = (soma_2 * 10) % 11
    
#     if resto_2 == 10:
#         resto_2 = 0
        
#     # Verifica o segundo dígito verificador (índice 10)
#     if resto_2 != int(cpf[10]):
#         return False

#     # Se passou por tudo, o CPF é válido!
#     return True

# # --- TESTE ---
# num = input("Digite o CPF para validar: ")
# if validar_cpf(num):
#     print(f"O CPF {num} é VÁLIDO!")
# else:
#     print(f"O CPF {num} é INVÁLIDO!")


# ### **3. Gerador de Tabuada**

# Escreva uma função `tabuada(numero, inicio=1, fim=10)` que exibe a tabuada do `numero` no intervalo `[inicio, fim]`. Se os argumentos `inicio` e `fim` não forem fornecidos, use 1 e 10.
# def taboada(numero, inicio=1, fim=10):
#     for i in range(inicio, fim + 1):
#         multi = numero * i
#         print(f"{numero} X {i} = {multi}")

# # def taboada(numero):
# #     for i in range(1,11):
# #         result = numero * i
# #         print(f"{numero} X {i} = {result}")
     

# x =  int(input("Qual tabuada quer saber, digite um numero: "))

# taboada(x)

# ### **4. Contador de Palavras**

# Crie uma função `contar_palavras(texto)` que retorna um dicionário com a contagem de cada palavra no texto (considere palavras separadas por espaços). O programa principal deve ler uma frase e exibir o resultado.
# def contar_palavras(texto):
#     palavras = len(texto)
#     print(f"Sua frase tem {palavras} de palavras contado os espaços")

# frase = input("Digite uma frase e veja a magica: ")

# contar_palavras(frase)

# def contar_palavras(texto):
#     lista_de_palavras = texto.split()
#     contagem = {}

#     for palavra in lista_de_palavras:
#         if palavra in contagem:
#             contagem[palavra] += 1
#         else:
#             contagem[palavra] = 1
            
#     return contagem

# frase = input("Digite uma frase e veja a mágica: ")
# resultado = contar_palavras(frase)

# print("\n--- Resultado da Contagem ---")
# # Aqui está o segredo: percorrer as chaves e valores do dicionário
# for palavra, quantidade in resultado.items():
#     print(f"A palavra '{palavra}' apareceu {quantidade}x")

# ### **5. Ordenação Personalizada**

# Implemente uma função `ordenar_lista(lista, crescente=True)` que retorna uma nova lista ordenada. Se `crescente=True`, ordena em ordem crescente; caso contrário, decrescente. Não use `sorted()` ou `list.sort()` (implemente o algoritmo de ordenação de sua escolha, como bolha).
# def ordenar_lista(lista, crescente=True):
#     nova_lista= lista.copy()
#     # nova_lista= lista[:] tambem serve pra copiar a lista em um novo lugar ok
#     n= len(nova_lista)
#     for i in range(n):
#         indice_alvo = i
#         for j in range(i+1,n):
#             if crescente:
#                 if nova_lista[j] < nova_lista[indice_alvo]:
#                     indice_alvo = j
#             else:
#                 if nova_lista[j] > nova_lista[indice_alvo]:
#                     indice_alvo = j
#         nova_lista[i],nova_lista[indice_alvo] = nova_lista[indice_alvo], nova_lista[i]

#     return nova_lista

# numeros =[]
# # numeros = [64, 34, 25, 12, 22, 11, 90]
# # criando uma lista com um for e ainda colocando em ordem
# for i in range(5):
#     num = int(input(F"Digite sua Lista {i+1}º numero: "))
#     numeros.append(num)
# print("Lista Ordenada:", ordenar_lista(numeros))
# print("Decrescente:", ordenar_lista(numeros, crescente=False))
# ordenar_lista(numeros)
 



# ### **6. Jogo de Adivinhação**
import random

# Crie uma função `jogar()` que sorteia um número entre 1 e 100 e dá dicas ("maior", "menor") até o usuário acertar. Use `random.randint()`. A função deve retornar o número de tentativas. No programa principal, chame a função e exiba quantas tentativas foram necessárias.
# def jogar():
#     num_secreto = random.randint(1,100)
#     tentativas = 0
#     acertou = False
#     print ("Tente acertar o numero: ")
#     while not acertou:
#         chute = int(input("Qual vai ser o seu chute: "))
#         tentativas += 1
#         if chute == num_secreto:
#             print(f"Parabens, acertou {num_secreto} em apenas {tentativas} tentativa(s).")
#             acertou= True
#         elif chute < num_secreto:
#             print("Tente um numero Maior")
#         else:
#             print("Tente um numero Menor")
    
#     return tentativas
# jogar()   


# ### **7. Conversor de Bases**

# Escreva uma função `converter_base(numero, base_origem, base_destino)` que converte um número entre bases 2, 8, 10 e 16. A entrada `numero` é uma string. A função retorna a string convertida. (Exemplo: `converter_base("1010", 2, 16)` → `"A"`). Use `int()` com base e depois formate.
# ### **8. Sistema de Caixa Eletrônico**
# def converter_base(numero, base_origem, base_destino)

# Crie uma função `sacar(valor)` que retorna um dicionário com a quantidade de notas de 100, 50, 20, 10, 5 e 2 necessárias para o valor. O valor deve ser inteiro e positivo. Caso não seja possível (valor não múltiplo de 2), a função retorna `None`. No programa principal, chame a função e exiba o resultado.

# ### **9. Análise de Lista com Múltiplos Retornos**

# Escreva uma função `analisar_lista(lista)` que retorna quatro valores: o menor valor, o maior valor, a soma e a média. No programa principal, receba uma lista de números do usuário (terminada por -1) e exiba os resultados usando desempacotamento.

# ### **10. Função que Modifica Lista Global**

# Crie uma lista global `estoque = []`. Escreva funções:

# - `adicionar_produto(nome, quantidade)`: adiciona um dicionário `{"nome": nome, "quantidade": quantidade}` à lista global.
# - `remover_produto(nome)`: remove o produto com esse nome (se existir).
# - `listar_estoque()`: exibe todos os produtos.
    
#     Use a palavra-chave `global` para modificar a lista dentro das funções. O programa principal deve apresentar um menu interativo para o usuário.