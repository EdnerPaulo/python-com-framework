# 1. Verificação de maioridade e permissão
# Enunciado:
# Crie um programa que leia a idade do usuário e se ele possui autorização dos pais (responda True ou False).
# O usuário pode participar da atividade se tiver 18 anos ou mais ou tiver autorização dos pais.
# Use and / or para verificar e exiba "Pode participar" ou "Não pode participar".
idade = int(input('Qual a sua Idade: '))
autorizacao = input('Voce tem permição dos seus pais: (Pode ou Não pode)')

pode = (idade >= 18 and autorizacao == 'Pode') 
msg = pode and "Pode" or "Não pode"

print(msg)

idade  = int(input('Idade: '))
autorizacao = bool(input('Possui autorização?>>>  '))
pode  =  idade >= 18 and autorizacao == True


msg =  pode and "Pode participar" or "Não pode participar"
print(msg)


# 2. Classificação de peso ideal
# Enunciado:
# Leia o peso (kg) e a altura (m) de uma pessoa. Calcule o IMC (peso / altura**2).
# Uma pessoa está com peso normal se o IMC estiver entre 18.5 e 24.9 (inclusive).
# Use operadores lógicos para verificar se o IMC está nessa faixa e exiba "Peso normal" ou "Fora da faixa".
# peso = float(input('Qual o seu peso '))
# altura = float(input('Qual a sua altura '))

# imc = (peso / altura**2)

# normal = (imc >=18.5 and imc <= 24.9)
# print(f"{imc:.2f}")
# # print(normal)
# mensagem = {
#     True : "Peso normal", 
#     False: "Fora da faixa"
#     }
# print(mensagem[normal])

# 3. Acesso ao sistema
# Enunciado:
# Leia o nome de usuário e a senha. O acesso é permitido apenas se o usuário for "admin" e a senha for "1234".
# Use and para verificar as duas condições e exiba "Acesso liberado" ou "Acesso negado".

# usuario = input("Digite o seu Usuario ")
# senha = int(input("Digite sua senha "))

# user = "admin"
# password =  1234

# autenticação = (usuario == user and senha == password)

# msg1 = autenticação and "Acesso liberado" or " Acesso negado"

# print(msg1)


# 4. Compra com desconto
# Enunciado:
# Leia o valor da compra e se o cliente é VIP (True ou False).
# O cliente ganha 10% de desconto se o valor for maior que R$ 100 ou ele for VIP.
# Exiba o valor final com desconto (se aplicável) ou o valor original.

# valor = int(input('Qual o valor da sua compra: '))
# vip = input('Você é cliente vip (Sim ou Não) ')

# desconto = valor > 100 or vip == 'Sim'
# desconto1 = valor - (0.10 * valor )
# msg2 = desconto and "Aplicavel" or "Valor original"
# print(msg2)
# msg3 = desconto and desconto1 or valor
# print(msg3)


# 5. Elegibilidade para doação de sangue
# Enunciado:
# Leia a idade e o peso.
# Para doar sangue, a pessoa deve ter entre 16 e 69 anos (inclusive) e pesar pelo menos 50 kg.
# Use and para verificar ambos os critérios e informe se a pessoa pode doar.
# idade_1 = int(input('Qual a sua idade: '))
# peso_1 = float(input('Qual o seu peso: '))

# doador = idade_1 > 16 and idade_1 < 69 and peso_1 > 50

# doar = doador and "Pessoa pode doar" or "Não pode doar"

# # doar = {
# #     True: "Pessoa pode doar",
# #     False: "Não pode doar"
# #     }

# # print(doar[doador])

# print(doar)

# 6. Validação de horário de funcionamento
# Enunciado:
# Uma loja funciona de segunda a sexta, das 9h às 18h.
# Leia o dia da semana (1=segunda, 7=domingo) e a hora (0 a 23).
# Determine se a loja está aberta.
# Dica: use and para combinar dia útil com horário, e or se quiser tratar sábado/domingo como fechado.
# semana = {
#     1:'Segunda',
#     2:'Terça',
#     3:'Quarta',
#     4:'Quinta',
#     5:'Sexta'
# }
# final_de_semana = ('Sabado','Domingo')

