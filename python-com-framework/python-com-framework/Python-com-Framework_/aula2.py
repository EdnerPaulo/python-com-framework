# 4  tipos
# str      int             float    bool
# textos numeros inteiros reais lógicos
# 'texto',  10 ,  5.2 ,  True , False
# 'Bom dia', 2026,1.80, 1 , 0
# 'Seu nome:',1, 60.200, 
# 'R$'

# ESTRUTURAS DE DADOS ****

# espaços na memória ram da maquina
# variar
# variaveis são dados únicos
# interpertador 
# meio termo linguagem 
# força indentação = organização
# OUTPUT - SAIDA - print()
# nomear de forma semantica  -  boa pratica

# regras para criar variáveis:
# _ ou letra
# não pode começar por números 
# não pode carcateres especiais 
# pode utilizar números(só não pode começar)
# palavra composta snake_case

# linguagem alto nivel
# interpretada
# dinamica - variáveis

# print('CADASTRO DE USUÁRIOS:')

# nome = 'Lucas Lima'
# idade  =  25
# email_usuario = 'lucas@gmail.com'
# peso = 80.50
# altura =  1.90
# endereco = 'Rua 10, Jd X'
# graduacao = 'ADS'
# casado = False 

# # SAÍDA
# print(nome)
# print(idade)
# print(email_usuario)
# print(endereco)
# print(graduacao)
# print(peso)
# print(altura)
# print(casado)

# # ENTRADA

# nome_2 = input('digite seu nome: ')
# print(nome_2)

# numero1 =  float(input('digite seu peso: '))
# numero2 =  float(input('digite sua altura: '))
# numero3 =  int(input('Digite o ano: '))

# soma  =  numero1 + numero2
# print(soma)


# print('IMC')

# peso =  float(input('Digite seu peso: '))
# altura  =  float(input('Digite sua altura: '))
# imc  =  peso/altura**2
# print('IMC', imc)

# print('SINAIS DE CALCULO ARITMÉTICO')


# print(10+200) # soma
# print(10-200) # subtração
# print(10*200) # multiplicalçi
# print(10/200) # divisão
# print('modulo', 10%200) #módulo
# print(10**2) # potencia
# print(10//200.0) # divisão c/ 2 barras

# variáveis -  estruturas de dados 
# funções  - print() input() float() int()
# sinais aritmétivos 


# sinais lógicos

# print(10 == 200) # comparar
# print(10 > 200) # verifa se 1º numero é maior
# print(10<200) # verifa se 1º numero é menor
# print(10>=200) # maior ou iguael
# print(10<=200) # menor ou igual
# print(10 != 2) # diferente

# # atividade: 

# # Peça ao usuário dois números.

# n1  =  int(input('Digite um número: '))
# n2  =  int(input('Digite um número: '))


# # Mostre:
# # A soma, subtração, multiplicação e divisão.
# print(n1 + n2)
# print(n1 - n2)
# print(n1 * n2)
# print(n1 / n2)



# # 
# # Verifique:

# # Se os números são iguais.

# print(n1 == n2)

# # Se o primeiro número é maior que o segundo.

# print(n1 > n2)

# # Se pelo menos um dos números é maior que 10.

# print(n1 > 10)
# print(n2 > 10)


# Peça o valor de um produto e:
# produto =  float(input('Digite o valor do produto: '))

# Calcule um desconto de 10%.

# desconto = produto * 0.10

# # Mostre o valor final.

# valor_prod = produto - desconto
# print('Valor do produto R$', valor_prod)

# # Verifique se o valor final é maior que 100.

# print('Verifique se o valor final é maior que 100 - ', valor_prod > 100)

# # Verifique se o produto ficou barato (menor que 50).

# print('Verifique se o produto ficou barato (menor que 50) - ', valor_prod < 50)




print('Concatenação: JUNTAR ')

pi = 3.14
pi = 3.18
print('pi', pi)

x  =  10
nome  = 'Thiago'

print('-------------------------')
# estrutura composta 

lista_ = [] # mutavel 

listas =  [10,20,30,10,50]
#          0  1  2  3  4   
lista_texto = ['a','b','c','d']
#              0    1   2   3 
lista_mista = ['a', True, 5.8]
#               0    1     2 
lista_bolaeno = [True, False, True]
#                 0     1       2
lista_real = [4.,5.6,9.8, 100]
#             0   1   2    3

lista_vazia = []

# adicionar um  dado a lista

lista_vazia.append(100)
print(lista_vazia)
lista_vazia.remove(100)
print(lista_vazia)
lista_vazia.append(100)
lista_vazia.append(120)
lista_vazia.append(150)
lista_vazia.append(250)
lista_vazia.insert(2,500)
lista_vazia.pop()

print('contagem de 150: ', lista_vazia.count(150))

l = [1,2,3]
indice =  l.index(2)
l.pop(indice)

print(l)



