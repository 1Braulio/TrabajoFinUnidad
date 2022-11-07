import pokemon_class as pkc

def opciones():
    print("Eliga una opcion:\n",
        "1.- Listar pokemon por generacion\n",
        "2.- Listar pokemon por forma\n",
        "3.- Listar pokemon por habilidad\n",
        "4.- Listar pokemon por habitat\n",
        "5.- Listar pokemon por tipo\n")
def Menu():
    #print("Eliga una opcion:\n", "op1\n", "op2\n", "op3\n", "op4\n", "op5\n")
    opciones()
    opcion =  input('Eliga una opcion: ')
    while opcion not in ['1','2','3','4','5']:
        opciones()
        opcion =  input('Eliga una opcion (1, 2, 3, 4 o 5): ')

    if opcion == '1':
        d = pkc.gen()
        pkc.get_pokemons(d)
    elif opcion == '2':
        d = pkc.shape()
        pkc.get_pokemons(d)
    elif opcion == '3':
        d = pkc.ability()
        pkc.get_pokemons(d)
    elif opcion == '4':
        d = pkc.hab()
        pkc.get_pokemons(d)
    else:
        d = pkc.typ()
        pkc.get_pokemons(d)

Menu()