# horario_comercial= {
#     9: 'nove da manha',
#     10: 'dez da manha',
#     11: 'onze da manha',
#     12: 'meio dia',
#     13: 'uma da tarde',
#     14: 'duas da tarde',
#     15: 'três da tarde',
#     16: 'quatro da tarde',
#     17: 'cinco da tarde',
#     18: 'seis da tarde'
# }
# horarios= {
#     00: 'meia noite',
#     1: 'uma da manha',
#     2: 'duas da manha',
#     3: 'três da manha',
#     4: 'quatro da manha',
#     5: 'cinco a manha',
#     6: 'seis da manha',
#     7: 'sete da manha',
#     8: 'oito da manha',
#     19: 'sete da noite',
#     20: 'oito da noite',
#     21: 'nove da noite',
#     22: 'dez da noite',
#     23: 'onze da noite'

# }
# print('Escolha um dias da semana', semana)
# dia = int(input("Pelo numero: "))

# print('Qual o horario da sua visita',horario_comercial)
# hora = int(input('Digite que horas ira aparecer: '))
# funcionando  = dia in semana and hora in horario_comercial
# aberto = funcionando == True and "A loja está aberta" or ' Estamos fechado'
# final = aberto == "A loja está aberta" and "Dia de semana" or final_de_semana 
# print(final)
# print(aberto)
# print(semana[dia])
# print (horario_comercial[hora])


# 7. Aprovação em duas disciplinas
# Enunciado:
# Leia as notas de Matemática e Português.
# O aluno é aprovado se ambas as notas forem maiores ou iguais a 6.
# Use and para verificar e exiba "Aprovado" ou "Reprovado".

# nota_m = float(input("Qual foi sua nota em Matematica: "))
# nota_p = float(input("Qual foi sua nota em Portugues: "))

# aluno = nota_m >= 6 and nota_p >= 6
# media = aluno == True and "Aprovado" or "Reprovado"
# print(f"O Aluno teve a nota {nota_m} em Matematica  e {nota_p} em Portugues sendo {media}")





# 8. Identificação de ano bissexto
# Enunciado:
# Um ano é bissexto se for divisível por 4, mas não por 100, a menos que também seja divisível por 400.
# Leia um ano e use and e or para determinar se ele é bissexto.
# Exiba "Ano bissexto" ou "Ano não bissexto".
# ano = int(input('Qual o ano você quer saber: '))

# bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

# mensg = bissexto == True and "Ano bissexto" or "Ano não bissexto" 
# # print(bissexto)
# print(mensg)

# 9. Faixa etária
# Enunciado:
# Leia a idade e classifique:
# "Criança" se idade < 12
# "Adolescente" se 12 ≤ idade ≤ 17
# "Adulto" se idade ≥ 18
# Use and e or para definir os intervalos e exiba a classificação.
# anos = ["Criança"]* 12 +["Adolescente"] * 6 + ["Adulto"]
# # dentro desta lista do 1 ao 12 e multiplicado e 12 ao 17 tmb so adulto que o min e 18 tranfomando qualquer numero acima em 18
# idade1 = int(input("Qual a sua idade: "))
# idade1 = min(idade1, 18)
# # age = idade1 < 12 or idade1 >= 12 and idade1 <=17 or idade1 > 17
# # esta linha so me entrega boleanno nao string
# print(anos[idade1])


# 10. Sistema de alerta de temperatura e umidade
# Enunciado:
# Leia a temperatura (°C) e a umidade (%).
# Dispare um alerta se temperatura > 35 ou umidade > 70.
# Caso contrário, exiba "Condições normais".
# Use or para combinar as condições.
# print('Digite a temperatura (°C) e a umidade (%). ')
# temp= float(input())
# umidade = float(input())
# clima = temp > 35 and umidade > 70
# alerta = clima == True and "Alerta de perigo" or "Condições normais"
# print(alerta)
