### **1. Calculadora com Funções**

# Crie funções separadas para as quatro operações básicas (`somar`, `subtrair`, `multiplicar`, `dividir`). Em seguida, escreva um programa que leia dois números e a operação desejada (como string) e chame a função correspondente. A divisão deve tratar divisão por zero.

def soma(x,y):
    return x + y


def subtrair(x,y):
    return x - y


def multiplicar(x,y):
    return x * y


def dividir(x,y):
    try:
        return x / y
            
    except ZeroDivisionError as erro:
        return erro

# def operacoes():


#     op =  input(':>>>')
#     if op == '+':
#        s  =  str(soma(10,50))
#        print(s) 
#        print(type(s))
#     elif op == '-':
#        s  =  str(subtrair(10,50))
#        print(s) 
#        print(type(s))


#     elif op == '*':
#        s  =  str(multiplicar(10,50))
#        print(s) 
#        print(type(s))   
#     elif op == '/':
#        s  =  str(dividir(10,0))
#        print(s) 
#        print(type(s))   
#     else:
#         print('Digite algo válido')           
# operacoes()

def operacoes():


    op =  input(':>>>')
    x = int(input('>>>'))
    y = int(input('>>>'))
    if op == '+':
       s  =  str(soma(x,y))
       print(s) 
       print(type(s))
    elif op == '-':
       s  =  str(subtrair(x,y))
       print(s) 
       print(type(s))


    elif op == '*':
       s  =  str(multiplicar(x,y))
       print(s) 
       print(type(s))   
    elif op == '/':
       s  =  str(dividir(x,y))
       print(s) 
       print(type(s))   
    else:
        print('Digite algo válido')           
operacoes()