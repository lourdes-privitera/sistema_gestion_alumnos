from inputs import (
    pedir_datos_alumno,
    ingresar_dni
)
from output import (
    mostrar_alumno
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

def listar_alumnos(lista_alumnos:list) -> None:
    """Muestra todos los alumnos registrados.

    Args:
        lista_alumnos (list): Lista de alumnos.
    """

    print("\n======= LISTADO DE ALUMNOS =======\n")

    for alumno in lista_alumnos:

        mostrar_alumno(alumno)

        print("-----------------------------")

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
