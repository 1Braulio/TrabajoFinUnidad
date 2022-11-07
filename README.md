# TrabajoFinUnidad
## Proyecto Libreria:
Para usar correctamente el programa primero hay que crear el archivo csv,para esto ejecutamos el archivo opciones.py con el comando-> python opciones.py <-
Para el correcto funcionamiento del programa instala la biblioteca Pandas con el siguiente comando -> py -m pip install pandas <-

El programa permite lo siguiente:
        1)  Cargar base de datos
        2)  Listar libros
        3)  Agregar libros
        4)  Eliminar libros
        5)  Buscar libros (ISBN/título)
        6)  Ordenar libros por orden alfabetico
        7)  Buscar libros (autor/editorial/genero)
        8)  Buscar libros por cantidad de autores
        9)  Actualizar datos de libros
        10) Guardar nueva base de datos

## Pokemon api (trabajo_pokemon):
Con menu.py se accede al menu de opciones de listado de pokemon. Este módulo importa las funciones de pokemon_class.py para obtener diccionarios de pokemon de acuerdo a los distintos criterios disponibles (generacion, tipo, habilidad, forma y habitat), donde cada criterio es una key del diccionario, el cual retorna la lista correspondiente. menu.py llama la función correspondiente para obtener el diccionario el cual usa para listar los pokemon con get_pokemon(dict). 
