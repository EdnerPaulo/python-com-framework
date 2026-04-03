
# Uma loja oferece um cupom especial. O cliente ganha o cupom se atender a pelo menos  das seguintes condições:
# Se for VIP (responde "sim" ou "não")
# Valor da compra acima de R$ 200
# Primeira compra no mês (responder "sim" ou "nao")
# Além disso, o cupom  pode ser aplicado se o cliente tiver  no histórico (número inteiro).

# Tarefa Receba:
print("Você é nosso cliente vip")
# vip (string "sim" ou "nao")
vip= input('Sim ou Não: ')
print(vip)
# valor (float)
valor= float(input('Qual o valor da sua compra: '))
print(valor)
# primeira_compra (string "sim" ou "nao")
primeira = input('Esta é sua primeira compra do més: ')
print(primeira)
# Reclamações
reclamacao= input('Gostou do produto (Sim ou Não): ')
print(reclamacao)
# Determine se o cliente  ("Cupom liberado") ou  ("Sem cupom"),  (SEM IF , SEM LOOP, SEM FUNÇÃO)
cupom = vip == "Sim" and valor >200 and primeira == "Sim" 
validar= cupom == True and "Cupom liberado" or "Sem cupom"
print(validar)
validador = reclamacao == "Sim"
val = vip == "Sim" and validador == False and "Volte sempre" or "Você tem direito a se tornar VIP"
print(val)




# Uma loja oferece um cupom especial. O cliente ganha 
# o cupom se atender a pelo menos  das seguintes condições:
# Se for VIP (responde "sim" ou "não") vip:
# Valor da compra acima de R$ 200 valor_c?
# Primeira compra no mês (responder "sim" ou "nao") compra_mes
# Além disso, o cupom  pode ser aplicado se o cliente tiver  
# no histórico 


# loja = {


#     'clientes':
#         {
#             'junior':{
#                 'vip': 'sim',
#                 'compra':201.0,
#                 'primeira_compra':'sim',
#                 'reclamacao':False


#             },
#             'fernando':{
#                 'vip': 'não',
#                 'compra':500.0,
#                 'primeira_compra':'não',
#                 'reclamacao':True
#             }
#         }}



# nome = input('Nome: ')
# # vip = input('É cliente VIP? ')
# # valor_compra  =  float(input('Valor da compra R$ '))
# # primeira_compra  =  input('Primeira compra sim ou não: ')
# # reclamacao =  bool(input('Possui reclamação? '))


# verificar_vip  =   loja['clientes'][nome]['vip'] == 'sim'
# print(verificar_vip)
# verifica_valor  =  loja['clientes'][nome]['compra'] > 200
# print(verifica_valor)
# verificar_p_compr =  loja['clientes'][nome]['primeira_compra'] == 'sim'
# print(verificar_p_compr)
# recla = loja['clientes'][nome]['reclamacao']  == False
# print(recla)


# saida = verificar_vip and verifica_valor and verificar_p_compr and recla and "Cupom liberado" or 'sem cupom'


# print(saida)

