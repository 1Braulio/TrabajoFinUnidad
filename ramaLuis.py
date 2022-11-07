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
            nuevo_ID = len(self.__df)+1
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

        self.__a=a
        self.__df.drop(self.__df.index[[self.a-1]],inplace=True)

        self.__df.to_csv(self.__ruta, index=None, mode="w", header=True,columns=columnas)


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
            dfcopia['AUTOR'] = dfcopia['AUTOR'].str.lower()
            print(dfcopia[dfcopia['AUTOR'].str.contains(a)])
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

    def buscarAutor(self):

        f=self.__df[self.__df['AUTOR'].str.contains('/')]
        indices=f.index


        autores=list(f.AUTOR)

        index_slash={}
        for i in range (0,len(indices),1):

            a=list(autores[i])
            index_slash.__setitem__(indices[i],a.count('/'))
            # print(i,a.count('/'))



        #print(index_slash)
        #print(contador)
        #print(index_slash.get(1))

         #numero ingresado por el usuario
        p = int(input("INGRESA NUMERO DE AUTORES: "))-1
        indiceFinal=[]
        for j in index_slash:
            if index_slash.get(j)==p:
                 indiceFinal.append(j)
                 #print(j) #imprime ids de las filas que debo imprimr

        mostrar_datos=[]

        for i in indiceFinal:
            asd=self.__df[self.__df.index==i]
            mostrar_datos.append(asd)


        print(mostrar_datos)


    def editarRegistro(self):

        columnas = ["ID", "TITULO", "GENERO", "ISBN", "EDITORIAL", "AUTOR"]


        while True:
            limiteId=len(self.__df.axes[0])

            while True:
                fila = int(input("INGRESA ID DE REGISTRO: ")) - 1
                if fila>=limiteId:
                    print("Ingresa ID valido")
                    #fila = int(input("INGRESA ID DE REGISTRO: ")) - 1
                else: break;
            print("-"*20)
            print("\nTITULO:    2"
                  "\nGENERO:    3"
                  "\nISBN :     4"
                  "\nEDITORIAL: 5"
                  "\nAUTOR:     6")
            while True:
                col=int(input("INGRESA COLUMNA: "))
                if col<2 or col>6:
                    print("Ingresa dato valido")
                else:break;

            valorReemplazo=input("INGRESA VALOR NUEVO: ")
            if col==2:
                self.__df.loc[fila, 'TITULO'] = valorReemplazo
                self.__df.to_csv(self.__ruta, index=None, mode="w", header=True, columns=columnas)
                print("VALOR CAMBIADO EXITOSAMENTE")
                self.getLeerRegistrosLibros()

            elif col==3:
                self.__df.loc[fila, 'GENERO'] = valorReemplazo
                self.__df.to_csv(self.__ruta, index=None, mode="w", header=True, columns=columnas)
                print("VALOR CAMBIADO EXITOSAMENTE")
                self.getLeerRegistrosLibros()

            elif col==4:
                self.__df.loc[fila, 'ISBN'] = valorReemplazo
                self.__df.to_csv(self.__ruta, index=None, mode="w", header=True, columns=columnas)
                print("VALOR CAMBIADO EXITOSAMENTE")
                self.getLeerRegistrosLibros()

            elif col==5:
                self.__df.loc[fila, 'EDITORIAL'] = valorReemplazo
                self.__df.to_csv(self.__ruta, index=None, mode="w", header=True, columns=columnas)
                print("VALOR CAMBIADO EXITOSAMENTE")
                self.getLeerRegistrosLibros()

            elif col==6:
                self.__df.loc[fila, 'AUTOR'] = valorReemplazo
                self.__df.to_csv(self.__ruta, index=None, mode="w", header=True, columns=columnas)
                print("VALOR CAMBIADO EXITOSAMENTE")
                self.getLeerRegistrosLibros()



            if input("SEGUIR? Y/N").lower()=="y":
                break;
            print("CONTINUAMOS");



    def guardarLibros(self):
        print(f"Libros guardados correcatamente en el archivo {self.__ruta}")