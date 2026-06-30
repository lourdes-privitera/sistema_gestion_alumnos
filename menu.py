from validaciones import (
    validar_opcion
)
from inputs import(
    ingresar_dni,
    ingresar_nombre_alumno,
    ingresar_edad,
    ingresar_nota_final
)
from output import(
    mostrar_menu
)

def ejecutar_sistema() -> None:

    hay_alumnos = False 
    programa_activo = True  

    while programa_activo:

        mostrar_menu()

        opcion_texto = input("Seleccionar opcion: ")
        
        while validar_opcion(opcion_texto) == False:
            opcion_texto = input("Reingrese una opcion valida: ")

        opcion = int(opcion_texto)
            
        if opcion == 1:

            dni = ingresar_dni()
            alumno = ingresar_nombre_alumno()
            edad = ingresar_edad()
            nota_final = ingresar_nota_final()
            #datos_alumno = [dni(),alumno(),edad(),nota_final()]                  
            hay_alumnos = True
            
        elif opcion == 7:
            print("SALIENDO...")
            programa_activo = False 
            
        elif hay_alumnos:         # Solo si ya se cargó alumno
            
            if opcion == 2:
                print()
            
            elif opcion == 3:
                print()

            elif opcion == 4:
                print()

            elif opcion == 5:
                print()

            elif opcion == 6:
                print() 

        else:
            print(f"¡¡¡NO SE PUEDE ACCEDER A LA OPCION {opcion} SIN CARGAR ALUMNOS!!!")
            
        if programa_activo:
            input("\nPresione Enter para continuar...")

