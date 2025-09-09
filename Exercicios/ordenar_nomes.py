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

def ordenar_nomes(n_list) :
    ordered_list = n_list.copy()
    c = 0
    inc_name = 0
    inc_lett = 0

    while c < 1000:
        name1 = ordered_list[inc_name]
        name2 = ordered_list[inc_name+1]

        print("\n",ordered_list)
        print(name1)
        print(name2)

        if ord(name1[inc_lett]) != 32 and ord(name2[inc_lett]) == 32:
            ordered_list.remove(name2)
            ordered_list.append(name2)
            inc_lett = 0
        if ord(name1[inc_lett]) > ord(name2[inc_lett]) :
            ordered_list.remove(name2)
            ordered_list.append(name2)
            inc_lett = 0
        elif ord(name1[inc_lett]) < ord(name2[inc_lett]) :
            ordered_list.remove(name1)
            ordered_list.append(name1)
            inc_lett = 0
        elif ord(name1[inc_lett]) == ord(name2[inc_lett]) :
            inc_lett += 1
        else: 
            inc_lett += 1

        c+=1



ordenar_nomes(nomes)