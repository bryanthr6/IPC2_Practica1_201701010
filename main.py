def main():
    opcion=0
    while opcion != 6:
        print("***************Menú Principal***************")
        print("*1. Registrar Auto                         *")
        print("*2. Registrar Cliente                      *")
        print("*3. Realizar Compra                        *")
        print("*4. Reporte de Compras                     *")
        print("*5. Datos del Estudiante                   *")
        print("*6. Salir                                  *")
        print("********************************************")
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("ERROR: No ingresó un número entero")
            continue
        match opcion:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                print('------------------------------------')
                print('|DATOS DEL ESTUDIANDTE             |')
                print('|UNIVERSIDAD DE SAN CARLOS         |')
                print('|FACULTAD DE INGENIERIA            |')
                print('|ESCUELA DE CIENCIAS Y SISTEMAS    |')
                print('|Carnet: 201701010                 |')
                print('|Nombre: Bryant Herrera Rubio      |')
                print('------------------------------------')
            case 6:
                print("Saliendo...")    
            case _:
                print("ERROR: Opción no válida")

if __name__ == '__main__':
    main()