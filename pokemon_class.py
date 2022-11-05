import requests

url1 = 'https://pokeapi.co/api/v2/pokemon/'
# url2 = 'https://pokeapi.co/api/v2/ability/'
url3 = 'https://pokeapi.co/api/v2/generation/'
# Se arma la base de datos de pokemon para las consultas:

# Pokemons por generacion

# Se obtienen los version groups por generaciones
dic_version_generacion = {}
n = 1
response = requests.get(url3 + str(n))
# json = response.json()
# version_groups = json.get('version_groups',[])
# print(version_groups)
while response.status_code == 200:
    json = response.json()
    version_groups = json.get('version_groups',[])
    for v in version_groups:
        # print(v)
        dic_version_generacion[v['name']] = n

    n += 1
    response = requests.get(url3 + str(n))

class pokemons():
    n = 1

    def get_pokemon(self):
        response = requests.get(url1 + str(self.n))
        contador = 1
        flag = True

        while response.status_code == 200 and contador <= 20:
            self.get_name_abilities_urli(response)
            self.n += 1
            response = requests.get(url1 + str(self.n))

            contador += 1
            
        continuar = input("Desea continuar? [Y/N]: ").upper()
        while continuar not in ["Y","N"]:
            continuar = input("Desea continuar? [Y/N] (ingrese Y o N): ").upper()

        if continuar == 'Y':
            self.get_pokemon()
        else:
            print("END")
            # if contador == 20:
            #     continuar = input("Desea continuar? [Y/N]: ").upper()
            #     while continuar not in ["Y","N"]:
            #         continuar = input("Desea continuar? [Y/N] (ingrese Y o N): ").upper()
        # response = requests.get(url1 + str(n))
        # if response.status_code == 200 and self.n<=20:
        #     self.n = self.n + 1
        #     get_name_abilities_urli

        # else:
            # print("Ya se listaron todos los pokemon")
    
    def get_name_abilities_urli(self, response):
        # response = self.get_pokemon()
        json = response.json()
        # Se imprime el nombre del pokemon
        print(f"Pokemon: {json['name']}\n")

        # Abilities
        abilities = json.get('abilities',[])
        abilities_list = []
        if abilities:
            for ab in abilities:
                abilities_list.append(ab['ability']['name'])
        sprite = json['sprites']['front_default']
        # Se imprimen las habilidades
        print("Habilidades:\n")
        for i in abilities_list:
            print(i,"\n")
        # URL de la imagen
        print('URL de imagen:\n')
        print(json['sprites']['front_default'])

    def get_PokGeneration(self, response):
        # response = self.get_pokemon()
        # self.n -= 1 
        json = response.json()
        indices = json.get("game_indices",[])
        ind = indices[0]['version']['name']
        return dic_version_generacion[ind]
    
    def Menu(self):
        print("")
        pass



# gen = input("Eliga una generacion")

obj = pokemons()
obj.get_pokemon()
# while True:
#     try:
#         if obj.get_PokGeneration() == gen:
#             obj.get_name_abilities_urli()
#     except:
#         break


        # print(f"Pokemon: {json['name']}\n")
    
    # def get_abilities(self):
    #     response = self.get_pokemon()
    #     json = response.json()






# N = 0
# def get_pokemons(url = url1, N) -> None:
#     n = 1
#     # N = 0
#     response = requests.get(url1 + str(N + n))
#     while n <= 20 and response.status_code == 200:
#         if opcion1:
        
#         elif opcion2:



#         n += 1
#         N += 1
#         if n == 20:
#             next = input('¿Desea continuar listando? [Y/N]').lower()
#             while next not in ['y','n']:
#                 next = input('¿Desea continuar listando? [Y/N], ingrese una de las dos opciones').lower()
#             if next == 'y':
#                 get_pokemons(N = N-1)

#         response = requests.get(url1 + str(N))


# # def get_pokemons(url = url1, offset = 0) -> None:
# #     args = {'offset': offset} if offset else {}

# #     response = requests.get(url1, params = args)

# #     if response.status_code == 200:
# #         json = response.json()# Se recupera el json
# #         results = json.get('results', [])#

# #         if results:
# #             for pokemon in results:
# #                 # Nombre del pokemon
# #                 name = pokemon['name']
# #                 print(name)
        
# #         next = input('¿Desea continuar listando? [Y/N]').lower()
# #         while next not in ['y','n']:
# #             next = input('¿Desea continuar listando? [Y/N], ingrese una de las dos opciones').lower()
# #         if next == 'y':
# #             get_pokemons(offset = offset + 20)

# # get_pokemons()



# # print(dic_version_generacion)

# # Ahora se obtienen los pokemon por habilidades:
# # dic_ability_pokemons = {}
# # n = 1
# # response = requests.get(url2 + str(n))
# # # json = response.json()
# # # version_groups = json.get('version_groups',[])
# # # print(version_groups)
# # # while response.status_code == 200:
# # while response.status_code == 200:
# #     json = response.json()
# #     ability_name = json['name']
# #     pokemones = json.get('pokemon',[])
# #     lista_pokemon = []

# #     for pok in pokemones:
# #         lista_pokemon.append(pok['pokemon']['name'])

# #     dic_ability_pokemons[ability_name] = lista_pokemon

# #     n += 1
# #     response = requests.get(url2 + str(n))

# # Ahora se obtienen los pokemon por tipo:



# # dic_pokemon_version = {}
# # n = 1
# # response = requests.get(url1 + str(n))
# # while response.status_code == 200:
# #     json = response.json()
# #     version_group = json.get('version_group',[])
# #     pokemon_name = json.get('pokemon',[])
# #     dic_pokemon_version[pokemon_name['name']] = version_group['name']

# #     n += 1
# #     response = requests.get(url1 + str(n))

# # print(dic_pokemon_version[pokemon_name['name']])





# # def get_pokemons(url = url1, offset = 0) -> None:
# #     args = {'offset': offset} if offset else {}

# #     response = requests.get(url1, params = args)

# #     if response.status_code == 200:
# #         json = response.json()# Se recupera el json
# #         results = json.get('results', [])#

# #         if results:
# #             for pokemon in results:
# #                 # Nombre del pokemon
# #                 name = pokemon['name']
# #                 # Obtenemos el url de la imagen del pokemon
# #                 urlPokemon = url1 + name
# #                 response = requests.get(urlPokemon) # Se accede a la url del pokemon
# #                 json = response.json() # Se recupera el json
# #                 url_imagen = json['sprites']['fron_default']
# #                 # Obtenemos sus habilidades
# #                 response = requests.get(url+'1')
# #                 n = 0
# #                 while response.status_code == 200:
# #                     json = response.json()
# #                     res = json.get('results',[])
# #                     if res:
# #                         for ability in res:

# #                     n += 1
# #                     response = requests.get(url + str(n))




# #                 print(name)
        
# #         next = input('¿Desea continuar listando? [Y/N]').lower()
# #         while next not in ['y','n']:
# #             next = input('¿Desea continuar listando? [Y/N], ingrese una de las dos opciones').lower()
# #         if next == 'y':
# #             get_pokemons(offset = offset + 20)

# # get_pokemons()