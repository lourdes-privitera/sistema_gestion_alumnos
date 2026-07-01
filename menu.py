from archivos import (
    cargar_alumnos, 
    guardar_alumnos
)
from output import(
    mostrar_menu,
    mostrar_busqueda_alumno,
    listar_alumnos,
    mostrar_estadisticas
)

from validaciones import (
    validar_opcion
)

from alumnos import(
    registrar_alumno,
    modificar_alumno,
    eliminar_alumno
)

def ejecutar_sistema() -> None:

    lista_alumnos = cargar_alumnos()

    programa_activo = True  

    while programa_activo:

        mostrar_menu()

        opcion_texto = input("Seleccionar opcion: ")
        
        while validar_opcion(opcion_texto) == False:
            opcion_texto = input("Reingrese una opcion valida: ")

        opcion = int(opcion_texto)
            
        if opcion == 1:
            lista_alumnos = registrar_alumno(lista_alumnos)
            guardar_alumnos(lista_alumnos)                                         
            
        elif opcion == 7:
            print("SALIENDO...")
            programa_activo = False 
            
        elif lista_alumnos:         # Solo si ya se cargó alumno
            
            if opcion == 2:
                listar_alumnos(lista_alumnos)
            
            elif opcion == 3:
                mostrar_busqueda_alumno(lista_alumnos)

            elif opcion == 4:
                modificar_alumno(lista_alumnos)
                guardar_alumnos(lista_alumnos)

            elif opcion == 5:
                eliminar_alumno(lista_alumnos)
                guardar_alumnos(lista_alumnos)

            elif opcion == 6:
                mostrar_estadisticas(lista_alumnos)

        else:
            print(f"¡¡¡NO SE PUEDE ACCEDER A LA OPCION {opcion} SIN CARGAR ALUMNOS!!!")
            
        if programa_activo:
            input("\nPresione Enter para continuar...")

