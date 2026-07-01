from inputs import(
    ingresar_dni
)
from alumnos import(
    buscar_alumno
)
def mostrar_menu() -> None:
    print("=========== GESTIÓN DE SALUMNOS ===========")  
    print("")    
    print("1.   Registrar alumno")
    print("2.   Listado alumnos")
    print("3.   Buscar alumno")
    print("4.   Modificar alumno")
    print("5.   Eliminar alumno")
    print("6.   Ver estadísticas")
    print("7.   Salir")

#La función recibe un diccionario y accede a cada dato utilizando la clave correspondiente.
def mostrar_alumno(alumno:dict) -> None:
    """Muestra los datos de un alumno.

    Args:
        alumno (dict): Diccionario con los datos del alumno.
    """

    print(f"DNI: {alumno['dni']}")
    print(f"Nombre: {alumno['nombre']}")
    print(f"Apellido: {alumno['apellido']}")
    print(f"Edad: {alumno['edad']}")
    print(f"Nota: {alumno['nota']}")

def mostrar_busqueda_alumno(lista_alumnos:list) -> None:
    """Solicita un DNI, busca el alumno y muestra sus datos.

    Args:
        lista_alumnos (list): Lista de alumnos registrados.
    """

    dni = ingresar_dni()

    alumno = buscar_alumno(lista_alumnos, dni)

    if alumno:
        mostrar_alumno(alumno)
    else:
        print("Alumno inexistente.")
        