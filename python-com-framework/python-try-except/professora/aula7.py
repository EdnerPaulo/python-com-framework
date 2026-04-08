try:
    x  =  int(input('>>>'))


    print(10 + x)
    l = [1,2,3,5]
    y  = l[x]
    print(y)
    
except NameError as erro:
    print(erro)
except ValueError as erro:
    print(erro)
except TypeError as erro:
    print(erro) 
except IndexError as erro:   
    print(erro)     
    
else:
    print('ocorreu um não identificado ou não houve erro')
   
finally:
    print('fim  decarregamento...')