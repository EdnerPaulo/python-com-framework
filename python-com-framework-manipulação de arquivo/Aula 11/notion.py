### **Modos de abertura**

# - `'r'` – leitura (padrão). O arquivo deve existir.
# - `'w'` – escrita. Cria um novo arquivo ou sobrescreve se já existir.
# - `'a'` – adição (append). Adiciona ao final do arquivo.
# - `'x'` – criação exclusiva. Falha se o arquivo já existir.
# - `'r+'` – leitura e escrita (posiciona no início).
# - `'b'` – modo binário (ex: `'rb'`, `'wb'` para imagens, executáveis).

# ---

### **Exemplos práticos**

### **1. Escrever em um arquivo (modo `'w'`)**

# Abre o arquivo para escrita (cria/substitui)
arquivo = open("dados.txt", "w")
arquivo.write("Linha 1\n")
arquivo.write("Linha 2\n")
arquivo.close()

### **2. Adicionar ao final (modo `'a'`)**

arquivo = open("dados.txt", "a")
arquivo.write("Linha 3\n")
arquivo.close()

### **3. Ler todo o conteúdo ´a´**

arquivo = open("dados.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

### **4. Ler linha por linha com   readline**

arquivo = open("dados.txt", "r")
linha = arquivo.readline()
while linha:
    print(linha.strip())  # strip remove a quebra de linha
    linha = arquivo.readline()
arquivo.close()

### **5. Ler todas as linhas com `readlines()`**

arquivo = open("dados.txt", "r")
linhas = arquivo.readlines()
for l in linhas:
    print(l.strip())
arquivo.close()

### **6. Usando `with`**

# O arquivo é fechado automaticamente ao sair do bloco
with open("dados.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())