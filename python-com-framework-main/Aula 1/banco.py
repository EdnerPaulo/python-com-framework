# Cria uma lista com o saldo inicial (R$ 1500)
saldo = [1500.0]

# Lista para guardar o histórico de transações (extrato)
extrato = []

# Adiciona o saldo inicial no extrato
extrato.append(sum(saldo))
# sum(lista) → soma tudo da lista

# Pede ao usuário o valor do saque
saque = float(input('Digite o saque: '))

# Calcula o novo saldo após o saque
transacao = sum(saldo) - saque

# Adiciona o valor do saque no extrato
extrato.append(saque)

# Atualiza o saldo com o novo valor após o saque
saldo = [transacao]

# Mostra o saldo atual
print('Saldo R$', saldo)

# Pede ao usuário o valor do depósito
deposito = float(input('Digite o Deposito R$: '))

# Adiciona o valor do depósito no extrato
extrato.append(deposito)

# Calcula o novo saldo após o depósito
transacao = sum(saldo) + deposito

# Atualiza o saldo com o novo valor após o depósito
saldo = [transacao]

# Mostra o saldo atualizado
print('Saldo R$', saldo)

# Mostra todo o histórico de transações (extrato)
print(extrato)