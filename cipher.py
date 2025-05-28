def cifra(texto, cifra):
    cripto = ""
    for char in texto:
        if char.isalpha():
            code = ord(char) + cifra
            if char.isupper():
                if code > ord('Z'):
                    code = code - ord('Z') + ord('A') - 1
            if char.islower():
                if code > ord('z'):
                    code = code - ord('z') + ord('a') - 1
        else:
            code = ord(char)
        cripto += chr(code)
    return cripto


def main():
    texto = input("Digite a frase: ")

    inter = input("Intervalo 1-25: ")
    while True:
        if not inter.isdigit:
            inter = input("Intervalo invalido, digite novamente: ")
        elif int(inter) <= 0 or int(inter) > 25:
            inter = input("Intervalo invalido, digite novamente: ")
        else:
            break
    
    print(cifra(texto, int(inter)))
        
main()
