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
            while not nuevo_ID.isnumeric(): # validacion
                nuevo_ID = input("INGRESE su ID (solo puede ser numerico): ")
            nuevo_ID = int(nuevo_ID)
            ID.append(nuevo_ID)

            nuevo_TITULO = input("INGRESE TITULO: ")
            TITULO.append(nuevo_TITULO)

            nuevo_GENERO = input("INGRESE su GENERO: ")
            GENERO.append(nuevo_GENERO)

            nuevo_ISBN = input("INGRESE ISBN: ")
            while not nuevo_ISBN.isnumeric(): # validacion
                nuevo_ISBN = input("INGRESE ISBN (solo puede ser numerico): ")
            nuevo_ISBN = int(input("INGRESE ISBN: "))
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

            a = input("SALIR? Y/N: ").upper()
            while a not in ["Y", "N"]: # validacion
                a = input("SALIR? Y/N (ingrese una opcion valida): ")

            if a == "Y":
                print("ADIOS")
                break;
            if a == "N":
                print("CONTINUAMOS")

        columnas = ["ID", "TITULO", "GENERO", "ISBN", "EDITORIAL", "AUTOR"]

        df = pd.DataFrame(list(zip(ID, TITULO, GENERO, ISBN, EDITORIAL, AUTOR)), columns=columnas)


        df.to_csv(self.__ruta, index=None, mode="a", header=False)

    #ELIMINA SOLO POR ID
    def deleteRegistro(self,a):
        columnas = ["ID", "TITULO", "GENERO", "ISBN", "EDITORIAL", "AUTOR"]

        self.a=a
        #df = pd.read_csv(self.ruta)
        self.df.drop(self.df.index[[self.a-1]],inplace=True)

        #ad=pd.DataFrame(df,columns=columnas)
        self.df.to_csv(self.ruta, index=None, mode="w", header=True,columns=columnas)


    def buscarTituloISBN(self):
        print("Buscar ISBN    : 1\nBuscar Titulo  : 0")
        q=input("INGRESA NUMERO: ")
        while q not in ['0','1']:
            print("Buscar ISBN    : 1\nBuscar Titulo  : 0")
            q=input("INGRESA NUMERO (0 o 1): ")
        q=int(q)
        if q==1:
            # a=int(input("INGRESE ISBN: "))
            # print(self.df[self.df.ISBN==a])
            a=input("INGRESE ISBN: ")
            while not a.isnumeric():
                a=input("INGRESE ISBN (solo debe contener numeros): ")
            a = int(a)
            print("\nLibros:")
            print(self.__df[self.__df.ISBN==a]['TITULO'])
        if q==0:
            a=input("Ingrese titulo: ")
            # self.df['TITULO']=self.df['TITULO'].str.lower()
            # print(self.df[self.__df['TITULO'].str.contains(a)])
            self.__df['TITULO']=self.__df['TITULO'].str.lower()
            print("\nLibros:")
            print(self.__df[self.__df['TITULO'].str.contains(a)]['TITULO'])
    
    def ordenarTitulo(self):
        print(self.__df.sort_values('TITULO'))


    def buscarAutorEditorialGenero(self):
        print("Buscar Autor    : 1\nBuscar Editorial  : 2\nBuscar Genero   :3")
        q=int(input("INGRESA NUMERO: "))
        if q==1:
            a = input("Ingrese Autor: ")
            dfcopia = self.__df.copy() # copia para no alterar los libros
            dfcopia['AUTORES'] = dfcopia['AUTORES'].str.lower()
            print(dfcopia[dfcopia['AUTORES'].str.contains(a)])
        if q==2:
            a=input("Ingrese Editorial: ")
            dfcopia = self.__df.copy()
            dfcopia['EDITORIAL']=dfcopia['EDITORIAL'].str.lower()
            print(dfcopia[dfcopia['EDITORIAL'].str.contains(a)])
        if q==3:
            a=input("Ingrese Genero: ")
            dfcopia = self.__df.copy()
            dfcopia['GENERO']=dfcopia['GENERO'].str.lower()
            print(dfcopia[dfcopia['GENERO'].str.contains(a)])
