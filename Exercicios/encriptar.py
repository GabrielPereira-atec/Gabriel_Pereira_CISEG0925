frase = str()
frase_enc = str()
chave = str()

def encripta(col, ch):
    new_phr = []
    key = 0

    for i in ch :

        if key+ord(i) > 255 :
            key = 32

        key += ord(i)

    for j in col :
        new_phr.append(ord(j)+key)

    return new_phr

def desencripta(enc, ch):
    key = 0

    for i in ch :

        if key+ord(i) > 255 :
            key = 32

        key += ord(i)

    print("\n")
    for j in range(len(enc)) :
        print(chr(enc[j]-key), end="")


def toChar(phr, chave) :
    key = int()

    for i in chave:

        if key+ord(i) > 255:
            key = 32

        key += ord(i)

    for j in range(len(phr)) :
        print((chr(phr[j])), end="")

frase = input("Digite sua frase: ")
chave = input("Defina a chave da encriptação: ")

frase_enc = encripta(frase, chave)

print("Frase encriptada em ascii: ",frase_enc)

print("Frase encriptada: ")
toChar(frase_enc, chave)

desencripta(frase_enc, chave)