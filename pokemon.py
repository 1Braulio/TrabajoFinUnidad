#data frame para cumplir con la solicitud de listar

import requests as re
import pandas as pd

pokemon = pd.DataFrame(columns=["nombre","habilidad","url"])

def primera_generacion():
    for i in range(1,152):
        response = re.get(f"https://pokeapi.co/api/v2/pokemon/{i}")
        data = response.json()
        lista_habilidades = []
        url_imagen = response.json()['sprites']['front_default']
        for x in response.json()["abilities"]:
            lista_habilidades.append(x["ability"]["name"] )
        
        pokemon.loc[i] = [data["name"],', '.join(lista_habilidades),url_imagen]
    print(pokemon.to_string())

primera_generacion()
