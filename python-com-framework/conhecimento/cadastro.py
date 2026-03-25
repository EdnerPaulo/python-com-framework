# Desafio 1: O Coletor de Dados (Aula 1 e 2)
# Crie um programa que pergunte o nome do usuário, a idade e a cidade onde mora. No final, exiba uma frase organizada: "Olá [Nome], você tem [Idade] anos e mora em [Cidade]."

nome = input('Digite o seu Nome: ')
idade = input('Digite a sua idade: ')
cidade = input('Digite a sua cidade: ')
input( f'Olá {nome} você tem {idade} anos e mora em {cidade}.')

# Desafio 2: Calculadora de Carga Horária (Aula 2 e 3)
# Baseado na sua imagem, cada aula tem 3h. Crie um programa onde o usuário digita quantas aulas ele já assistiu, e o sistema calcula o total de horas estudadas.
# Exemplo: 5 aulas assistidas = 15 horas.

quant = input('Quantas aulas você ja assistiu: ')
resul = int(quant) * 3
input (f'Você assistiu {quant} aulas , totalizando {resul} de horas estudadas')

# Desafio 3: Verificador de Paradigma (Aula 4)
# A aula 4 fala sobre "Paradigma Estrutural". Crie um código que peça uma nota de 0 a 10.
# Se a nota for maior ou igual a 6, imprima: "Aprovado".
# Se for menor, imprima: "Reprovado".
# (Isso exercita a estrutura de decisão if/else).

numero = float(input('Digite uma nota de 0 a 10: '))
if numero >=6 :
    print('Aprovado')
else :
    print('Reprovado')
    
# Desafio 4: O Garçom Digital (Aula 5 - Funções I/O)
# Crie um pequeno menu:
# Suco (R$ 5.00)
# Sanduíche (R$ 10.00)
# O usuário escolhe o número, e o programa imprime o valor total a pagar.
lista = [('suco', 5.00), ('sanduíche', 10.00)]

print (f'1 - Suco (R$ 5.00) , 2 - Sanduíche (R$ 10.00)')

opcao = float(input('Escolha sua opção; '))

if opcao == 1:
    print('Você gastou R$ 5,00 reais ')
elif opcao == 2:
    print('Você gastou R$ 10,00 reais ')
else:
    print('Você digitou errado')