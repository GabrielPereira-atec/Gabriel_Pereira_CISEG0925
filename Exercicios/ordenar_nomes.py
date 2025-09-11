nomes = [
    "Gabriel Pereira",
    "Anna Beatriz",
    "Carlos Figueiras",
    "Ana Carla",
    "Eduardo Paiva",
    "Fabio Barrento",
    "Ana Clara",
    "João Albuquerque",
    "Tiago Leão",
    "Mateus Lira"
]

def compara_nomes(name1, name2) :
    for cont1, cont2 in zip(name1, name2):
        if ord(cont1) < ord(cont2) :
            return True
        elif ord(cont1) > ord(cont2) :
            return False
    return len(name1) <= len(name2)

def ordenar_lista(n_list) :
    n = len(n_list)

    for inc in range(n):
        for inc2 in range(0, n - inc - 1) :
            if not compara_nomes(n_list[inc2], n_list[inc2+1]) :
                n_list[inc2], n_list[inc2+1] = n_list[inc2+1], n_list[inc2]

    return n_list

print(ordenar_lista(nomes))