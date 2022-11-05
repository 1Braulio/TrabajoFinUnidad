import requests

# url1 = 'https://pokeapi.co/api/v2/pokemon/'
# # url2 = 'https://pokeapi.co/api/v2/ability/'
# url3 = 'https://pokeapi.co/api/v2/generation/'
# # Se arma la base de datos de pokemon para las consultas:
url_shape = 'https://pokeapi.co/api/v2/pokemon-shape/'
url_type = 'https://pokeapi.co/api/v2/type/'
url_ability = 'https://pokeapi.co/api/v2/ability/'
url_generation = 'https://pokeapi.co/api/v2/generation/'
url_habitat = 'https://pokeapi.co/api/v2/pokemon-habitat/'


def shape():
    response = requests.get(url_shape)
    json = response.json()
    results = json.get("results")
    dic_shape = {}

    for shape in results:
        url = url_shape + shape['name']
        response_1 = requests.get(url)
        json = response_1.json()
        dic_shape[shape['name']] = []

        for ps in json.get('pokemon_species'):
            dic_shape[shape['name']].append(ps['name'])

    return dic_shape


def typ():
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

def ability():
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

def gen():
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
