banco = {
   'clientes':{
       'a':{
       'conta' : 123,
       'saldo': 50000,
       'extrato':[100,-250],
       }
   }
}


conta = int(input('Digite o numero da conta: '))

if conta == banco['clientes']['a']['conta']:
    print('Acesso liberado')
    op =input (f'''

         escolha a operação da conta: {banco['clientes']['a']['conta']}

          1 - sacar
          2 - depositar
          3 - extrato
                  


         ''')
    

    if op == '1':
        saque  = float(input('Saque R$: '))
        s = banco['clientes']['a']['saldo'] - saque
        banco['clientes']['a']['extrato'].append(saque)
        print('Valor de saque R$', saque)
        banco['clientes']['a']['saldo'] = s
        print('Saldo R$', banco['clientes']['a']['saldo'])        
    elif op == '2':
        deposito  = float(input('Saque R$: '))
        s = banco['clientes']['a']['saldo'] + deposito
        banco['clientes']['a']['extrato'].append(deposito)
        print('Valor de deposito R$', deposito)
        banco['clientes']['a']['saldo'] = s
        print('R$', banco['clientes']['a']['saldo']) 
    elif op =='3':
        print('EXTRATO')
        print('R$', banco['clientes']['a']['extrato']) 
    else:
        print('Digite algo válido ... ')               


# Crie um programa que leia a nota de um aluno (0 a 10) e exiba a menção correspondente:


# - `"Excelente"` se nota >= 9
# - `"Bom"` se nota >= 7 e < 9
# - `"Regular"` se nota >= 5 e < 7
# - `"Insuficiente"` se nota < 5



nota =  float(input('nota >>>'))


if nota >= 9:
    print('EXCELENTE')
elif nota >=7 and nota <9:
    print('Bom')
elif nota >= 5 and  nota < 7:
    print('Regular')
else:
    print('insuficiente')    