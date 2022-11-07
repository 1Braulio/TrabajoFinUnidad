import requests

url_shape = 'https://pokeapi.co/api/v2/pokemon-shape/'
url_type = 'https://pokeapi.co/api/v2/type/'
url_ability = 'https://pokeapi.co/api/v2/ability/'
url_generation = 'https://pokeapi.co/api/v2/generation/'
url_habitat = 'https://pokeapi.co/api/v2/pokemon-habitat/'


def shape() -> dict: # Retorna un diccionario donde las llaves son formas y cada una lleva a una lista de pokemones correspondiente
    response = requests.get(url_shape)
    json = response.json()
    results = json.get("results")
    dic_shape = {}

    for shape in results: # loop sobre todas las formas (shape)
        url = url_shape + shape['name'] # se crea la url de la forma
        response_1 = requests.get(url)
        json = response_1.json()
        dic_shape[shape['name']] = [] # shape como llave a una lista de pokemones correspondiente

        for ps in json.get('pokemon_species'): # cada pokemon en la pagina de shape se agrega a la lista creada antes
            dic_shape[shape['name']].append(ps['name'])

    return dic_shape

# El mismo principio siguen las demas funciones pero para tipo, generacion, etc.

def typ() -> dict:# Retorna un diccionario donde las llaves son tipos (fuego, agua, etc.) y cada una lleva a una lista de pokemones correspondiente
    response = requests.get(url_type)
    json = response.json()
    results = json.get("results")
    dic_type = {}

    for typ in results:
        url = url_type + typ['name']
        response_1 = requests.get(url)
        json = response_1.json()
        dic_type[typ['name']] = []

        for pk in json.get('pokemon'):
            dic_type[typ['name']].append(pk['pokemon']['name'])

    return dic_type

def ability() -> dict: # Retorna un diccionario donde las llaves son habilidades y cada una lleva a una lista de pokemones correspondiente
    response = requests.get(url_ability)
    json = response.json()
    results = json.get("results")
    dic_ability = {}

    for ab in results:
        url = url_ability + ab['name']
        # print(url)
        response_1 = requests.get(url)
        json = response_1.json()
        dic_ability[ab['name']] = []

        for pk in json.get('pokemon'):
            dic_ability[ab['name']].append(pk['pokemon']['name'])
    
    return dic_ability

def gen() -> dict:
    response = requests.get(url_generation)
    json = response.json()
    results = json.get("results")
    dic_generation = {}

    for gen in results:
        url = url_generation + gen['name']
        # print(url)
        response_1 = requests.get(url)
        json = response_1.json()
        dic_generation[gen['name']] = []

        for pk in json.get('pokemon_species'):
            dic_generation[gen['name']].append(pk['name'])

    return dic_generation

def hab() -> dict:
    response = requests.get(url_habitat)
    json = response.json()
    results = json.get("results")
    dic_habitat = {}

    for hab in results:
        url = url_habitat + hab['name']
        # print(url)
        response_1 = requests.get(url)
        json = response_1.json()
        dic_habitat[hab['name']] = []

        for pk in json.get('pokemon_species'):
            dic_habitat[hab['name']].append(pk['name'])

    return dic_habitat

# La siguiente funcion imprime los pokemon (nombre, habilidades y url de imagen) de acuerdo al diccionario entregado
urlpok = 'https://pokeapi.co/api/v2/pokemon/'
def get_pokemons(d: dict) -> None:
    # Opcion para listar todos los pokemon de un solo criterio o de todos los criterios (el criterio es tipo, habilidad, generacion, etc.)
    listaKeys = list(d.keys())
    last_opcion = str(len(listaKeys)+1)

    # Display de menu para seleccionar criterio
    print("Eliga una opcion:\n")
    # En total hay criterios + 1 opciones (el 1 que se agrega es de la opcion de listar todos los pokemon para todos los criterios)
    def yield_key(listaKeys):
        cont = 1
        for yk in listaKeys:
            string = f"{cont}.- {yk}"
            cont += 1
            yield string

    for string in yield_key(listaKeys):
        print(string)
    opcion = input("o--> ")
    
    while opcion not in [str(n_opcion + 1) for n_opcion in range(len(listaKeys) + 1)]:
        print(f"Eliga una opcion válida (uno de los numeros de la lista):")
        for string in yield_key(listaKeys):
            print(string)
        opcion = input("o--> ")

    if opcion != last_opcion:
        key_criterio = listaKeys[int(opcion)-1] # int(opcion)-1 es el indice del criterio/llave en la lista
        print(f"    CRITERIO --> {key_criterio}")
        for pokm in d[key_criterio]:
            urlpok_pk = urlpok + pokm #url del pokemon para obtener los tres datos (nombre, habilidades y url de imagen)
            # try para manejar la excepcion de pokemons para los que la url no funcione (ocurre con deoxys)
            try:
                response = requests.get(urlpok_pk)
                json = response.json()
                abis = [] # lista que contiene todas sus habilidades
                for abi in json.get('abilities'): # se llena la lista de habilidades
                    abis.append(abi['ability']['name']) # se llena la lista de habilidades
                print(f"Nombre: {pokm} |-->| Habilidades: {abis} |-->| url: {json['species']['url']} ") # se imprime
            except:
                # cuando ocurre la excepcion no se puede obtener la url de su imagen entonces se reemplaza por NA
                abis = [abil for abil in d.keys() if pokm in d[abil]]
                print(f"Nombre: {pokm} |-->| Habilidades: {abis} |-->| url: NA")
            # json = response.json()
            # abis = []
            # for abi in json.get('abilities'):
            #     abis.append(abi['ability']['name'])
            # print(f"Nombre: {pokm} |-->| Habilidades: {abis} |-->| url: {json['species']['url']} ")
        print("\n")

    else:
        # Opcion de imprimir todos los pokemon por criterio (llave del diccionario)
        for key in d.keys():
            print(f"    CRITERIO --> {key}") # se indica el criterio
            # print("|<-.->|"+key+"|<-.->|"+"\n") # se indica el criterio
            # Se hace un loop para listar pokemones que corresponden al criterio
            for pokm in d[key]:
                urlpok_pk = urlpok + pokm #url del pokemon para obtener los tres datos (nombre, habilidades y url de imagen)
                # try para manejar la excepcion de pokemons para los que la url no funcione (ocurre con deoxys)
                try:
                    response = requests.get(urlpok_pk)
                    json = response.json()
                    abis = [] # lista que contiene todas sus habilidades
                    for abi in json.get('abilities'): # se llena la lista de habilidades
                        abis.append(abi['ability']['name']) # se llena la lista de habilidades
                    print(f"Nombre: {pokm} |-->| Habilidades: {abis} |-->| url: {json['species']['url']} ") # se imprime
                except:
                    # cuando ocurre la excepcion no se puede obtener la url de su imagen entonces se reemplaza por NA
                    abis = [abil for abil in d.keys() if pokm in d[abil]]
                    print(f"Nombre: {pokm} |-->| Habilidades: {abis} |-->| url: NA")
                # json = response.json()
                # abis = []
                # for abi in json.get('abilities'):
                #     abis.append(abi['ability']['name'])
                # print(f"Nombre: {pokm} |-->| Habilidades: {abis} |-->| url: {json['species']['url']} ")
            print("\n")


# Menu()