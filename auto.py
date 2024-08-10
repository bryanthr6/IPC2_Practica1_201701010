class Auto:
    def __init__(self, placa, marca, modelo, descripcion, precio):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.descripcion = descripcion
        self.precio = precio
    
    #Métodos y otros
    def get_placa(self):
        return self.placa
    
    def set_placa(self, placa):
        self.placa = placa

    def get_marca(self):
        return self.marca
    
    def set_marca(self, marca):
        self.marca = marca

    def get_modelo(self):
        return self.modelo 
    
    def set_modelo(self, modelo):
        self.modelo = modelo   
    
    def get_descripcion(self):
        return self.descripcion
    
    def set_descripcion(self, descripcion):
        self.descripcion = descripcion
    
    def get_precio(self):
        return self.precio 
    
    def set_precio(self, precio):
        self.precio = precio