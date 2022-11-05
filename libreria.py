from csv import writer, reader


################################################

class Libro:
    
    
    def __init__(self,id,titulo,genero,ISNB,editorial,autores):
        self.id = id
        self.titulo = titulo
        self.genero = genero
        self.ISNB = ISNB
        self.editorial = editorial
        self.autores = autores
    
    
    def __del__(self):
        print("Esto elimina libros")   
######################################################

""" print(¿En que puedo ayudarte hoy?\n
    1)  Cargar base de datos
    2)  Listar libros
    3)  Agregar libros
    4)  Eliminar libros
    5)  Buscar libros (ISBN/título)
    6)  Ordenar libros por orden alfabetico
    7)  Buscar libros (autor/editorial/genero)
    8)  Buscar libros por cantidad de autores
    9)  Actualizar datos de libros
    10) Guardar nueva base de datos \n) """
##########################################################
with open('./lista.csv','w') as file:
    header = ('id','titulo','genero','ISBN','editorial','autores')
    csv_writer = writer (file, lineterminator = '\n')
    data = [
        [1,"Amazing Spider-Man","comic","0785123370","Marvel","John Michael Straczynski / Ron Garney"],
        [2,"Fight Club","novela","0393355942","W. W. Norton & Company","Chuck Palahniuk"],
        [3,"Trainspotting","novela","9780393314809","W. W. Norton & Company","Irvine Welsh"]
    ]

    csv_writer.writerow(header)
    csv_writer.writerows(data)

with open('./lista.csv') as file:
    csv_reader = reader(file)
    for row in csv_reader:
        print(row)
