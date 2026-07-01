import json


def guardar_alumnos(lista_alumnos: list) -> None:
    """Guarda la lista de alumnos en un archivo JSON.

    Args:
        lista_alumnos (list): lista de alumnos a guardar.
    """

    archivo = open("alumnos.json", "w", encoding="utf-8")
    json.dump(lista_alumnos, archivo, indent=4)
    archivo.close()


def cargar_alumnos() -> list:
    """Carga la lista de alumnos desde un archivo JSON.

    Returns:
        list: lista de alumnos. Si el archivo no existe, retorna lista vacía.
    """

    try:
        archivo = open("alumnos.json", "r", encoding="utf-8")
        lista = json.load(archivo)
        archivo.close()
    except:
        lista = []

    return lista