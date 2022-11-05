from TrabajoFinUnidad.ramaLuis import *
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
    a = int(input("SI QUIERE SALIR INGRESE 0\nINGRESA NUMERO"));
    if a==0:
        break;
    if a == 1:
        getCrearCsv()

    if a == 2:
        milibro = Libro('./bbdd.csv')
        milibro.getLeerRegistrosLibros();
    if a==3:
        milibro = Libro('./bbdd.csv')
        milibro.setRegistrarLibros();

    if a == 4:
        milibro = Libro('./bbdd.csv')
        milibro.deleteRegistro();
        
    if a == 5:
        milibro = Libro('./bbdd.csv')
        milibro.buscarTituloISBN();

    if a == 6:
      milibro = Libro('./bbdd.csv')
      milibro.ordenarTitulo();
    if a == 7:
      milibro = Libro('./bbdd.csv')
      milibro.buscarAutorEditorialGenero();
      
    # if a == 8:
    # if a == 9:
    # if a == 10:
