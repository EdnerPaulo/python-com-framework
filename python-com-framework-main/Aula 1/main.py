print('hello word')



peso =  float(input('Digite seu peso: '))
altura  =  float(input('Digite sua altura: '))
imc  =  peso/altura**2
print('IMC', imc)


# 4 tipos de dados em python


# texto 


'texto'
"texto"


# reais -  dinheiro - peso - altura - 


10.6
5.9
21.0


# inteiros


5
10
5
2


# lógicos 


True 
False

print('SINAIS DE CALCULO ARITMÉTICO')



print(10+200) # soma
print(10-200) # subtração
print(10*200) # multiplicalçi
print(10/200) # divisão
print('modulo', 10%200) #módulo
print(10**2) # potencia
print(10//200.0) # divisão c/ 2 barras

# atividade: 


# Peça ao usuário dois números.


n1  =  int(input('Digite um número: '))
n2  =  int(input('Digite um número: '))



# Mostre:
# A soma, subtração, multiplicação e divisão.
print(n1 + n2)
print(n1 - n2)
print(n1 * n2)
print(n1 / n2)




# 
# Verifique:


# Se os números são iguais.


print(n1 == n2)


# Se o primeiro número é maior que o segundo.


print(n1 > n2)


# Se pelo menos um dos números é maior que 10.


print(n1 > 10)
print(n2 > 10)

# Peça o valor de um produto e:
produto =  float(input('Digite o valor do produto: '))


# Calcule um desconto de 10%.


desconto = produto * 0.10


# Mostre o valor final.


valor_prod = produto - desconto
print('Valor do produto R$', valor_prod)


# Verifique se o valor final é maior que 100.


print('Verifique se o valor final é maior que 100 - ', valor_prod > 100)


# Verifique se o produto ficou barato (menor que 50).


print('Verifique se o produto ficou barato (menor que 50) - ', valor_prod < 50)