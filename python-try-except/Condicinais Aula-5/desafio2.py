# Contexto:
# Uma indústria monitora temperatura (T), umidade (U) e presença de gás inflamável (G, 0 ou 1).
# O nível de risco é dado por:

# Crítico: (T > 40 ou U > 80) e G == 1

# Alto: (T > 40 ou U > 80) e G == 0

# Médio: (T entre 25 e 40) e (U entre 50 e 80)

# Baixo: qualquer outra situação

# Tarefa:
# Receba T (float), U (float), G (0 ou 1).
T = float(input('Qual a temperatura'))
U = float(input('Quanto tem de umidade'))
G = float(input('A presença de gás inflamavel (1 para sim , 0 para não )'))
# Classifique o risco em "Crítico", "Alto", "Médio" ou "Baixo" sem usar if/elif.
critico = (T > 40 or U > 80) and G == 1
alto = (T > 40 or U > 80) and G == 0
medio= (T > 25 and T < 40) and (U > 50 and U < 80)

classificacao = critico == True and "Crítico" or alto == True and "Alto" or medio == True and "Médio" or "Baixo"

print(classificacao)

# Use apenas dicionários com chaves booleanas e operadores lógico

# UTILIZE APENAS SINAIS LÓGICOS -  VARIAVEIS  -  LISTAS  -  I/O -  NÃO UTILIZE CONDICIONAIS OU LOOPS