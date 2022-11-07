from TrabajoFinUnidad.ProyectoLibros.ramaLuis import *
import os
def opciones():
    print("¿En que puedo ayudarte hoy? "
        "\n1)  Cargar base de datos"
        "\n2)  Listar libros"
        "\n3)  Agregar libros"
        "\n4)  Eliminar libros"
        "\n5)  Buscar libros (ISBN/título)"
        "\n6)  Ordenar libros por orden alfabetico"
        "\n7)  Buscar libros (autor/editorial/genero)"
        "\n8)  Buscar libros por cantidad de autores"
        "\n9)  Actualizar datos de libros"
        "\n10) Guardar nueva base de datos");
    
while True:
    opciones()
    a = input("SI QUIERE SALIR INGRESE 0\nINGRESA NUMERO ")
    while a not in [str(n_opcion) for n_opcion in range(11)]:
        opciones()
        a = input("SI QUIERE SALIR INGRESE 0\nINGRESA NUMERO (1-10) ")
    a = int(a)

    if a==0:
        break;
    if a == 1:
        os.system("cls")
        getCrearCsv()

    milibro = Libro('./bbdd.csv')
    if a == 2:
        #milibro = Libro('./bbdd.csv')
        os.system("cls")
        milibro.getLeerRegistrosLibros();

    if a==3:
        #milibro = Libro('./bbdd.csv')
        os.system("cls")
        milibro.setRegistrarLibros();


    if a == 4:
       # milibro = Libro('./bbdd.csv')

        os.system("cls")
        milibro.deleteRegistro();

        
    if a == 5:
        #milibro = Libro('./bbdd.csv')
        os.system("cls")
        milibro.buscarTituloISBN();

    if a == 6:
      #milibro = Libro('./bbdd.csv')
      os.system("cls")
      milibro.ordenarTitulo();
    if a == 7:
      #milibro = Libro('./bbdd.csv')
      os.system("cls")
      milibro.buscarAutorEditorialGenero();
      
    if a == 8:
        os.system("cls")
        milibro.buscarAutor();

    if a == 9:
        os.system("cls")
        milibro.editarRegistro()

    if a == 10:
        os.system("cls")
        milibro.guardarLibros()
