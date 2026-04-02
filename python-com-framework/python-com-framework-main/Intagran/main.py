# import random


# print("Acerte o numero ")
# number = random.randint(1,6)
# guess = int(input("Digite um numero entre 1 e 6: "))

# if guess == number:
#     print(f"Você acertou {guess}")
# else:
#     print(f"Voce errou o numero era {number}")


# name = "Mouse"
# print (name[1:4])


# def balance(b):
#     if b < 100:
#         return "Low"
#     return "OK"
# print(balance(99))

x = 6
y = 6

# x = int(input("Digite o valor de x: "))
# y = int(input("Digite o valor de y: "))

if x > 5:
    if y == 5:
        print("C")
    elif y > 2:
        if x > y:
            print("A")
        else:
            print("B")
    else:
        if x - y == 5:
            print("D")
        else:
            print("E")
else:
    print("F")