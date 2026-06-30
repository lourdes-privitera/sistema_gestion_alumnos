from validaciones import (
    validar_longitud_minima,
    validar_rango,
    validar_entero,
    validar_letras
)

def pedir_numero(mensaje:str, longitud:int, minimo:int, maximo:int) -> int:
    """Solicita un número entero y verifica que:
        - No esté vacío.
        - Contenga únicamente dígitos.
        - Cumpla con la longitud mínima indicada.
        - Se encuentre dentro del rango permitido.

    Args:
        mensaje (str): Mensaje mostrado al usuario.
        longitud (int): Cantidad mínima de dígitos requerida.
        minimo (int): Valor mínimo permitido.
        maximo (int): Valor máximo permitido.

    Returns: int: Número entero validado.
    """

    numero = input(mensaje)
    ingreso_valido = False

    while ingreso_valido == False:

        bandera_validada = True

        if validar_entero (numero) == False:
            print(f"----------------¡¡DEBE INGRESAR UN N° ENTERO!!----------------")
            bandera_validada = False  
                    
        if bandera_validada and validar_longitud_minima(numero,longitud) == False:            
            print("--------------¡¡NO CUMPLE CON LOS DIGITOS MINIMOS!!-------------")
            bandera_validada = False
                                
        if bandera_validada and validar_rango (numero,minimo,maximo) == False:
            print(f"----¡¡FUERA DE RANGO (ingresar n° de {minimo} a {maximo})!!----")
            bandera_validada = False
        
        if bandera_validada:
            ingreso_valido = True
            
        else:
            print("---------------------------INVALIDO----------------------------")
            numero = input("Reingrese un número válido: ")

    return int(numero)

def ingresar_dni() -> int:
    """Solicita y valida el DNI del alumno.

    Returns: int: DNI ingresado.
    """
    return pedir_numero("Ingrese DNI del alumno: ",6, 0, 99999999)

def ingresar_edad() -> int:
    """Solicita y valida la edad del alumno.

    Returns: int: Edad ingresada.
    """
    return pedir_numero("Ingrese edad del alumno: ",1, 0, 100)

def ingresar_nota_final() -> int:
    """Solicita y valida la nota final del alumno.

    Returns: int: Nota final ingresada.
    """
    return pedir_numero("Ingrese nota final del alumno: ",1, 0, 10)

def ingresar_nombre_alumno() -> str:
    """Solicita y valida el nombre del alumno.
        - Tener al menos 3 caracteres.
        - Contener únicamente letras y espacios.

    Returns: str: Nombre del alumno validado.
    """

    nombre = input("Ingrese nombre del alumno: ")

    while validar_longitud_minima(nombre, 3) == False or validar_letras(nombre) == False:

        print("----------------------- INVÁLIDO -----------------------")
        print("Debe contener al menos 3 caracteres y solo letras.")
        nombre = input("Reingrese nombre del alumno: ")

    return nombre

