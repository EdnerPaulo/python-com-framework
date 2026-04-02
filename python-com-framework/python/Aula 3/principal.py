# Mostre:
# Saldo atual
# Lista de transações
# Peça:
# Valor da operação (positivo depósito, negativo saque)
# Calcule:
# Novo saldo
# Peça:
# Valor da operação (positivo depósito, negativo saque)
# Calcule:
# Novo saldo
# Parte 3: Regras do Banco
# Aplique regras usando apenas lógica:
# Se saldo final < 0 - cobrar taxa de 20
# Se depósito > 500 - bônus de 10
# Se saque maior que saldo - taxa extra de 15
# Sem if
banco = {
    "Joao": {
        "saldo": 1500,
        "transacoes": [200, -100, 50]
    },
    "Maria": {
        "saldo": 800,
        "transacoes": [-200, -50, 300]
    },
    "Carlos": {
        "saldo": 1200,
        "transacoes": [500, -300, -100]
    }
}
# ---------------------------------
nome = input('Digite no nome do dono da conta(Joao,Maria,Carlos)')
conta = banco[nome]["saldo"]
print(f'O saldo na conta de {nome} é de {conta}')
transacoes = banco[nome]["transacoes"]
print(f'As transações que voce pode fazer {transacoes}')
valor_da_operação = int(input(f'{transacoes}'))
print(valor_da_operação)
acao = valor_da_operação in banco[nome]["transacoes"]
# print(acao)



# print(banco)