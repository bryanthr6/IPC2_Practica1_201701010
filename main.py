#se importan las clases 
from auto import Auto
from cliente import Cliente

#Lista donde se almacenan los autos
autos = []
id_auto = 0

def main():
    opcion=0
    while opcion != 6:
        global id_auto  # Se indica que se usará la variable global id_auto
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
                pass
            case 3:
                realizar_compra()
            case 4:
                pass
            case 5:
                print('------------------------------------')
                print('|DATOS DEL ESTUDIANDTE             |')
                print('|Carnet: 201701010                 |')
                print('|Nombre: Bryant Herrera Rubio      |')
                print('------------------------------------')
            case 6:
                print("Saliendo...")    
            case _:
                print("ERROR: Opción no válida")

def crear_auto():
    global id_auto  # Se indica que se usará la variable global id_auto
    print("***************Registro de Auto***************")
    id = id_auto
    placa = input("Ingrese la placa del auto: ")
    marca = input("Ingrese la marca del auto: ")
    modelo = input("Ingrese el modelo del auto: ")
    descripcion = input("Ingrese la descripción del auto: ")
    precio = float(input("Ingrese el precio del auto: Q"))
    nuevo = Auto(placa, marca, modelo, descripcion, precio)
    autos.append(nuevo)
    id_auto += 1  # Incrementa el ID del auto

def crear_cliente():
    print("***************Registro de Cliente***************")
    nombre = input("Ingrese el nombre del cliente: ")
    email = input("Ingrese el email del cliente: ")
    nit = input("Ingrese el NIT del cliente: ")
    nuevo = Cliente(nombre, email, nit)
    return nuevo

def realizar_compra():
    global autos
    print("***************Realizar Compra***************")
    
    if len(autos) == 0:
        print("ERROR: No hay autos registrados")
        return
    
    print("Autos disponibles para compra:")
    for index, auto in enumerate(autos):
        print(f"{index + 1}. Placa: {auto.get_placa()}, Marca: {auto.get_marca()}, Modelo: {auto.get_modelo()}, Precio: Q{auto.get_precio()}")
    
    try:
        seleccion = int(input("Seleccione el número del auto que desea comprar: "))
        if 1 <= seleccion <= len(autos):
            auto_seleccionado = autos[seleccion - 1]
            print(f"Has seleccionado el auto con placa {auto_seleccionado.get_placa()} de marca {auto_seleccionado.get_marca()}.")
            # Aquí podrías continuar con el proceso de compra
        else:
            print("ERROR: Selección no válida")
    except ValueError:
        print("ERROR: No ingresó un número entero")


if __name__ == '__main__':
    main()