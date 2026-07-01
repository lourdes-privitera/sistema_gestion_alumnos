from inputs import (
    pedir_datos_alumno,
    ingresar_dni,
    ingresar_nombre,
    ingresar_apellido,
    ingresar_edad,
    ingresar_nota_final
)

#Voy recorriendo toda la lista de alumnos. Cada elemento es un diccionario. Comparo el DNI guardado con el DNI ingresado.
def buscar_dni(lista_alumnos:list, dni:int) -> bool:
    """Verifica si un DNI ya se encuentra registrado.

    Args:
        lista_alumnos (list): Lista de alumnos .
        dni (int): DNI a buscar.

    Returns: bool: True si el DNI existe, False en caso contrario.
    """

    retorno = False

    for alumno in lista_alumnos:
        if alumno["dni"] ==  dni:
            retorno = True

    return retorno  

#Obtiene todos los datos del alumno y los guarda en un único diccionario.
def registrar_alumno(lista_alumnos:list) -> list:
    """Registra un nuevo alumno verificando que el DNI no esté repetido.

    Args:
        lista_alumnos (list): Lista de alumnos registrados.
    """

    alumno = pedir_datos_alumno()

    while buscar_dni(lista_alumnos, alumno["dni"]):

        print("ERROR: El DNI ya se encuentra registrado.")

        alumno["dni"] = ingresar_dni()

    lista_alumnos += [alumno] # Agrega el nuevo alumno al final de la lista.

    return lista_alumnos

def buscar_alumno(lista_alumnos:list, dni:int) -> dict:
    """Busca un alumno por DNI.

    Args:
        lista_alumnos (list): Lista de alumnos.
        dni (int): DNI buscado.

    Returns: dict: Diccionario del alumno si existe. None: Si no se encuentra.
    """

    retorno = None

    for alumno in lista_alumnos:

        if alumno["dni"] == dni:
            retorno = alumno
            break

    return retorno

def modificar_alumno(lista_alumnos:list) -> None:
    """Modifica los datos de un alumno existente.

    Solicita el DNI, busca al alumno correspondiente y permite
    actualizar su nombre, apellido, edad y nota final.

    Args:
        lista_alumnos (list): Lista de alumnos registrados.
    """

    dni = ingresar_dni()

    alumno = buscar_alumno(lista_alumnos, dni)

    if alumno:

        print("\nIngrese los nuevos datos:\n")

        alumno["nombre"] = ingresar_nombre()
        alumno["apellido"] = ingresar_apellido()
        alumno["edad"] = ingresar_edad()
        alumno["nota"] = ingresar_nota_final()

        print("Alumno modificado correctamente.")

    else:
        print("Alumno inexistente.")

def eliminar_alumno(lista_alumnos:list) -> None:
    """Elimina un alumno mediante su DNI.

    Recorre la lista de alumnos hasta encontrar el DNI indicado
    y elimina ese registro de la lista.

    Args:
        lista_alumnos (list): Lista de alumnos registrados.
    """

    dni = ingresar_dni()

    indice = 0
    encontrado = False

    while indice < len(lista_alumnos) and encontrado == False:

        if lista_alumnos[indice]["dni"] == dni:

            del lista_alumnos[indice]

            encontrado = True

        else:
            indice += 1

    if encontrado:
        print("Alumno eliminado correctamente.")
    else:
        print("Alumno inexistente.")