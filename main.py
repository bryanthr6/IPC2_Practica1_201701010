from auto import Auto
from cliente import Cliente
from compra import Compra

autos = []
clientes = []
compras = []
id_auto = 0
id_cliente = 0
id_compra = 0

def main():
    opcion = 0
    while opcion != 6:
        print("              SUPER AUTOS GT")
        print(" ")
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
                crear_auto()
            case 2:
                crear_cliente()
            case 3:
                realizar_compra()
            case 4:
                mostrar_reporte_compras()
            case 5:
                print('------------------------------------')
                print('|DATOS DEL ESTUDIANDTE             |')
                print('|Carnet: 201701010                 |')
                print('|Nombre: Bryant Herrera Rubio      |')
                print('------------------------------------')
                print(" ")
            case 6:
                print("Saliendo...")    
            case _:
                print("ERROR: Opción no válida")
                print(" ")

def crear_auto():
    global id_auto
    print("***************Registro de Auto***************")
    placa = input("Ingrese la placa del auto: ")
    marca = input("Ingrese la marca del auto: ")
    modelo = input("Ingrese el modelo del auto: ")
    descripcion = input("Ingrese la descripción del auto: ")
    precio = float(input("Ingrese el precio del auto: Q "))
    nuevo = Auto(placa, marca, modelo, descripcion, precio)
    autos.append(nuevo)
    id_auto += 1
    print("Auto registrado exitosamente")
    print(" ")

def crear_cliente():
    global id_cliente
    print("***************Registro de Cliente***************")
    nombre = input("Ingrese el nombre del cliente: ")
    email = input("Ingrese el email del cliente: ")
    nit = input("Ingrese el NIT del cliente: ")
    nuevo = Cliente(nombre, email, nit)
    clientes.append(nuevo)
    id_cliente += 1
    print("Cliente registrado exitosamente")
    print(" ")

def realizar_compra():
    print("***************Realizar Compra***************")
    nit_cliente = input("Ingrese el NIT del cliente: ")

    # Verificar si el cliente existe
    cliente = next((c for c in clientes if c.nit == nit_cliente), None)
    
    if cliente is None:
        print("ERROR: Cliente no encontrado.")
        print(" ")
        return
    print("Cliente encontrado.")

    # Crear una nueva compra para este cliente
    nueva_compra = Compra(cliente)

    opcion = 0
    while opcion != 2:
        print("  ")
        print("***************Menú de Compras***************")
        print(f"Cliente: {cliente.nombre} NIT: {cliente.nit}.")
        print("1. Agregar Auto")
        print("2. Terminar Compra y Facturar")
        print("*********************************************")
        print(" ")
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("ERROR: No ingresó un número entero")
            continue
        match opcion:
            case 1:
                agregar_auto_a_compra(nueva_compra)
            case 2:
                # Preguntar si incluir seguro
                nueva_compra.con_seguro = obtener_opcion_seguro()
                print("Compra finalizada. Facturando...")
                nueva_compra.mostrar_compra()
                compras.append(nueva_compra)
                print(" ")
                break
            case _:
                print("ERROR: Opción no válida")
                print(" ")


def agregar_auto_a_compra(compra):
    placa_auto = input("Ingrese la placa del auto: ")

    #Buscar el auto por la placa en la lista de autos
    auto = next((a for a in autos if a.placa == placa_auto), None)

    if auto is None:
        print("ERROR: Auto no encontrado.")
        print(" ")
        return
    
    compra.agregar_auto(auto)
    print(f"Auto {auto.marca}, {auto.modelo} agregado a la compra exitosamente.")
    print(" ")

def mostrar_reporte_compras():
    print("***************Reporte de Compras***************")
    
    total_general = 0
    
    for compra in compras:
        compra.mostrar_compra()  # Mostrar detalles de la compra
        # Sumar el total de la compra, considerando el seguro si está activado
        if compra.con_seguro:
            total_general += compra.total + (0.15 * compra.total)
        else:
            total_general += compra.total
    
    print(f"\nTotal General: Q{total_general:.2f}")
    print(" ")


def obtener_opcion_seguro():
    while True:
        print("***************Incluir Seguro***************")
        print("1. Si")
        print("2. No")
        print("********************************************")
        
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                return True
            elif opcion == 2:
                return False
            else:
                print("ERROR: Opción no válida. Por favor seleccione 1 o 2.")
        except ValueError:
            print("ERROR: No ingresó un número entero. Por favor intente nuevamente.")


if __name__ == '__main__':
    main()
