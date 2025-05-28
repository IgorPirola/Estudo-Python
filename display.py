def display(lista):
    a5 = {'0':"###", '1':"  #", '2':"###", '3':"###", '4':"# #", '5':"###", '6':"###", '7':"###", '8':"###", '9':"###"} 
    a4 = {'0':"# #", '1':"  #", '2':"  #", '3':"  #", '4':"# #", '5':"#  ", '6':"#  ", '7':"  #", '8':"# #", '9':"# #"} 
    a3 = {'0':"# #", '1':"  #", '2':"###", '3':"###", '4':"###", '5':"###", '6':"###", '7':"  #", '8':"###", '9':"###"}  
    a2 = {'0':"# #", '1':"  #", '2':"#  ", '3':"  #", '4':"  #", '5':"  #", '6':"# #", '7':"  #", '8':"# #", '9':"  #"}  
    a1 = {'0':"###", '1':"  #", '2':"###", '3':"###", '4':"  #", '5':"###", '6':"###", '7':"  #", '8':"###", '9':"###"} 
    for i in lista:
        print(a5[i], end=' ')
    print("")
    for i in lista:
        print(a4[i], end=' ')
    print("")
    for i in lista:
        print(a3[i], end=' ')
    print("")
    for i in lista:
        print(a2[i], end=' ')
    print("")
    for i in lista:
        print(a1[i], end=' ')

def main():
    num = input("Digite um numero inteiro maior ou igual a 0: ")
    while True:
        if not num.isdigit():
            print("Entrada inválida")
            num = input("Digite um numero inteiro maior ou igual a 0: ")
            continue
        elif int(num) < 0:
            print("Entrada inválida")
            num = input("Digite um numero inteiro maior ou igual a 0: ")
            continue
        else:
            break
    lista = []
    for i in num:
        lista += i
    display(lista)

main()