# O Desafio da Excelência (Prática)
# Para consolidar as aulas 1 a 6, não faça apenas um código simples. Vamos aplicar a lógica de desenvolvimento de software profissional.

# O Problema: Você precisa criar um sistema que ajude um pequeno empreendedor a calcular o lucro de um produto.

# O sistema deve pedir o nome do produto.
produto = input("Qual o nome do produto que você quer: ")
# Deve pedir o custo de fabricação (float).
custo = float(input("qual o custo de fabrica do produto: "))
# Deve pedir a porcentagem de lucro desejada (ex: 30 para 30%).
lucro = float(input("Qual o sua porcentagem de lucro"))
# O sistema deve calcular o preço de venda final.
venda_final = custo * lucro
# No final, exiba uma mensagem elegante usando F-Strings (como no exemplo acima).
print(f"o valor de venda final de cada produto é de {venda_final}")