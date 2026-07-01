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
        
def listar_alumnos(lista_alumnos:list) -> None:
    """Muestra todos los alumnos registrados.

    Args:
        lista_alumnos (list): Lista de alumnos.
    """

    print("\n======= LISTADO DE ALUMNOS =======\n")

    for alumno in lista_alumnos:

        mostrar_alumno(alumno)

        print("-----------------------------")

def mostrar_estadisticas(lista_alumnos:list)->None:
    """Muestra las estadísticas generales de los alumnos.

    Informa:
        - Cantidad total de alumnos.
        - Promedio de notas.
        - Alumno con mayor nota.
        - Cantidad de aprobados.
        - Cantidad de desaprobados.

    Args:
        lista_alumnos (list): Lista de alumnos registrados.
    """    

    from estadisticas import (
        cantidad_alumnos,
        promedio_notas,
        mejor_alumno,
        cantidad_aprobados,
        cantidad_desaprobados
    )

    print("\n===== ESTADÍSTICAS =====")

    print(f"Cantidad de alumnos: {cantidad_alumnos(lista_alumnos)}")

    print(f"Promedio: {promedio_notas(lista_alumnos):.2f}")

    mejor = mejor_alumno(lista_alumnos)

    if len(lista_alumnos) > 0:

        mejor = mejor_alumno(lista_alumnos)

        print(f"Mayor nota: {mejor['nombre']} {mejor['apellido']} ({mejor['nota']})")

    print(f"Aprobados: {cantidad_aprobados(lista_alumnos)}")

    print(f"Desaprobados: {cantidad_desaprobados(lista_alumnos)}")