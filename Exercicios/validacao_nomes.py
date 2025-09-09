nome = str()

def name_valid(name) :
    #Tenta dividir o nome em duas variaveis (primeiro_nome e ultimo_nome) utilizando o espaço para verificar se há dois nomes. Caso não tenha dois nomes, responde que o nome é invalido e termina o programa
    try:
        full_name = name.split(" ", 2)
        first_name = full_name[0]
        last_name = full_name[1]
        check_cases = first_name[1:] + last_name[1:]
    except IndexError:
        print("\bNome Inválido!\nSem a presença de um espaço, último nome ou primeiro nome!!!")
        return 0

    #Verificação da primeira letra do primeiro nome, se for minuscula para o programa e diz que é invalido
    try:
        if first_name[0].islower() :
            print("Nome Inválido!\nPrimeira letra do -primero nome- não pode ser MINUSCULA!!!")
            return 0
        elif ord(first_name[0]) < 65 or ord(first_name[0]) > 91:
            print("Nome Inválido!\nPrimeira letra do -primero nome- deve ser uma letra!!!")
            return 0

    #Verificação da primeira letra do ultimo nome, se for minuscula para o programa e diz que é invalido
        if last_name[0].islower() :
            print("Nome Inválido!\nPrimeira letra do -último nome- não pode ser MINUSCULA!!!")
            return 0
        elif ord(last_name[0]) < 65 or ord(last_name[0]) > 91:
            print("Nome Inválido!\nPrimeira letra do -último nome- deve ser uma letra!!!")
            return 0
    except:
        print("\bNome Inválido!\nSem a presença de um espaço, último nome ou primeiro nome!!!")
        return 0

    #Verificação das letras do nome com exceção da primeira, todas tem de ser minusculas, que é verificado pelo valor ASCII das letras. Caso a letra esteja fora do valor ASCII das letras minusculas o programa é parado depois de exibir a mensagem de nome invalido
    for lett_first in check_cases :
        if ord(lett_first) < 97 or ord(lett_first) > 122:
            print("Nome Inválido!\nCaractéres inválidos ou letras maiusculas no meio dos nomes!")
            return 0

    return print("NOME VÁLIDO!!!!!!")

print("Introduza o seu nome completo: ")
nome = str(input("r: "))

print("\nVerificando nome . . .  \n")

name_valid(nome)