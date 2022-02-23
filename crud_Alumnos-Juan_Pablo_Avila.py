import operator
import os

def ingresar_nombre():
    """ función para ingresar un nombre de estudiante"""
    while True:
        nombre = input("Ingrese el nombre del estudiante: ")
        if nombre=="":
            print("Debe ingresar un nombre!")
        else:
            return nombre

def ingresar_edad():
    """ funcion para ingresar la edad del alumno """
    while True:
        try:
            edad = int(input("Ingrese la edad del alumno (18 a 95 años):"))
            if 18<=edad<=95:
                return edad
            else:
                print("la edad permitida es entre 18 y 95 años")
        except:
            print("la edad tiene que ser un número...")

def ingresar_nota():
    """ funcion para ingresar una nota """
    while True:
        try:
            nota = float(input("Ingrese la nota del estudiante (0 a 10):"))
            if 0<=nota<=10:
                return nota
            else:
                print("la nota tiene que ser un valor entre 0 y 10")
        except:
            print("la nota tiene que ser un valor numérico") 

def cargar_estudiante():
    """función para cargar los datos por teclado del estudiante y devolver una lista con esos valores"""
    estud =[]
    estud.append(ingresar_nombre())
    estud.append(ingresar_edad())
    estud.append(ingresar_nota())

    print(f"Datos cargados: {estud[0]}, {estud[1]} años, nota {estud[2]}")
    return estud

def buscar_estudiante_nombre(nombre):
    """función para buscar estudiantes de la lista, por su nombre"""
    cont=0
    for estudiante in lista_estudiantes:
        if estudiante[0] == nombre:
            print(f"Datos encontrados: {estudiante[0]}, {estudiante[1]} años, nota {estudiante[2]}")
            cont+=1
    if cont == 0:                
        print("No se encontró un estudiante registrado con ese nombre.")

def borrar_estudiante(nombre):
    """función para eliminar estudiantes de la lista, por su nombre"""
    try:
        cont = 0
        for alumno in lista_estudiantes:
            if alumno[0] == nombre:
                lista_estudiantes.remove(alumno)
                print(f"Alumno {nombre} borrado de la lista")
                cont+=1
        if cont == 0:                
            print("No se encontró un estudiante registrado con ese nombre.")
    except:
        print("Ocurrió un error al borrar!")

def modificar_nota(nombre):
    """función para modificar la nota de un estudiante"""
    cont=0
    for estudiante in lista_estudiantes:
        if estudiante[0] == nombre:
            print(f"Datos encontrados: {estudiante[0]}, {estudiante[1]} años, nota {estudiante[2]}")
            #solicito la nueva nota para modificar y muestro el cambio
            estudiante[2] = ingresar_nota()
            print(f"Nueva nota confirmada: {estudiante[0]}, {estudiante[1]} años, nota {estudiante[2]}")
            cont+=1
    if cont == 0:                
        print("No se encontró un estudiante registrado con ese nombre.")

def promediar_notas():
    """ funcion para calcular y mostrar el promedio de notas de los estudiantes"""
    if len(lista_estudiantes)==0:
        return -1
    return sum(x[2] for x in lista_estudiantes)/len(lista_estudiantes)

def promediar_edades():
    """ funcion para calcular y mostrar el promedio de edades de los estudiantes"""
    if len(lista_estudiantes)==0:
        return -1
    return sum(x[1] for x in lista_estudiantes)/len(lista_estudiantes)

def validar_lista_estudiantes():
    """función que nos permite determinar si la lista de estudiantes está vacía"""
    if len(lista_estudiantes)==0:
        print ("La lista de estudiantes está vacía.\n")
        return False
    else:
        return True

def Menu():
    print("""-------------------------------------------------------
            Sistema de Gestión de Alumnos
-------------------------------------------------------
    Selecciona una opción...
    1 - Agregar estudiante
    2 - Buscar estudiante por nombre
    3 - Modificar nota
    4 - Listado ordenados por nombres
    5 - Listado ordenados por notas
    6 - Mostrar promedio de las notas
    7 - Borrar un estudiante
    8 - Calcular la edad promedio de los estudiantes
    0 - Salir
    """)

# --------------- Programa principal----------------------------

# definimos la lista de estudiantes (lista anidada de estudiantes, con sus datos)
lista_estudiantes = []

while True:
    Menu ()
    
    try:
        opcion = int(input("Ingrese el número de opción a realizar: "))
    except:
        opcion=-1
 
    if opcion == 1:
        # agregamos estudiante a la lista anidada, llamando a la función 
        lista_estudiantes.append(cargar_estudiante())
        print("Listado de estudiantes registrados\n",lista_estudiantes)
        os.system("pause")

    elif opcion == 2:
        #solicitamos ingresar el nombre a buscar, y llamamos a la función
        if validar_lista_estudiantes():
            buscar_estudiante_nombre(ingresar_nombre())
            os.system("pause")
        
    elif opcion == 3:
        #pedimos el nombre del estudiante, si lo encontramos en la lista, pedimos la nueva nota y modificamos
        if validar_lista_estudiantes():
            modificar_nota(ingresar_nombre())
            os.system("pause")

    elif opcion == 4:
        #Validamos el largo de la lista, e imprimimos ordenando por nombre
        if validar_lista_estudiantes():
            lista_orden_nombre = sorted(lista_estudiantes, key=operator.itemgetter(0))
            print("Lista ordenada por Nombre: ",lista_orden_nombre)
            os.system("pause")

    elif opcion == 5:
        #Validamos el largo de la lista, e imprimimos ordenando por nota ascendente
        if validar_lista_estudiantes():
            lista_orden_nota = sorted(lista_estudiantes, key=operator.itemgetter(2))
            print("Lista ordenada por Nota: ",lista_orden_nota)
        os.system("pause")
        
    elif opcion == 6:
        #Validamos el largo de la lista, y calculamos promedio de notas con redondeo
        if validar_lista_estudiantes():
            promedio_notas = round(promediar_notas(),2)
            print("El promedio de notas es de ",promedio_notas)
            os.system("pause")
        
    elif opcion == 7:
        #solicitamos ingresar el nombre del estudiante a borrar, y llamamos a la función
        if validar_lista_estudiantes():
            borrar_estudiante(ingresar_nombre())
            os.system("pause")

    elif opcion == 8:
        #Validamos el largo de la lista, y calculamos promedio de edad redondeado sin decimales
        if validar_lista_estudiantes():
            promedio_edad = int(promediar_edades())
            print(f"El promedio de edades es de {promedio_edad} años.")
            os.system("pause")

    elif opcion == 0:
        print("Gracias por usar nuestro sistema!")
        break
    
    else:
        print("La opción ingresada no es correcta, indica una opción correcta")
