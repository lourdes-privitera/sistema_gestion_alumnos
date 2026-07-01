def cantidad_alumnos(lista_alumnos:list) -> int:
    """Calcula la cantidad total de alumnos en la lista.

    Args:
        lista_alumnos (list): lista de alumnos.

    Returns:
        int: cantidad total de alumnos.
    """    

    return len(lista_alumnos)

def promedio_notas(lista_alumnos:list) -> float:
    """Calcula el promedio de las notas de los alumnos.

    Args:
        lista_alumnos (list): lista de alumnos con clave 'nota'.

    Returns:
        float: promedio de notas. Si la lista está vacía, retorna 0.
    """

    acumulador = 0

    for alumno in lista_alumnos:
        acumulador += alumno["nota"]

    if len(lista_alumnos) > 0:
        retorno = acumulador / len(lista_alumnos)
    else:
        retorno = 0

    return retorno

def mejor_alumno(lista_alumnos:list) -> dict:
    """Busca el alumno con la nota más alta.

    Args:
        lista_alumnos (list): lista de alumnos con clave 'nota'.

    Returns:
        dict: alumno con la mayor nota.
    """

    mejor = lista_alumnos[0]

    for alumno in lista_alumnos:

        if alumno["nota"] > mejor["nota"]:
            mejor = alumno

    return mejor

def cantidad_aprobados(lista_alumnos:list) -> int:
    """Cuenta la cantidad de alumnos aprobados (nota >= 6).

    Args:
        lista_alumnos (list): lista de alumnos con clave 'nota'.

    Returns:
        int: cantidad de alumnos aprobados.
    """

    contador = 0

    for alumno in lista_alumnos:

        if alumno["nota"] >= 6:
            contador += 1

    return contador

def cantidad_desaprobados(lista_alumnos:list) -> int:
    """Cuenta la cantidad de alumnos desaprobados (nota < 6).

    Args:
        lista_alumnos (list): lista de alumnos con clave 'nota'.

    Returns:
        int: cantidad de alumnos desaprobados.
    """

    contador = 0

    for alumno in lista_alumnos:

        if alumno["nota"] < 6:
            contador += 1

    return contador