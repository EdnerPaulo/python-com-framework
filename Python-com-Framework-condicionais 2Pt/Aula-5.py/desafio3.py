
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
val = validador == True and "Você tem direito a se tornar VIP" or "Volte sempre"
print(val)
