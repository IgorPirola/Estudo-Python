texto1 = input("Digite uma palavra: ")
texto2 = input("Digite outra: ")

texto1 = texto1.lower()
texto2 = texto2.lower()
def verifica():
    if texto1 == '' or texto1.isspace() or texto2 == '' or texto2.isspace():
        print("Não são anagramas")
        return
    else:
        texto1.replace(' ', '')
        texto2.replace(' ', '')
        
        if len(texto1) != len(texto2):
            print("Não são anagramas")
        else:
            for ch in texto1:
                if ch not in texto2:
                    print("Não são anagramas1")
                    return
            for ch in texto2:
                if ch not in texto1:
                    print("Não são anagramas2")
                    return
    print("São anagramas")

verifica()