import pandas as pd
from csv import *



def getCrearCsv():
    with open('./bbdd.csv', 'w') as file:
        header = ('ID', 'TITULO', 'GENERO', 'ISBN', 'EDITORIAL', 'AUTORES')
        csv_writer = writer(file, lineterminator='\n')
        data = [
            [1, "Amazing Spider-Man", "comic", "0785123370", "Marvel", "John Michael Straczynski / Ron Garney"],
            [2, "Fight Club", "novela", "0393355942", "W. W. Norton & Company", "Chuck Palahniuk"],
            [3, "Trainspotting", "novela", "9780393314809", "W. W. Norton & Company", "Irvine Welsh"]
        ]

        csv_writer.writerow(header)
        csv_writer.writerows(data)

    with open('./bbdd.csv') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            print(row)



class Libro():
    def __init__(self,ruta):
        self.__ruta = ruta#'./bbdd.csv' #"bbdd.csv"
        self.__df = pd.read_csv(self.__ruta)



    def getLeerRegistrosLibros(self):
        #nrows=3
        with open(self.__ruta) as file:
            csv_reader = reader(file)
            for row in csv_reader:
                print(row)
        #print(self.__df)

    def setRegistrarLibros(self):
        #,id,titulo,genero,ISBN,editorial,autor

        ID = []
        TITULO = []
        GENERO = []
        ISBN = []
        EDITORIAL = []
        AUTOR = []
        while True:
            nuevo_ID = input("INGRESE su ID: ")
            ID.append(nuevo_ID)

            nuevo_TITULO = input("INGRESE TITULO: ")
            TITULO.append(nuevo_TITULO)

            nuevo_GENERO = input("INGRESE su GENERO: ")
            GENERO.append(nuevo_GENERO)

            nuevo_ISBN = input("INGRESE ISBN: ")
            ISBN.append(nuevo_ISBN)

            nuevo_EDITORIAL = input("INGRESE su EDITORIAL: ")
            EDITORIAL.append(nuevo_EDITORIAL)

            nuevo_AUTOR = input("PARA MAS DE 2 AUTORES SEPARAR CON / \nINGRESE AUTOR: ")
            AUTOR.append(nuevo_AUTOR)

            # data = {
            #     "ID": ID,
            #     "TITULO": TITULO,
            #     "GENERO": GENERO,
            #     "ISBN": ISBN,
            #     "EDITORIAL": EDITORIAL,
            #     "AUTOR": AUTOR
            # };

            a = input("SALIR? Y/N: ")
            if a == "Y":
                print("ADIOS")
                break;
            print("CONTINUAMOS")

        columnas = ["ID", "TITULO", "GENERO", "ISBN", "EDITORIAL", "AUTOR"]

        df = pd.DataFrame(list(zip(ID, TITULO, GENERO, ISBN, EDITORIAL, AUTOR)), columns=columnas)


        df.to_csv(self.__ruta, index=None, mode="a", header=False)

