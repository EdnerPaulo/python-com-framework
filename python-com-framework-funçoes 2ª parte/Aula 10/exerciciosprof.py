# def cpf2():


#     cpf  =  input('CPF: ')
#     soma  = 0


#     for i in range(9):
#         soma += int(cpf[i]) * (10 - i)
    
#     nu1 = soma * 10
#     x1 = nu1 % 11
#     if x1 == 10:
#         x1 = 0
#     print(x1)



#     soma = 0
#     for i in range(10):
#         soma += int(cpf[i]) * (11 - i)


#     nu2 = soma * 10
#     x2 = nu2 % 11
#     if x2  == 10:
#         x2  = 0
#     print(x2)
   
   
    
#     if x1 ==  int(cpf[-2] and x2 ==  int(cpf[-1])):
#         print(True)
#     else:
#         print(False)    


# cpf2()




# tabuada 


# def tabuada(numero, inicio=1, fim=10):
#     for x in range(inicio,fim):
#         c  = x * numero
#         print( c)
     


# def mostrar():
#     tabuada(5,0,11)


# mostrar()    



#


# def contar_palavras(palavras_texto):
#     palavra = palavras_texto.split()
#     d =  {}
#     for i in palavra:
#         if i in d:
#             d[i] += 1
#         else:
#             d[i] = 1    
        
#     print(d)


# contar_palavras('olá olá bom dia')    

def ordenar_lista(lista):
    x = 0
    for i in range(len(lista)):
        for j in range(len(lista) - 1):
            if lista[i] > lista[j]:
                x  = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = x
            # else:
            #     lista[j] = x 
            #     lista[j+1] =  lista[j]
            #     x = lista[j+1] 


        print(lista)        


ordenar_lista([10,15,61,2,1,35])