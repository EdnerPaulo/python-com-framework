# # def teste():
# #     print('teste')


# # print('teste2')
# # teste()



# # variáveis global


a = 'teste 1'
def x():
    a = 'teste 2'
    print(a)
x()
print(a)    


# # variáveis locais 


# def y():
#     nome = 'Paulo'
#     idade = 12
#     print(nome, idade)


# y()


# # globais
# nome = 'teste'
# def z():
#     global nome, idade, endereco
    
#     nome = 'Marcos'
#     idade  =  25
#     endereco = 'rua 10'



# # z()


# print(nome)
# # print(idade)
# # print(endereco)


def x(a=5,b=0,c =5):
    print(a+b)


x(10,200)
x(110,20)
x() 