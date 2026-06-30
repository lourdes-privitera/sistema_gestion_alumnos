def validar_entero(texto: str) -> bool:
    """Valida que una cadena represente un número entero positivo.

    Args:
        texto (str): Cadena a validar.

    Returns: True si la cadena contiene únicamente dígitos y no está vacía,
        False en caso contrario.
    """

    retorno = True

    if validar_longitud_minima(texto,1) == False:
        retorno = False
        
    for c in texto: # Validar que todos los caracteres sean dígitos
        if c < "0" or c > "9":
            retorno = False

    return retorno

def validar_rango(texto:str, valor_minimo:float, valor_maximo:float) -> bool:
    """Valida que un número se encuentre dentro de un rango determinado.

    Args:
        texto (str): Número a validar en formato texto.
        valor_minimo (float): Valor mínimo permitido.
        valor_maximo (float): Valor máximo permitido.

    Returns: bool: True si el número se encuentra dentro del rango indicado,
        False en caso contrario.
    """

    retorno = True
    numero = float(texto)

    if numero < valor_minimo or numero > valor_maximo:
        retorno = False

    return retorno

def validar_opcion(opcion:str) -> bool:
    """Valida que la opción del menú sea un número entero entre 1 y 7.

    Args:
        opcion (str): Opción ingresada por el usuario.

    Returns: bool: True si la opción es válida, False en caso contrario.
    """

    retorno = True

    if validar_entero(opcion) == False:        
        retorno = False        
    elif validar_rango(opcion,1,7) == False:
        retorno = False

    return retorno 

def validar_longitud_minima(cadena:str,minimo:int) -> bool:
    """Valida que una cadena tenga una longitud minima determinada.

    Args:
        cadena (str): Cadena a validar.
        minimo (int): Cantidad mínima de caracteres requerida.

    Returns: bool: True si la longitud de la cadena es mayor o igual al mínimo indicado,
        False en caso contrario.
    """

    retorno = False

    if len(cadena) >= minimo :
        retorno = True

    return retorno

def validar_letras (texto:str)-> bool :
    """Valida que una cadena contenga únicamente letras y espacios.

    Args:
        texto (str): Cadena a validar.

    Returns: bool: True si la cadena contiene únicamente letras y espacios, False en caso contrario.

    """
    retorno = True

    for c in texto:

        if not ("A" <= c <= "Z") and not ("a" <= c <= "z") and c != " ":
            retorno = False

    return retorno

