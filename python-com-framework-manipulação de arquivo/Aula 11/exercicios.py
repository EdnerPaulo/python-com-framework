# 1. **Criar e escrever**
    
#     Crie um programa que peça ao usuário um nome e uma idade, e grave essas informações em um arquivo chamado `cadastro.txt`, uma pessoa por linha no formato `"nome,idade"`. O programa deve permitir adicionar várias pessoas até que o usuário digite `"sair"`.

def escrever_mostrar():
    c = input('Deseja cadastra? sim ou sair: ')
    quant =  int(input("quantas pessoas: "))
    while c == 'sim':
        for  n in range(quant):
            nome =  input('nome: ')
            idade =  int(input('Idade:  '))
            arquivo = open("cadastro.txt", "a")
            arquivo.write(f"Nome - {nome}, Idade - {idade}\n")
        c = input('Deseja cadastra? sim ou sair: ')

    else:
        arquivo.close()
        print('Saiu...')
escrever_mostrar()

# 2. **Ler e exibir**
    
#     Escreva um programa que leia o arquivo `cadastro.txt` criado no exercício anterior e exiba na tela cada pessoa no formato `"Nome: [nome], Idade: [idade]"`.

arquivo = open("cadastro.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close() 

# 3. **Contar linhas**
    
#     Crie uma função `contar_linhas(nome_arquivo)` que retorna o número de linhas do arquivo. Teste com o arquivo `cadastro.txt`.

def contar():


    nome =  input('Nome do arquivo: ')
    palavra  =  input('palavra: ')


    c  =  0
    linhas  = open(nome, 'r')


    for linha in linhas:
        # print(linha)
        linha = linha.lower()
        c  =  c + linha.count(palavra.lower())
    linhas.close()
    print(c) 


contar()       
    
    
# 4. **Procurar palavra**
    
#     Peça ao usuário uma palavra e um nome de arquivo. Conte quantas vezes essa palavra aparece no arquivo (ignorando maiúsculas/minúsculas). Exiba o resultado.
    
def ler_l():
    arquivo = open("teste.txt", "r")
    linhas = arquivo.readlines()
    print(len(linhas))
    # arquivo.close()


ler_l()     

     
#   
# 5. **Copiar arquivo**
    
#     Peça ao usuário o nome de um arquivo de origem e um arquivo de destino. Copie o conteúdo do arquivo de origem para o destino, mantendo as linhas.

def leitura(o, d):
    
   
    
    origem = open(o, 'w')
    origem.write('teste 1\n')
    origem.write('teste 2\n')
    origem.close()
    
    with open(o, 'r') as c :
        conteudo = c.read() 


        
        destino = open(d, 'w')
        destino.write(conteudo)
        destino.close()
  
    
    
     


o = input('Origem:')
d = input('destino:')


leitura(o,d)

