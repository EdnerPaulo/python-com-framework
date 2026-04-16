def escrever_mostrar():
    c = input('Deseja cadastra? sim ou sair: ')
    while c == 'sim':
        nome =  input('nome: ')
        idade =  int(input('Idade:  '))
        arquivo = open("cadastro.txt", "a")
        arquivo.write(f"nome - {nome} idade - {idade}\n")
        nome2 =  input('nome: ')
        idade2 =  int(input('Idade:  '))
        arquivo.write(f"nome - {nome2} idade - {idade2}\n")
        c = input('Deseja cadastra? sim ou sair')
       
    else:
        arquivo.close()
        print('Saiu...')
escrever_mostrar()

arquivo = open("cadastro.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()



