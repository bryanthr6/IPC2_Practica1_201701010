from cliente import Cliente
from auto import Auto

class Compra:
    def __init__(self, cliente):
        self.cliente = cliente
        self.autos = []
        self.total = 0
        self.con_seguro = False  # Puedes ajustar esto según tu necesidad

    def agregar_auto(self, auto):
        self.autos.append(auto)
        self.total += auto.precio

    def mostrar_compra(self):
        total_con_seguro = self.total
        if self.con_seguro:
            total_con_seguro += 0.15 * self.total
        
        print(f"Nombre: {self.cliente.nombre}")
        print(f"Correo Electrónico: {self.cliente.email}")
        print(f"NIT: {self.cliente.nit}")
        print("Autos comprados:")
        for auto in self.autos:
            print(f"  {auto.marca} {auto.modelo} - Q {auto.precio}")
        
        #El 2f indica que se mostrarán dos decimales
        print(f"Total: Q {self.total:.2f}")
        if self.con_seguro:
            print(f"Total con Seguro: Q {total_con_seguro:.2f}")
        
        print("***************************************************")
        print(" ")
